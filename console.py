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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
