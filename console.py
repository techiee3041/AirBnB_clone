#!/usr/bin/python3

"""Module containing the HBNB console"""

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): This is the command prompt
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """
            creates a new class instance and prints the id

            Usage: create <class>
        """
        line = shlex.split(arg)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(line[0])().id)
            models.storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance

           Usage: show <class> <id> or <class>.show(<id>)

        """
        args = shlex.split(arg)
        objs = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            if instance_key not in objs:
                print("** no instance found **")
            else:
                instance = objs[instance_key]
                print(instance)
                models.storage.save()

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id and saves it
            Usage: destroy <class> <id>
        """
        args = shlex.split(arg)
        objs = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objs.keys():
            print("** no instance found **")
        else:
            del objs[f"{args[0]}.{args[1]}"]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances.

            Usage: all or all <class> or <class>.all()
        """
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objects = []
            for x in models.storage.all().values():
                if len(args) > 0 and args[0] == x.__class__.__name__:
                    objects.append(x.__str__())
                elif len(args) == 0:
                    objects.append(x.__str__())
            print(objects)

    def do_update(self, arg):
        """Updates an instance"""
        args = shlex.split(arg)
        dictionary = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if f"{args[0]}.{args[1]}" not in dictionary.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except Exception:
                print("** value missing **")
                return False
        if len(args) == 4:
            x = dictionary[f"{args[0]}.{args[1]}"]
            if args[2] in x.__class__.__dict__.keys():
                value_type = type(dictionary.__class__.__dict__[args[2]])
                type(dictionary.__class__.__dict__[args[2]])
            else:
                x.__dict__[args[2]] = args[3]
        if type(eval(args[2])) == dict:
            x = dictionary[f"{args[0]}.{args[1]}"]
            for key, value in eval(args[2]).items():
                if (key in x.__class__.__dict__.keys() and
                        type(x.__class__.__dict__[key]) in {str, int, float}):
                    value_type = type(x.__class__.__dict__[key])
                    x.__dict__[key] = value_type(value)
                else:
                    x.__dict__[key] = value
        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
