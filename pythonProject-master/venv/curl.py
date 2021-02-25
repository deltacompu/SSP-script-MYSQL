import requests

data = {
  'short_description': 'SSP printer need your attention',
  'details': 'Printer located near pole 1T09 with Ip Address 10.243.240.126 is having the next error [\'media out\', \' Printer is paused \']',
  'category': 'OpsTechIT',
  'type': 'Client Devices',
  'item': 'Printers',
  'impact': '5',
  'requester_login': 'davsuar',
  'requester_name': 'David',
  'assigned_group': 'OpsTechIT-BFL1'
}

response = requests.post('https://ticket-api.integ.amazon.com/tickets', data=data, verify=False, auth=('flx-it-bfl1', 'flx-it-bfl1'))
print (response)