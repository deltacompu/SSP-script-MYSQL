import serial;
import json;

class Printer:
    def __init__(self,port="com1",baudrate=9600,bytesize=8,stopbits=1,parity='N'):
        self.port = port
        self.baudrate=9600
        self.bytesize=bytesize
        self.stopbits=stopbits
        self.parity=parity

    def initTemplate(self,template):
        ser = serial.Serial(port=self.port,baudrate=self.baudrate,
                            bytesize=self.bytesize,parity=self.parity,
                            stopbits=self.stopbits)
        ser.write(template.encode())
        print template
        ser.close()

    def printLableWithTemplate(self,template_name="",fn_fields="",params={}):
        str = '^XA\n^XFR:'+template_name+".GRF\n"
        field_map = json.loads(fn_fields)
        for (k,v) in field_map.items():
            print k + ' = '+v
            if (v == 'QR Code'):
              str += '^'+k+'^FD  '+json.dumps(params)+'^FS\n'
            else:
              str += '^'+k+'^FD'+params[v]+'^FS\n'
        str += '^XZ'
        print "----------------------\n"
        print str
        print "----------------------\n"
        ser = serial.Serial(port=self.port, baudrate=self.baudrate,
                            bytesize=self.bytesize, parity=self.parity,
                            stopbits=self.stopbits)
        ser.write(str.encode())
        ser.close()

    def printLable(self,zpl_content=""):
        ser = serial.Serial(port=self.port, baudrate=self.baudrate,
                            bytesize=self.bytesize, parity=self.parity,
                            stopbits=self.stopbits)
        ser.write(zpl_content.encode())
        ser.close()

if __name__ == '__main__':

    str = '{"FN1":"sn","FN2":"mac","FN3":"QR Code"}'
    params={}
    params["sn"]="A001"
    params["mac"]="18:05:03:11:22:33"
    template_name="IR915L.GPR"
    template ='^XA\n^DFR:'+template_name+'^FS\n' \
                                           '^FO50,50^ADN36,10^FDSN: ^FS\n' \
                                           '^FO50,100^ADN36,10^FDMAC:^FS\n' \
                                           '^FO100,50^ADN36,10^FN1^FS\n' \
                                           '^FO100,100^ADN36,10^FN2^FS\n' \
                                           '^FO50,150^AD72,20^FN3^FS\n' \
                                           '^FO50,180^BQN2,3^FN3^FS\n^XZ\n'
    #step 1: open com
    p = Printer(port="com1")
    #step 2: init the template, send it to the printer
    p.initTemplate(template)
    #step 3: print the label.
    p.printLableWithTemplate(template_name=template_name,fn_fields=str,params=params)

"""
^XA
^DFR:ECOER915.GRF^FS
^FO60,35
^GB1028,686,6,,2^FS
^FO60,160
^GB1028,480,6^FS
^FO280,60
^ADN,90, 24^FDEcoer Smart IoT Gateway^FS
^FO600,220
^ADN,18,10^FDContains FCCID:^FS
^FO800,220
^ADN,18,10^FN0^FS
^FO100,240
^ADN,36,20^FDModle:^FS
^FO270,240
^ADN,36,20^FN1^FS
^FO100,300
^ADN,36,20^FDP/N:^FS
^FO270,300
^ADN,36,20^FN2^FS
^FO100,360
^ADN,36,20^FDS/N:^FS
^FO270,360
^ADN,36,20^FN3^FS
^FO100,420
^ADN,36,20^FDIMEI:^FS
^FO270,420
^ADN,36,20^FN4^FS
^FO100,480
^ADN,36,20^FDICCID:^FS
^FO270,480
^ADN,36,20^FN5^FS
^FO100,650
^ADN,30,20^FDDate:^FS
^FO270,650
^ADN,30,20^FN10^FS
^FO780,280
^BQN,2,10^FN20^FS
^XZ

^XA
^XFR:ECOER915.GRF
^FN20^FD  {"mac": "18:05:03:11:22:33", "sn": "A001"}^FS
^FN10^FD07.2017^FS
^FN0^FDQIPELS61-US^FS
^FN1^FDEG910L^FS
^FN2^FDFS71-S-ESIM^FS
^FN3^FDEG9101721012345^FS
^FN4^FD89011703278101364837^FS
^FN5^FD3278101364837^FS
^XZ
"""