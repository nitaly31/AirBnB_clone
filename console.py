#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNB Class
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True

    def emptyline(self):
        """ Overwriting the emptyline method """
        return False

    def do_quit(self, line):
        """Quit command exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
