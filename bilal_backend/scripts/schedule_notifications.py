from crontab import CronTab
from bilal_backend.libs.pt_handler import prayer_times_handler
from bilal_backend.utils.utils import db_context
from bilal_backend.libs.constants import PrayerNames
import getpass
import os

'''Needs crontab job like so: 0 1 * * * pipenv shell python3 /path/to/schedule_athans.py > /dev/null 2>&1'''

# get the prayer times from pt_handler
@db_context
def get_pt(data):
    loc = data.get("location")
    calc = data.get("calculation")
    if not loc:
        return None
    if not calc:
        return None
    else:
        lat = loc["lat"]
        long = loc["long"]
        tz = loc["tz"]
        return prayer_times_handler(lat=lat, long=long, tz=tz, calc=calc, format='24h')


# convert the time the pt_handler gives us to hours and minutes to use with cron
# return a list of dicts with the information needed to schedule cronjobs
def get_cron_times(athan_times):
    """These prayers will be scheduled"""
    prayers = [
        PrayerNames.FAJR,
        PrayerNames.DHUHR,
        PrayerNames.ASR,
        PrayerNames.MAGHRIB,
        PrayerNames.ISHA
    ]

    notifications = []
    for prayer in prayers:
        notifications.append(
            {
                'name': prayer,
                'hour':  int(athan_times[prayer].split(':')[0]),
                'min': int(athan_times[prayer].split(':')[1]),
            }
        )
    return notifications


def add_notification_scheduler():
    pwd = os.getcwd()
    user = getpass.getuser()
    with CronTab(user=user) as cron:
        cron.remove_all(comment='bilal_scheduler')
        job = cron.new(command=f'curl -X GET http://localhost:5002/athans/schedule > /dev/null 2>&1 # bilal_scheduler')
        job.hour.on(1)
        job.minute.on(0)


# schedule new notification times and remove existing ones
def add_notifications(notifications):
    user = getpass.getuser()
    with CronTab(user=user) as cron:
        cron.remove_all(comment='notification')    
        for notification in notifications:
            name = notification['name']
            job = cron.new(command=f'curl -X GET http://localhost:5002/speakers/play/notification/{name} > /dev/null 2>&1 # notification')
            job.hour.on(notification['hour'])
            job.minute.on(notification['min'])
    return None


def sched_notifications():
    athan_times = get_pt()
    if not athan_times:
        return None
    notifications = get_cron_times(athan_times)
    add_notifications(notifications)
    return "Success"