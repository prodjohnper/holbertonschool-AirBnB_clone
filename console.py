#!/usr/bin/python3
'''
    console.py
    
    Description: Command interpreter entry point
'''
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    '''
        Command interpreter
    '''
    prompt = '(hbnb) '

    def __init__(self):
        '''
            comment
        '''
        super().__init__()
        self._HBNBCommand = FileStorage()

    def do_quit(self, arg):
        '''
            Exit program
        '''
        return True

    def do_EOF(self, arg):
        '''
            Exit program with EOF (Ctrl + D)
        '''
        print()
        return True

    def cmdloop(self):
        '''
            Handle EOF
        '''
        try:
            super().cmdloop()
        except KeyboardInterrupt:
            print()
            return True

    def emptyline(self):
        '''
            Do nothing (Empty line + Enter)
        '''
        pass

    def do_create(self, arg):
        '''
            Creates a new instance of BaseModel
        '''
        if arg == '':
            print("** class name missing **")
            return

        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def all(self):
        '''
            Returns the dictionary representation of all objects
        '''
        objs_dict = {}
        try:
            with open('file.json', 'r') as file:
                objs_dict = json.load(file)
        except FileNotFoundError:
            pass
        return objs_dict

    def do_show(self, arg):
        '''
            Prints the string representation of an instance
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        # Load data from JSON file
        try:
            with open("file.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return

        key = args[0] + "." + args[1]
        if key not in data:
            print("** no instance found **")
        else:
            instance_dict = data[key]
            instance = BaseModel(**instance_dict)
            print(instance)

    def do_destroy(self, arg):
        '''
            Deletes an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objs = self.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            del objs[key]
            with open('file.json', 'w') as file:
                json.dump(objs, file)

    def do_all(self, arg):
        '''
            Prints all string representation of all instances
        '''
        args = arg.split()
        if len(args) == 1 and args[0] == 'BaseModel':
            with open('file.json', 'r') as file:
                my_dict_from_json = json.load(file)
                for key, dictionary in my_dict_from_json.items():
                    obj = BaseModel(**dictionary)
                    print(obj)
        else:
            print("** class doesn't exist **")
        """ objs = self.all() """

    def do_update(self, arg):
        '''
            Updates an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        objs = self.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        obj = objs[key]
        setattr(obj, args[2], args[3])
        with open('file.json', 'w') as file:
            json.dump(objs, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
