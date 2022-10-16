#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self):
        super().save()
        d = self.__dict__
        ds = storage.all()
        ds[self.__class__.__name__ + "." + self.id].__dict__.update(d)
        storage.save()
