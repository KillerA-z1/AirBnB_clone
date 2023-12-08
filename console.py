#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter to manage AirBnB clone project.
    Attributes:
        prompt (str): The command prompt.
        intro (str): The introduction to the command interpreter.
    """
    intro = 'Welcome to AirBnB clone project.\n'
    prompt = "(hbnb) "
    cls = ["BaseModel", ]

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        print('Thank you for using AirBnB clone.')
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
