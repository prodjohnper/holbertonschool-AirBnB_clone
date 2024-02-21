#!/usr/bin/python3
"""
    class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
"""


import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self): #Returns all stored objects.
        return FileStorage.__objects

    def new(self, obj): #Adds a new object to the internal dictionary of objects.
        name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[name] = obj.to_dict()

    def save(self): #Saves the current state of objects to the JSON file.
        with open(self.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self): #Reloads objects from the JSON file.
        try:
            with open(self.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
