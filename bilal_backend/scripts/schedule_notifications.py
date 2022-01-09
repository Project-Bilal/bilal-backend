from crontab import CronTab
from bilal_backend.libs.pt_handler import prayer_times_handler
from bilal_backend.utils.utils import db_context
import getpass
import os
from datetime import datetime, timedelta


# get the prayer times from pt_handler
@db_context
def get_pt(data):
    loc = data.get("location", {})
    calc = data.get("calculation", {})
    method = calc.get("method", {})
    jur = calc.get("jurisprudence", None)
    if not loc or not method:
        return None
    else:
        lat = loc["lat"]
        long = loc["long"]
        tz = loc["tz"]
        return prayer_times_handler(
            lat=lat, long=long, tz=tz, calc=method, jur=jur, format="24h"
        )


# convert the time the pt_handler gives us to hours and minutes to use with cron
# return a list of dicts with the information needed to schedule cronjobs
@db_context
def get_cron_times(data, athan_times):
    data = data.get("athan", {})
    if not data:
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
                                "athan": prayer,
                                "type": "athan",
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
                                    "athan": prayer,
                                    "type": "notification",
                                    "hour": play_time.hour,
                                    "min": play_time.minute,
                                    "audio_id": audio_id,
                                    "vol": volume,
                                }
                            )
    return notifications


def add_notification_scheduler():
    pwd = os.getcwd()
    user = getpass.getuser()
    with CronTab(user=user) as cron:
        cron.remove_all(comment="bilal_scheduler")
        job = cron.new(
            command=f"curl -X GET http://localhost:5002/athans/schedule > /dev/null 2>&1 # bilal_scheduler"
        )
        job.hour.on(1)
        job.minute.on(0)


# schedule new notification times and remove existing ones
def add_notifications(notifications):
    user = getpass.getuser()
    with CronTab(user=user) as cron:
        cron.remove_all(comment="notification")
        for notification in notifications:
            athan = notification["athan"]
            type = notification["type"]
            audio_id = notification["audio_id"]
            vol = notification["vol"]
            job = cron.new(
                command=f"curl -X GET http://localhost:5002/speakers/play/{athan}/{type}/{audio_id}/{vol} > /dev/null 2>&1 # notification"
            )
            job.hour.on(notification["hour"])
            job.minute.on(notification["min"])
    return None


def sched_notifications():
    athan_times = get_pt()
    if not athan_times:
        return None
    notifications = get_cron_times(athan_times)
    if not notifications:
        return None
    add_notifications(notifications)
    return "Success"
