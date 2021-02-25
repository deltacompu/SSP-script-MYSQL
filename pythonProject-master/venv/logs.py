import time
import re
from datetime import datetime
class logs():

    filePrinter = "logs.txt"
    offline = "offlinePrinter.txt"



    def saveEvent(self, message):
        self.message = message
        now = datetime.now()
        current_time = now.strftime("%D %H:%M")
        with open(self.filePrinter, 'a') as file:
            file.write(current_time+ " "+self.message)
            file.close()

    def offlinePrinter(self, message):
        self.message = message
        with open(self.offline, 'a') as file:
            file.write(self.message+"\n")
            file.close()

    def checkOffline(self):
        list=[]
        with open("offlinePrinter.txt", 'r') as f:
            for linea in f:
                list.append(linea)
            return list

    def deleteOffline(self, ip):
        with open("offlinePrinter.txt", "r") as f:
            lines = f.readlines()
        with open("offlinePrinter.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != ip:
                    f.write(line)



    def find_string(self, ip):
        self.ip = ip
        with open(self.offline, 'r') as a:
            for line in a:
                line = line.rstrip()
                if re.search(r"\b{}\b".format(self.ip), line):

                    return True

        return False

    def delete_blankline(self):
        with open("offlinePrinter.txt", 'r') as f:
            data = f.read()
            with open("offlinePrinter.txt", 'w') as w:
                w.write(data[:-1])



