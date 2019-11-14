#!/usr/bin/python3
""" Module for HBNBCommand class """
import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class - allow us to work in interactive mode """
    prompt = "(hbnb) "
    __names = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, argv):
        """ closes the program """
        return True

    def help_quit(self):
        """ help fuction for the command quit """
        print("Quit command to exit the program")

    def do_EOF(self, argv):
        """ close the program with Ctr-D """
        return True

    def help_EOF(self):
        """ help fuction for the command EOF """
        print("EOF command to exit the program")

    def emptyline(self):
        """ Avoids the last command from executing with an empty line """
        pass

    def do_create(self, argv):
        """ Creates a new instance """
        if argv in self.__names:
            new_instance = self.__names[argv]()
            new_instance.save()
            print("{}".format(new_instance.id))
        elif len(argv) is 0:
            print("** class name missing **")
        elif argv is not "BaseModel":
            print("** class doesn't exist **")

    def help_create(self):
        """ help function for the create command """
        print("create instances")

    def do_show(self, argv):
        """ prints an instance according to the given id """
        argument_split = argv.split()
        aux = 0
        if len(argument_split) == 0:
            print("** class name missing **")
        elif not argument_split[0] in self.__names:
            print("** class doesn't exist **")
        elif len(argument_split) < 2:
            print("** instance id missing **")
        elif argument_split[0] in self.__names:
            for key, obj in models.storage.all().items():
                if key == argument_split[0]+"."+argument_split[1]:
                    aux = 1
                    print(obj)
            if aux == 0:
                print("** no instance found **")

    def help_show(self):
        """ help function for the show command """
        print("print an instance based on the class name and id")

    def do_destroy(self, argv):
        """ destroys an instance """
        argument_split = argv.split()
        aux = 0

        if len(argument_split) == 0:
            print("** class name missing **")
        elif not argument_split[0] in self.__names:
            print("** class doesn't exist **")
        elif len(argument_split) < 2:
            print("** instance id missing **")
        elif argument_split[0] in self.__names:
            for key, obj in models.storage.all().items():
                if key == argument_split[0]+"."+argument_split[1]:
                    aux = 1
                    del (models.storage.all()[key])
                    models.storage.save()
                    return
            if aux == 0:
                print("** no instance found **")

    def help_destroy(self):
        """ help function for the command destroy """
        print("delete an instance based on the class name and id")

    def do_all(self, argv):
        """ prints all instances """
        list_obj = []
        if (argv in self.__names and
                len(argv.split()) < 2 or len(argv.split()) == 0):
            models.storage.reload()
            for key, obj in models.storage.all().items():
                list_obj.append(obj.__str__())
            print(list_obj)
        elif not (argv in self.__names):
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints all all instances based or not on the class name")

    def do_update(self, line):
        """ updates or adds a new attribute to a specific instance """
        args = shlex.split(line)
        size = len(args)
        db = models.storage.all()
        if size == 0:
            print("** class name missing **")
        elif not args[0] in self.__names:
            print("** class doesn't exist **")
        elif size == 1:
            print("** instance id missing **")
        elif not (args[0] + "." + args[1]) in db:
            print("** no instance found **")
        elif size == 2:
            print("** attribute name missing **")
        elif size == 3:
            print("** value missing **")
        else:
            new_dict = db[args[0] + "." + args[1]].to_dict()
            val = args[3]
            if self.is_int(val):
                val = int(val)
            elif self.is_float(val):
                val = float(val)
            new_dict[args[2]] = val
            obj = self.__names[args[0]](**new_dict)
            db[args[0] + "." + args[1]] = obj
            models.storage.save()

    def help_update(self):
        print("Updates an instance based on the class name and id")

    def is_float(self, val):
        """ test if val is a float """
        try:
            float(val)
            return True
        except ValueError:
            return False

    def is_int(self, val):
        """ test if val is an integer """
        try:
            int(val)
            return True
        except ValueError:
            return False

    def default(self, line):
        """ hnadle non-defined commands """
        text = line.split(".", 1)
        db = models.storage.all()

        if text[0] in self.__names:
            if text[1] == "all()":
                for k in db:
                    if k.split(".")[0] == text[0]:
                        print(db[k])
            if text[1] == "count()":
                count = 0
                for k in db:
                    if k.split(".")[0] == text[0]:
                        count += 1
                print(count)
            parsed = text[1].split("(")
            if len(parsed) != 2:
                return
            if len(parsed[1]) == 0:
                return
            if parsed[1][-1] != ")":
                return
            if parsed[0] == "show":
                for k in db:
                    k_div = k.split(".")
                    if k_div[0] == text[0] and k_div[1] == parsed[1][0:-1]:
                        print(db[k])
                        return
                print("** no instance found **")
            if parsed[0] == "destroy":
                for k in db:
                    k_div = k.split(".")
                    if k_div[0] == text[0] and k_div[1] == parsed[1][0:-1]:
                        del db[k]
                        models.storage.save()
                        return
                print("** no instance found **")
            if parsed[0] == "update":
                args = parsed[1][0:-1].split(",")
                size = len(args)
                if size != 0 and not len(args[0]):
                    print("** instance id missing **")
                    return
                if size == 1:
                    print("** attribute name missing **")
                    return
                elif size == 2:
                    print("** value missing **")
                    return
                k = text[0] + "." + args[0]
                if k in db:
                    new_dict = db[k].to_dict()
                    val = args[2].strip()
                    if self.is_int(val):
                        val = int(val)
                    elif self.is_float(val):
                        val = float(val)
                    new_dict[args[1].strip()] = val
                    obj = self.__names[text[0]](**new_dict)
                    db[k] = obj
                    models.storage.save()
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    """ Entry point of the console """
    HBNBCommand().cmdloop()
