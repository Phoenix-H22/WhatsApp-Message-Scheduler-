import pyautogui as pg
import time
import logging
import pywhatkit 
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
log = logging.getLogger('apscheduler.executors.default')


def sender():
    x=datetime.today()
    h=x.hour
    m=x.minute +1
    pywhatkit.sendwhatmsg("+201069683986","This is a message",h,m)
    print ("Message sent on", h,":",m)

def enter():
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')    

scheduler = BlockingScheduler()
scheduler.add_job(sender, 'interval', seconds=20)
scheduler.start()
