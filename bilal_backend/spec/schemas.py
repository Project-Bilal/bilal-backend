from apiflask import Schema, fields, validators


class LocationSchema(Schema):
    lat = fields.String()
    long = fields.String()
    tz = fields.String()


class CalculationSchema(Schema):
    calculation = fields.String(
        required=True,
        validate=validators.OneOf(["MWL", "ISNA", "Egypt", "Makkah", "Karachi", "Tehran", "Jafari"]),
        metadata={'description': 'The calculation method used for deriving the prayer times.'}
    )


class AthanSchema(Schema):
    athan = fields.String(required=True,
                          metadata={'description': 'id of the athan to be played on the speaker'})


class SpeakerSchema(Schema):
    name = fields.String(required=True,
                         metadata={'description': 'name of the speaker to be used for prayer calls'})
    model = fields.String(required=True,
                         metadata={'description': 'model name of the speaker'})
    cast_type = fields.String(required=True,
                         metadata={'description': 'Group of devices or single device'})
    cast_info = fields.String(required=True,
                         metadata={'description': 'cast_info from device'})


class SpeakersSchema(Schema):
    speakers = fields.List(fields.Nested(SpeakerSchema, required=True))


class VolumeSchema(Schema):
    volume = fields.Integer(required=True,
                            validate=validators.Range(min=0, max=10),
                            metadata={'description': 'Volume of the speaker to be used for prayer calls'})


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
