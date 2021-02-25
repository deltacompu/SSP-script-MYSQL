class IpAddress():

    # Open function to open the file "MyFile1.txt"
    # (same directory) in append mode and
    filePrinter="Printers.txt"

    def __init__(self):
       print()

    def savePrinterInformation(self,ipAddress, location):
        self.ipAddress = ipAddress
        self.location = location
        self.list1 = self.ipAddress + " " + self.location
        with open(self.filePrinter, 'a') as file:
            file.write(self.list1 + "\n")
            file.close()

    def readPrinterInformation(self):
        with open(self.filePrinter, 'r') as reader:
            return(reader.readlines())


