from apiflask import Schema, fields, validators


class LocationSchema(Schema):
    lat = fields.String()
    long = fields.String()


class CalculationSchema(Schema):
    calculation = fields.String(
        validate=validators.OneOf(["MWL", "ISNA", "Egypt", "Makkah", "Karachi", "Tehran", "Jafari"])
    )


class AthanSchema(Schema):
    athan = fields.String()


class SpeakerSchema(Schema):
    name = fields.String()


class VolumeSchema(Schema):
    volume = fields.Integer()


class PlaySound(Schema):
    audio_id = fields.String(required=True)
    speaker_name = fields.String(required=True)


class SoundPlayed(Schema):
    message = fields.String()


class PrayerTimesSchemas(Schema):
    asr = fields.String()
    dhuhr = fields.String()
    fajr = fields.String()
    imsak = fields.String()
    isha = fields.String()
    maghrib = fields.String()
    midnight = fields.String()
    sunrise = fields.String()
    sunset = fields.String()
