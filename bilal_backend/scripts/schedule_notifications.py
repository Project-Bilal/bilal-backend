from crontab import CronTab
from bilal_backend.libs.pt_handler import prayer_times_handler
from bilal_backend.utils.utils import db_context
import getpass
from datetime import datetime, timedelta


# get the prayer times from pt_handler
@db_context
def get_pt(data):
    loc = data.get("location", {})
    calc = data.get("calculation", {})
    method = calc.get("method", {})
    jur = calc.get("jurisprudence", "Standard")
    if not loc or not method:
        del_notifications()
        print("###ERROR### 'location' or 'method' empty or missing in data.json")
        return None
    else:
        lat = loc.get("lat", None)
        long = loc.get("long", None)
        tz = loc.get("tz", None)
        if not lat or not long or not tz:
            del_notifications()
            print("###ERROR### 'lat', 'long', or 'tz' empty or missing in data.json")
            return None
        return prayer_times_handler(
            lat=lat, long=long, tz=tz, calc=method, jur=jur, format="24h"
        )


# convert the time the pt_handler gives us to hours and minutes to use with cron
# return a list of dicts with the information needed to schedule cronjobs
@db_context
def get_cron_times(data, athan_times):
    data = data.get("athans", {})
    if not data:
        del_notifications()
        print("###ERROR### 'athans' data object empty or missing in data.json")
        return None
    notifications = []
    for prayer in data:
        prayer_info = data.get(prayer, {})
        if prayer_info:
            volume = prayer_info.get("volume", {})
            if volume:
                if prayer_info.get("athan_on", {}):
                    audio_id = prayer_info.get("audio_id", {})
                    if audio_id:
                        notifications.append(
                            {
                                "hour": int(athan_times[prayer].split(":")[0]),
                                "min": int(athan_times[prayer].split(":")[1]),
                                "audio_id": audio_id,
                                "vol": volume,
                            }
                        )
                if prayer_info.get("notification_on", {}):
                    audio_id = prayer_info.get("notification_id", {})
                    if audio_id:
                        offset = prayer_info.get("notification_time", {})
                        if offset:
                            delta = timedelta(minutes=offset)
                            hour = int(athan_times[prayer].split(":")[0])
                            min = int(athan_times[prayer].split(":")[1])
                            play_time = (
                                datetime.now().replace(hour=hour, minute=min) - delta
                            )
                            notifications.append(
                                {
                                    "hour": play_time.hour,
                                    "min": play_time.minute,
                                    "audio_id": audio_id,
                                    "vol": volume,
                                }
                            )
    return notifications


# delete existing crontab jobs
def del_notifications():
    user = getpass.getuser()
    with CronTab(user=user) as cron:
        cron.remove_all(comment="notification")

# schedule new notification times and remove existing ones
def add_notifications(notifications):
    user = getpass.getuser()
    del_notifications()
    with CronTab(user=user) as cron:
        for notification in notifications:
            audio_id = notification["audio_id"]
            vol = notification["vol"]
            job = cron.new(
                command=f"curl -X GET http://localhost:5002/speakers/play/{audio_id}/{vol} > /dev/null 2>&1 # notification"
            )
            job.hour.on(notification["hour"])
            job.minute.on(notification["min"])
    return "###SUCCESS### Added notification cron jobs succcessfully"


# schedule the notification scheduler that runs at 1 AM local time daily
def add_notification_scheduler():
    user = getpass.getuser()
    with CronTab(user=user) as cron:
        cron.remove_all(comment="bilal_scheduler")
        job = cron.new(
            command=f"curl -X GET http://localhost:5002/athans/schedule > /dev/null 2>&1 # bilal_scheduler"
        )
        job.hour.on(1)
        job.minute.on(0)
    return "###SUCCESS### Added notificaton scheduler successfully"


def sched_notifications():
    athan_times = get_pt()
    if not athan_times:
        del_notifications()
        return "###ERROR### get_pt is missing information. Will not schedule cron jobs."
    notifications = get_cron_times(athan_times)
    if not notifications:
        del_notifications()
        return "###ERROR### Missing or empty information in data.json for the `athans` object"
    return add_notifications(notifications)
