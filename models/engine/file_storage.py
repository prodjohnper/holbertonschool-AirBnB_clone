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
        return self.__objects

    def new(self, obj): #Adds a new object to the internal dictionary of objects.
        name = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[name] = obj.to_dict()

    def save(self): #Saves the current state of objects to the JSON file.
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self): #Reloads objects from the JSON file.
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
