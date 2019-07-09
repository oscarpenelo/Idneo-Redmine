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
parser.add_argument('-u', "--user", type=str, help="username")
parser.add_argument('-p', "--password", type=str, help="password")
parser.add_argument('-i', "--issueid", type=int, help="issueid")
parser.add_argument('-m', "--month", type=int, help="month")
parser.add_argument('-y', "--year", type=int, help="year")
parser.add_argument('-e', "--exclude", type=str,
                    help="Define a list of days separated by comma. Ex: \"01,02,20\"")


parser.add_argument('-d', action='store_true', help="daemon", default=argparse.SUPPRESS)

args = parser.parse_args()

redmine = Redmine('https://idneo.easyredmine.com', username=args.u, password=args.p)


def track_today():
    d = datetime.datetime.now()
    if (d.weekday() >= 0) and (d.weekday() <= 4):
        print("TRACKING " + str(d.day) + "/" + str(d.month) + "/" + str(d.year))
        try:
            time_entry = redmine.time_entry.create(issue_id=args.i, spent_on=d, hours=8)
        except Exception as e:
            print('**Track error: ' + str(e))


def run_threaded(job_fn):
    job_thread = threading.Thread(target=job_fn)
    job_thread.start()


def excluding_days(exclude_argument):
    exclude_arg = exclude_argument
    exclude_int_arg = list(map(int, exclude_arg.split(",")))
    return exclude_int_arg


if 'd' in args:
    schedule.every().day.at("15:00").do(run_threaded, track_today)

    while True:
        schedule.run_pending()
        time.sleep(1)

else:
    d = datetime.date(args.y, args.m, 1)

    exclude_int_arg = excluding_days(args.exclude)

    while d.month == args.m:
        if (d.weekday() >= 0) and (d.weekday() <= 4):
            if int(d.day) not in exclude_int_arg:
                print("TRACKING " + str(d.day) + "/" + str(d.month) + "/" + str(d.year))
                try:
                    time_entry = redmine.time_entry.create(issue_id=args.i, spent_on=d, hours=8)
                except Exception as e:
                    print('**Track error: ' + str(e))
            else:
                print("day " + str(d.day) + " was excluded")
        d += datetime.timedelta(days=1)
