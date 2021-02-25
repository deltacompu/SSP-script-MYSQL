from IpAddress import IpAddress

newPrinter=True
while (newPrinter):
    ipAddress = input("Type the ip address ")
    ipLocation = input("Type the printer Location ")
    response = input("Do you wan to add more printers Y or N ")
    if response=="Y":
        newPrinter=True
    elif response == "y":
            newPrinter = True
    else:
        newPrinter=False

store = IpAddress(ipAddress, ipLocation)
store.save()

# Note that in version 3, the print() function
# requires the use of parenthesis.

