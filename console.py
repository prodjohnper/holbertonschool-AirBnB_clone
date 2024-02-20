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

    def do_show(self, arg):
        '''
            Prints the string representation of an instance
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in BaseModel.__subclasses__():
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
            print(objs[key])

    def do_destroy(self, arg):
        '''
            Deletes an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in BaseModel.__subclasses__():
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
            with open(self.file_path, 'w') as file:
                json.dump(objs, file)

    def do_all(self, arg):
        '''
            Prints all string representation of all instances
        '''
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in BaseModel.__subclasses__()])
            return
        if args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        objs = self.all()
        print([str(obj)
              for obj in objs.values() if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        '''
            Updates an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in BaseModel.__subclasses__():
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
        with open(self.file_path, 'w') as file:
            json.dump(objs, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
