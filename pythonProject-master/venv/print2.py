import socket
import logging
import time


TCP_IP = '10.243.243.100'
TCP_PORT=5964
BUFFER_SIZE = 1024
TCP_IPs = ['10.243.240.100',
'10.243.240.109',
'10.243.240.114',
'10.243.240.111',
'10.243.240.150',


'10.243.240.167',
'10.243.240.164',
'10.243.240.23',
'10.243.240.192',
'10.243.240.101',
'10.243.240.24',
'10.243.240.18',
'10.243.240.130',
'10.243.240.159',

'10.243.240.128',
'10.243.240.126',
'10.243.240.42',
'10.243.240.182',
'10.243.240.97',
'10.243.240.102',
'10.243.240.149',
'10.243.240.10',
'10.243.240.187',
'10.243.240.168',
'10.243.240.55',
'10.243.240.86',
'10.243.240.209',
'10.243.240.118',
'10.243.240.184',
'10.243.240.138',
'10.243.240.103',
'10.243.240.175',
'10.243.240.157',

'10.243.240.11',
'10.243.240.173',

'10.243.240.104',
'10.243.240.105',
'10.243.240.106',
'10.243.240.107',
'10.243.240.108']
start_time = time.time()

seconds = 60

#this will print a code 128 barcode
zpl = """
^XA
^FO150,40^BY3
^BCN,110,Y,N,N
^FD123456^FS
^XZ 
"""

zpltest ="""
~HS
"""
while True:
    for x in TCP_IPs:
        current_time = time.time()
        elapsed_time = current_time - start_time
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.debug("Connect")
        try:
            s.connect((x, TCP_PORT))
            print(s.getpeername())
        except socket.error as e:
            print(e)
            logging.error("!!! Socket Connect FAILED: %s" % e)
        print("Printer is online")
        # s.send(bytes(zpl, "utf-8"))
        s.send(bytes(zpltest, "utf-8"))
        dataFromServer = s.recv(1024)
        ab = dataFromServer.decode()
        cd = ab.split(",")
        if int(cd[1]) == 0:
            print("Media ok")
        else:
            print("Media out")
        if int(cd[2]) == 0:
            print("Printer is not paused")
        else:
            print("Printer is paused")
        s.close()
    time.sleep(60)
    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        break
