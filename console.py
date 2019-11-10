#!/usr/bin/python3

import sys
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, argv):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, argv):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")

    def emptyline(self):
        pass

    def do_create(self, argv):
        if argv == "BaseModel":
            new_instance = BaseModel()
            models.storage.new(new_instance) 
            models.storage.save()
            print("{}".format(new_instance.id))
        elif len(argv) is 0:
            print("** class name missing **")
        elif argv is not "BaseModel":
            print("** class doesn't exist **")

    def help_create(self):
        print("create instances")

    def do_show(self, argv):
        argument_split = argv.split()
        aux = 0
       
        if len(argument_split) == 0:
            print("** class name missing **")
        elif argument_split[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argument_split) < 2:
            print("** instance id missing **")
        elif argument_split[0] == "BaseModel":
            for key, obj in models.storage.all().items():
                if key == argument_split[0]+"."+argument_split[1]:
                    aux = 1
                    print(obj)   
            if aux == 0:
                print("** no instance found **")

if __name__ == "__main__": 
    
    HBNBCommand().cmdloop()
