__author__ = "Oscar Penelo"
__copyright__ = "Copyright (C) 2018 Oscar Penelo"
__license__ = "gplv3.0"
__version__ = "1.0"

from redminelib import Redmine
import argparse
import datetime
import schedule
import threading
import time
print('IDNEO REMDINE SCHEDULER - BY OSCAR PENELO')
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-i', type=int, help="issueid")
parser.add_argument('-m', type=int, help="month")
parser.add_argument('-y', type=int, help="year")

parser.add_argument('-d',  action='store_true', help="daemon")

args = parser.parse_args()

redmine = Redmine('https://idneo.easyredmine.com', username=args.u, password=args.p)
def track_today(): 
    d=datetime.datetime.now()
    if (d.weekday() >= 0) and (d.weekday()<=4):
        print("TRACKING " + str(d.day) + "/" + str(d.month) +"/" + str(d.year))
        try:
            time_entry= redmine.time_entry.create(issue_id=args.i,spent_on=d,hours=8)
        except Exception as e:
            print('**Track error: '+ str(e))

def run_threaded(job_fn):
    job_thread = threading.Thread(target=job_fn)
    job_thread.start()

if args.d is not None:
    schedule.every().day.at("15:30").do(run_threaded, track_today)

    while True:
        schedule.run_pending()
        time.sleep(1)


else:


    d=datetime.date(args.y,args.m,1)
    while d.month == args.m:
        if (d.weekday() >= 0) and (d.weekday()<=4):
            print("TRACKING " + str(d.day) + "/" + str(d.month) +"/" + str(d.year))
            try:
                time_entry= redmine.time_entry.create(issue_id=args.i,spent_on=d,hours=8)
            except Exception as e:
                print('**Track error: '+ str(e))
        d += datetime.timedelta(days=1)

