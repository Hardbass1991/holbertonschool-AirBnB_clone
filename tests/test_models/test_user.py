#!/usr/bin/python3
import unittest
from models.user import User
from uuid import uuid4, UUID
from datetime import datetime
from models import storage

def is_valid_uuid(val):
    try:
        UUID(str(val))
        return True
    except ValueError:
        return False

class TestBaseModel(unittest.TestCase):
    kw = {
        "email": "MILFHUNTER69@aol.com",
        "password": "lavaquita",
        "first_name": "Robert",
        "last_name": "Lewandowski"
    }
    tmp = User(**kw)
    tmp.save()

    objs = storage.all()

    def test_attributes(self):
        for i in self.kw.keys():
            self.assertEqual(self.kw[i], self.tmp.__dict__[i])
