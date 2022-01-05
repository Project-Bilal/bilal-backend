from apiflask import Schema, fields, validators


class AthanSchema(Schema):
    name = fields.String(metadata={'description': 'Name of audio file to display to user'})
    length = fields.String(metadata={'description': 'Length of audio file'})
    id = fields.String(metadata={'description': 'ID of audio file to be passed back to settings'})
    type = fields.String(metadata={'description': 'type: fajr, tabir, notifications or dua'})


class AthansSchema(Schema):
    audio_id = fields.Dict(fields.Nested(AthanSchema))


class LocationSchema(Schema):
    lat = fields.Float()
    long = fields.Float()
    address = fields.String()


class CalculationSchema(Schema):
    calculation = fields.String(
        required=True,
        validate=validators.OneOf([
            "MWL",
            "ISNA",
            "Egypt",
            "Makkah",
            "Karachi",
            "Tehran",
            "Jafari",
            "Moon",
            "UAE",
            "Kuwait",
            "Qatar",
            "Singapore",
            'Jakarta',
            'Turkey',
            'France',
            'Russia',
            'Tunisia',
            'Algeria'
        ]),
        metadata={'description': 'The calculation method used for deriving the prayer times.'}
    )


class AudioSchema(Schema):
    audio_id = fields.String(required=True,
                             metadata={'description': 'id of the athan to be played on the speaker'})


class VolumeSchema(Schema):
    volume = fields.Integer(required=True,
                            validate=validators.Range(min=0, max=10),
                            metadata={'description': 'Volume of the speaker to be used for prayer calls'})


class SpeakerSchema(Schema):
    name = fields.String(required=True,
                         metadata={'description': 'name of the speaker to be used for prayer calls'})
    ip = fields.String(required=True,
                       metadata={'description': 'ip address of the speaker'})
    port = fields.Integer(required=True,
                          metadata={'description': 'port of the speaker'})
    uuid = fields.String(required=True,
                         metadata={'description': 'uuid string of the speaker'})
    model = fields.String(required=True,
                          metadata={'description': 'model name of the speaker'})
    cast_type = fields.String(required=False,
                              metadata={'description': 'Group of devices or single device'})


class SpeakersSchema(Schema):
    speakers = fields.List(fields.Nested(SpeakerSchema, required=True))


class PlaySchema(Schema):
    audio_id = fields.String(required=True)
    audio_title = fields.String(required=False)


class TestSoundSchema(Schema):
    audio_id = fields.String(required=True)
    speaker = fields.Nested(SpeakerSchema, required=True)


class PlayedSchema(Schema):
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


class MethodParams(Schema):
    fajr = fields.String()
    maghrib = fields.String()
    isha = fields.String()
    midnight = fields.String()


class MethodsSchema(Schema):
    name = fields.String()
    params = fields.Dict(fields.Nested(MethodParams))


class CalculationsSchema(Schema):
    calculations = fields.Dict()
