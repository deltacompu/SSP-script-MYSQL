import socket
import logging
import time
from logs import logs

class PrinterStatus():
    TCP_PORT = 5964
    BUFFER_SIZE = 1024
    zplCommand = """
    ~HS
    """

    def __init__(self):
        self.TCP_PORT = 5964
        self.BUFFER_SIZE = 1024
        self.zplCommand = """
            ~HS
            """
        self.register=logs()

    def runStatus(self,IpAddress):
        a = []
        self.IpAddress = str(IpAddress)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        logging.debug("Connect")
        log=""
        try:
            s.connect((self.IpAddress, self.TCP_PORT))
            if s:
                str(s.getpeername())
                s.send(bytes(self.zplCommand, "utf-8"))
                dataFromServer = s.recv(1024)
                ab = dataFromServer.decode()
                cd = ab.split(",")
                if int(cd[1]) == 0:
                    print("media ok")
                else:
                    a.append("media out")
                    log += str(s.getpeername())+" Printer is online media out "
                if int(cd[2]) == 0:
                    print("Printer is not paused")
                else:
                    a.append("Printer is paused")
                    log += "Printer is paused \n"
                s.close()
                if (len(log)!=0):
                    self.register.saveEvent(log)
            else:
                a.append("Printer is offline")
                s.close()
            return a
        except socket.timeout:
            a.append("Printer is offline")
            self.register.saveEvent(self.IpAddress+ " Printer offline \n")
            print("Printer is offline")
            return a
            s.close()
