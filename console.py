#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd
import models
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex

classGroup = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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

    def do_create(self, line):
        """Creates a new BaseModel instance, saves it to the JSON file and prints the id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        try:
            string = line + "()"
            instance = eval(string)
            print(instance.id)
            instance.save()
        except:
            print("** class doesn't exist **")
    def help_quit(self):
        ''' help_quit '''
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """help_EOF"""
        print("End of File command: exit the program\n")
    def do_show(self, line):
        """Prints an instance as a string based on the class and id"""    
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")
    def do_destroy(self, line):
        """Deletes an instance based on the class and id"""
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")
    def do_all(self, arg):
        """Prints string representations of instances"""
        className_line = shlex.split(arg)
        obj_list = []
        if len(className_line) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif className_line[0] in classGroup:
            for key in models.storage.all():
                if className_line[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")
    def do_update(self, line):
        """Update an instance based on the class name, id, attribute & value"""
        className_line = line.split()
        staticArray = ["id", "created_at", "updated_at"]
        objects = models.storage.all()
        if not line:
            print("** class name missing **")
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        else:
            instance = className_line[0] + "." + className_line[1]
            if instance not in models.storage.all():
                            print("** no instance found **")
            elif len(className_line) < 3:
                print("** attribute name missing **")
            elif len(className_line) < 4:
                print("** value missing **")
            elif className_line[2] not in staticArray:
                ojb = objects[instance]
                ojb.__dict__[className_line[2]] = className_line[3]
                ojb.updated_at = datetime.now()
                ojb.save()
    def do_count(self, line):
        "count instances of the class"
        className_line = line.split()
        if className_line[0] not in classGroup:
            return
        else:
            counter = 0
            keys_list = models.storage.all().keys()
            for searchKey in keys_list:
                len_searchKey = len(className_line[0])
                if searchKey[:len_searchKey] == className_line[0]:
                    counter += 1
            print(counter)

if __name__ == '__main__':
    HBNBCommand().cmdloop()