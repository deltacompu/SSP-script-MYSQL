import time
import subprocess
from datetime import datetime
from core import core
process = None
firstShift = True
secondShift = False
thirdShift = False
firstShiftTest = True
secondShiftTest = False
thirdShiftTest = False
start = core()
while True:
    now = datetime.now()
    print(now)
    current_time = now.strftime("%H:%M")
    time.sleep(10)
    if current_time == "21:40" and firstShiftTest:
        print('Running script offline printer')
        start.checkOffline()
        firstShiftTest = False
        secondShiftTest = True
    elif current_time == "21:45" and firstShift:
        print('Running script first shift')
        start.sTART()
        firstShift = False
        secondShift = True
    elif current_time == "21:55" and secondShiftTest:
        print('Running script offline printer')
        start.checkOffline()
        secondShiftTest = False
        thirdShiftTest = True
    elif current_time == "21:58" and secondShift:
        print('Running script second shift 2')
        start.sTART()
        secondShift = False
        thirdShift = True
    elif current_time == "22:15" and thirdShiftTest:
        print('Running script offline printer')
        start.checkOffline()
        thirdShiftTest = False
        firstShiftTest = True
    elif current_time == "22:25" and thirdShift:
        print('Running script third shift 3')
        start.sTART()
        thirdShift = False
        firstShift = True


