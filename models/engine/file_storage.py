#!/usr/bin/python3
import json
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj["__class__"] + "." + obj["id"]] = obj
    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as f:
            # print(self.__objects)
            f.write(json.dumps(self.__objects, default=str))

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                if f:
                    #print("a" + f.read() + "a")
                    self.__objects.update(json.load(f))
