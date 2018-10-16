import timeit
from datetime import date,timedelta
import datetime
import sys
def getWorkDay(delt=None):
    if str(delt).isdigit():
        if delt == None:
            workday = datetime.date.today()
            if workday.weekday()==0:
                workday = workday - timedelta(3)
            else:
                workday = workday - timedelta(1)
            return workday
        else:
            workday = datetime.date.today()
            return workday - timedelta(int(delt))
    else:
        sys.exit("Please imput number (timedelta)")
