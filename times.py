import     time
from datetime import datetime
import     win32com.client

wmi = win32com.client.GetObject('winmgmts:')

start=datetime.now()

file_name = 1
while 1:
    try:
        f=open('%s.txt'%file_name)
        file_name+=1
    except IOError:
        f=file('%s.txt'%file_name,'w')
        f.close()
        break

def log():
    logs = file('%s.txt' % file_name, 'a')
    BatteryPercentage = wmi.InstancesOf('win32_battery')
    percentage = BatteryPercentage[0].EstimatedChargeRemaining
    passed_time = datetime.now() - start
    passed_time = passed_time.seconds
    string = '%s:%s - %s \n' % (passed_time / 60, passed_time % 60, percentage)
    print string
    logs.write(string)
    logs.close()
    time.sleep(15)
    log()

log()
