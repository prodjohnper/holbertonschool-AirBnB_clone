#!/usr/bin/python3
'''
    console.py
    
    Description: Command interpreter entry point
'''
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''
        Command interpreter
    '''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''
            Exit program
        '''
        return True

    def do_EOF(self, arg):
        '''
            Exit program with EOF (Ctrl + D)
        '''
        return True

    def cmdloop(self):
        '''
            Handle EOF
        '''
        try:
            super().cmdloop()
        except KeyboardInterrupt:
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
        args = arg.split()
        if len(args) < 4:
            print("** Usage: update <class name> <id> <attribute name> <attribute value>")
            return

        class_name = args[0]
        obj_id = args[1]
        attr_name = args[2]
        attr_value = " ".join(args[3:])  # Handle attribute value with spaces

        try:
            with open("file.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("** no instance found **")
            return

        key = f"{class_name}.{obj_id}"
        if key not in data:
            print("** no instance found **")
            return

        obj_dict = data[key]
        obj_dict[attr_name] = attr_value  # Update attribute in the dictionary

        with open("file.json", "w") as file:
            json.dump(data, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
