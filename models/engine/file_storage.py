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
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self): #Saves the current state of objects to the JSON file.
        with open(FileStorage.__file_path, "w") as file:
            new_dict = {k: obj.to_dict() for k, obj in FileStorage.__objects.items()}
            json.dump(new_dict, file)

    def reload(self): #Reloads objects from the JSON file.
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls = BaseModel
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
