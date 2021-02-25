from notifications import notifications
from PrinterStatus import PrinterStatus
from IpAddress import IpAddress
from logs import logs
from database import database
import requests

class core():

    def sTART(self):
        query=database()
        final = []
        PrintersIPs = query.findallIPprinter()
        status = PrinterStatus()
        logger = logs()
        for x in PrintersIPs:
            ipAddress = (x[0])
            result = str(status.runStatus(ipAddress))
            if result == "['Printer is offline']":
                resultOffline = query.findprinterstatus(ipAddress)
                if resultOffline == "offline":
                    print("Printer is still offline")
                else:
                    printerLocation = query.findaprinterlocation(ipAddress)
                    data = {
                        'short_description': 'SSP printer need your attention',
                        'details': 'Printer near pole ' + printerLocation + ' with Ip Address' + ipAddress + ' is offline',
                        'category': 'OpsTechIT',
                        'type': 'Client Devices',
                        'item': 'Printers',
                        'impact': '5',
                        'requester_login': 'davsuar',
                        'requester_name': 'David',
                        'assigned_group': 'OpsTechIT-BFL1'
                    }
                    response = requests.post('https://ticket-api.integ.amazon.com/tickets', data=data,
                                             verify=False,
                                             auth=('flx-it-bfl1', 'flx-it-bfl1'))
                    print(response)
                    query.updateprinterstatus(ipAddress,'offline')
            elif result == "['media out']" or result == "['Printer is paused']" or result =="['media out', 'Printer is paused']":
                    printerLocation = query.findaprinterlocation(ipAddress)
                    final.append(
                        "Printer located near pole " + printerLocation + " with Ip Address " + ipAddress + " is facing the next error " + result + "\n")
            else:
                print("printer is working")

        if len(final) != 0:
            multiline_str = ''.join(final)
            notifier = notifications()
            notifier.sendEmail(multiline_str)
        elif len(final) == 0:
            logger.saveEvent("All printers are online \n")

    def checkOffline(self):
        status = PrinterStatus()
        logger = logs()
        query = database()
        result = query.findallprinteroffline()
        if len(result)>0:
            for x in result:
                ipAddress = (x[0])
                s = str(status.runStatus(ipAddress))
                print(s)
                if s == "['Printer is offline']":
                    logger.saveEvent("Printer is still offline" + ipAddress + "\n")
                else:
                    query.updateprinterstatus(ipAddress,'online')
        else:
            print("No print offline")
