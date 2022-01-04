from crontab import CronTab
from bilal_backend.libs.pt_handler import prayer_times_handler
from bilal_backend.utils.utils import db_context
import getpass
import sys

'''Needs crontab job like so: @daily pipenv shell python3 /path/to/schedule_athans.py sched > /dev/null 2>&1'''

# get the prayer times from pt_handler
@db_context
def get_pt(data):
    loc = data.get("location")
    lat = loc["lat"]
    long = loc["long"]
    tz = loc["tz"]
    return prayer_times_handler(lat=lat, long=long, tz=tz, calc=data.get("calculation"), format='24h')

# convert the time the pt_handler gives us to hours and minutes to use with cron
def get_cron_times(data):
    """These prayers will be scheduled"""
    prayers = [
        'fajr',
        'dhuhr',
        'asr',
        'maghrib',
        'isha',
        #'imsak',
        #'sunrise',
        #'midnight,
        # All the above is available via the API
        # if you add or remove please update the crontab file as well
    ]

    athan_cron = {}
    for prayer in prayers:
        athan_cron[prayer] = {'hour' : int(athan_times[prayer].split(':')[0]), 'min' : int(athan_times[prayer].split(':')[1])}
    return athan_cron

# delete existing scheduled prayers
def remove_jobs():
    user = getpass.getuser()
    cron = CronTab(user=user)
    for job in cron:
        if 'athan' in job.comment:
            cron.remove(job)
            cron.write()

# schedule new prayer times
def schedule_jobs():
    user = getpass.getuser()
    cron = CronTab(user=user)
    for prayer, timing in athan_cron.items():
        # TODO update the command to call the end point to play
        # TODO use the db to get the athan id like so data.get("fajr_athan")["audio_id"]
        job = cron.new(command=f'play_athan.sh > /dev/null 2>&1 # athan_{prayer}')
        job.hour.on(timing['hour'])
        job.minute.on(timing['min'])
        cron.write()


# when run as main check the arguments and either schedule or push
if __name__ == '__main__':
    if sys.argv[1] == 'sched':
        athan_times = get_pt()
        athan_cron = get_cron_times(athan_times)
        remove_jobs()
        schedule_jobs()
