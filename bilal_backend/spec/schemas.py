from apiflask import Schema, fields


class LocationSchema(Schema):
    lat = fields.Integer()
    long = fields.Integer()


class CalculationSchema(Schema):
    calculation = fields.String()


class AthanSchema(Schema):
    athan = fields.String()


class SpeakerSchema(Schema):
    name = fields.String()


class VolumeSchema(Schema):
    volume = fields.Integer()
