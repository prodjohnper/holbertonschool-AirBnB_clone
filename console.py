#!/usr/bin/python3
'''
    console.py
    
    Description: Command interpreter entry point
'''
import cmd
import json
import shlex
from models.user import User


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
            Creates a new instance of User
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name != "User":
            print("** class doesn't exist **")
            return

        new_user = User()
        new_user.save()
        print(new_user.id)

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
            Prints the string representation of a User instance
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "User":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        user_id = args[1]
        objs = self.all()
        key = class_name + "." + user_id
        if key not in objs:
            print("** no instance found **")
            return

        print(objs[key])

    def do_destroy(self, arg):
        '''
            Deletes a User instance based on the id
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "User":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        user_id = args[1]
        objs = self.all()
        key = class_name + "." + user_id
        if key not in objs:
            print("** no instance found **")
            return

        del objs[key]
        with open('file.json', 'w') as file:
            json.dump(objs, file)

    def do_all(self, arg):
        '''
            Prints all string representations of User instances
        '''
        if not arg:  # If no argument provided, print all instances
            with open('file.json', 'r') as file:
                objs_dict = json.load(file)
                for key, dictionary in objs_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        obj = User(**dictionary)
                        print(obj)
        else:
            args = arg.split()
            if len(args) == 1:
                class_name = args[0]
                if class_name == "User":
                    with open('file.json', 'r') as file:
                        objs_dict = json.load(file)
                        for key, dictionary in objs_dict.items():
                            if key.startswith(class_name):
                                obj_id = key.split('.')[1]
                                obj = User(**dictionary)
                                print(obj)
                else:
                    print("** class doesn't exist **")

    def do_update(self, arg):
        args = shlex.split(arg)
        args = args[:4]  # Ensure only first 4 arguments are used

        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]

        if class_name != 'User':
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print('** instance id missing **')
            return
        obj_id = args[1]

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

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]

        if len(args) < 4:
            print('** value missing **')
            return

        attr_value = " ".join(args[3:])  # Handle attribute value with spaces
        obj_dict = data[key]
        obj_dict[attr_name] = attr_value  # Update attribute in the dictionary

        with open("file.json", "w") as file:
            json.dump(data, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
