#!/usr/bin/python3

import sys
import cmd

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

if __name__ == "__main__": 
    
    HBNBCommand().cmdloop()
