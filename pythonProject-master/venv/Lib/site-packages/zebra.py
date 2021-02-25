#!/usr/bin/env python3

# Copyright (c) 2011-2020 Ben Croston
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os.path
import sys

if sys.platform.lower().startswith('win'):
    IS_WINDOWS = True
    import win32print
else:
    IS_WINDOWS = False
    import subprocess

class Zebra:
    """A class to communicate with (Zebra) label printers"""

    def __init__(self, queue=None):
        """queue - name of the printer queue (optional)"""
        self.queue = queue

    def _output_unix(self, commands):
        if self.queue == 'zebra_python_unittest':
            p = subprocess.Popen(['cat','-'], stdin=subprocess.PIPE)
        else:
            p = subprocess.Popen(['lpr','-P{}'.format(self.queue),'-oraw'], stdin=subprocess.PIPE)
        p.communicate(commands)
        p.stdin.close()

    def _output_win(self, commands):
        if self.queue == 'zebra_python_unittest':
            print(commands)
            return
        hPrinter = win32print.OpenPrinter(self.queue)
        try:
            hJob = win32print.StartDocPrinter(hPrinter, 1, ('Label',None,'RAW'))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, commands)
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)

    def output(self, commands, encoding='cp437'):
        """Send raw commands to the label printer

        commands - commands to send to the printer.  Converted to a byte string if necessary.
        encoding - Encoding used if 'commands' is not a byte string
        """
        assert self.queue is not None
        if type(commands) != bytes:
            commands = str(commands).encode(encoding=encoding)
        if IS_WINDOWS:
            self._output_win(commands)
        else:
            self._output_unix(commands)

    def print_config_label(self):
        """
        Send an EPL2 command to print label(s) with current config settings
        """
        self.output('\nU\n')

    def _getqueues_unix(self):
        queues = []
        try:
            output = subprocess.check_output(['lpstat','-p'], universal_newlines=True)
        except subprocess.CalledProcessError:
            return []
        for line in output.split('\n'):
            if line.startswith('printer'):
                queues.append(line.split(' ')[1])
        return queues

    def _getqueues_win(self):
        printers = []
        for (a,b,name,d) in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
            printers.append(name)
        return printers

    def getqueues(self):
        """Returns a list of printer queues on local machine"""
        if IS_WINDOWS:
            return self._getqueues_win()
        else:
            return self._getqueues_unix()

    def setqueue(self, queue):
        """Set the printer queue"""
        self.queue = queue

    def setup(self, direct_thermal=None, label_height=None, label_width=None):
        """Set up the label printer using EPL2. Parameters are not set if they are None.
        Not necessary if using AutoSense (hold feed button while powering on)

        direct_thermal - True if using direct thermal labels
        label_height   - tuple (label height, label gap) in dots
        label_width    - in dots
        """
        commands = '\n'
        if direct_thermal:
            commands += 'OD\n'
        if label_height:
           commands += 'Q%s,%s\n'%(label_height[0],label_height[1])
        if label_width:
            commands += 'q%s\n'%label_width
        self.output(commands)

    def reset_default(self):
        """Reset the printer to factory settings using EPL2"""
        self.output('\n^default\n')

    def reset(self):
        """Resets the printer using EPL2 - equivalent to switching off/on"""
        self.output('\n^@\n')

    def autosense(self):
         """Run AutoSense by sending an EPL2 command
         Get the printer to detect label and gap length and set the sensor levels
         """
         self.output('\nxa\n')

    def store_graphic(self, name, filename):
        """Store a 1 bit PCX file on the label printer, using EPL2.

        name     - name to be used on printer
        filename - local filename
        """
        assert filename.lower().endswith('.pcx')
        commands = '\nGK"%s"\n'%name
        commands += 'GK"%s"\n'%name
        size = os.path.getsize(filename)
        commands += 'GM"%s"%s\n'%(name,size)
        self.output(commands)
        self.output(open(filename,'rb').read())

    def print_graphic(self, x, y, width, length, data, qty):
        """Print a label from 1 bit data, using EPL2

        x,y    - top left coordinates of the image, in dots
        width  - width of image, in dots.  Must be a multiple of 8.
        length - length of image, in dots
        data   - raw graphical data, in bytes
        qty    - number of labels to print
        """
        assert type(data) == bytes
        assert width % 8 == 0  # make sure width is a multiple of 8
        assert (width//8) * length == len(data)
        commands = b"\nN\nGW%d,%d,%d,%d,%s\nP%d\n"%(x, y, width//8, length, data, qty)
        self.output(commands)

if __name__ == '__main__':
    z = Zebra()
    print('Printer queues found:',z.getqueues())
    z.setqueue('zebra_python_unittest')
    z.setup(direct_thermal=True, label_height=(406,32), label_width=609)    # 3" x 2" direct thermal label
    z.store_graphic('logo','logo.pcx')
    label = """
N
GG419,40,"logo"
A40,80,0,4,1,1,N,"Tangerine Duck 4.4%"
A40,198,0,3,1,1,N,"Duty paid on 39.9l"
A40,240,0,3,1,1,N,"Gyle: 127     Best Before: 16/09/2011"
A40,320,0,4,1,1,N,"Pump & Truncheon"
P1
"""
    z.output(label)

