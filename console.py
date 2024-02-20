#!/usr/bin/python3
'''
    console.py
    
    Description: Command interpreter entry point
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
        Command interpreter
    '''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''
            Exit program
        '''
        quit()

    def do_EOF(self, arg):
        '''
            Exit program with EOF (Ctrl + D)
        '''
        return True

    def emptyline(self):
        '''
            Do nothing (Empty line + Enter)
        '''
        pass

    def cmdloop(self):
        try:
            super().cmdloop()
        except KeyboardInterrupt:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
