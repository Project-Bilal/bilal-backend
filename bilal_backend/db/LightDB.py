import os
import json


class LightDB(dict):
    def __init__(self, location: str):
        super().__init__()
        self.location = location
        self.update(**self.load())

    def __repr__(self):
        return object.__repr__(self)

    def load(self):
        resp = {}
        if os.path.exists(self.location):
            file = open(self.location, "r")
            resp = json.load(file)
            file.close()
        return resp

    def save(self):
        file = open(self.location, "w+")
        json.dump(self, file, ensure_ascii=False, indent=4)
        file.close()
        return True

    def set(self, key, value):
        self[key] = value
        return self.save()

    def get(self, key, default=None):
        res = dict(self).get(key, default)
        return res

    def reset(self):
        self.clear()
        return self.save()
