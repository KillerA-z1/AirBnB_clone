#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter to manage AirBnB clone project.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                'Place': Place,
                'City': City,
                'Review': Review,
                'State': State,
                'Amenity': Amenity,
                        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of a given class, saves it to the file,
            and prints its id.
        Usage: create <class>
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            # Assuming you have a dictionary mapping class names to classes
            # Add all your classes here
            class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                'Place': Place,
                'City': City,
                'Review': Review,
                'State': State,
                'Amenity': Amenity,
                        }
            new_instance = class_dict[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        words = arg.split()
        class_name = words[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(words) < 2:
            print("** instance id missing **")
            return

        instance_id = words[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all(class_name)
        if key not in instances:
            print("** no instance found **")
        else:
            print(instances[key])

    def do_all(self, line):
        """Print string representation of all instances based on class name."""
        if line:
            words = line.split(' ')
            class_name = words[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            nl = [str(obj) for key, obj in storage.all().items()
                  if type(obj).__name__ == class_name]
            print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instances = storage.all(args[0])
        key = "{}.{}".format(args[0], args[1])
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if "{" in args[2]:  # check if the third argument is a dictionary
            attr_dict = eval(args[2])  # convert the string to a dictionary
            for attr_name, attr_value in attr_dict.items():
                if attr_name not in ['id', 'created_at', 'updated_at']:
                    if isinstance(attr_value, int):
                        attr_value = int(attr_value)
                    elif isinstance(attr_value, float):
                        attr_value = float(attr_value)
                    else:
                        attr_value = str(attr_value)  # handle string attribute values
                    setattr(instances[key], attr_name, attr_value)
        else:
            attr_name = args[2]
            attr_value = args[3]
            if attr_name not in ['id', 'created_at', 'updated_at']:
                if attr_value.isdigit():
                    attr_value = int(attr_value)
                elif attr_value.replace('.', '', 1).isdigit():
                    attr_value = float(attr_value)
                else:
                    attr_value = str(attr_value)  # handle string attribute values
                setattr(instances[key], attr_name, attr_value)
        instances[key].save()
        storage.save()

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Args:
            arg (str): The class name and id separated by a space.
        """
        args = arg.split()
        if len(args) != 2:
            print("** class name missing **")
            return
        class_name, id = args
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def default(self, line):
        """
    Method called on an input line when the command prefix is not recognized.
    In this case, it's used to handle the <class name>.show(<id>) syntax.

    Args:
        line (str): The input line.
    """
        if '.' in line:
            words = line.split('.')
            if len(words) > 1:
                if words[1].startswith('show("') and words[1].endswith('")'):
                    id = words[1][6:-2]  # Extract the id from the string
                    self.do_show(f"{words[0]} {id}")
                elif words[1].startswith('destroy("') and words[1].endswith('")'):
                    id = words[1][9:-2]  # Extract the id from the string
                    self.do_destroy(f"{words[0]} {id}")
                elif words[1].startswith('update("') and words[1].endswith('")'):
                    # Use regular expressions to extract the id, attribute name, and attribute value from the string
                    match = re.match(r'update\("([^"]*)", "([^"]*)", "([^"]*)"\)', words[1])
                    if match:
                        id, attr_name, attr_value = match.groups()
                        self.do_update(f"{words[0]} {id} {attr_name} {attr_value}")
            else:
                super().default(line)
        else:
            super().default(line)

    def do_count(self, class_name):
        """
    Counts the number of instances of a given class.

    This method iterates over all objects in storage, and increments a counter
    for each object that is an instance of the specified class. The count is
    then printed to the console.

    If the specified class does not exist, an error message is printed and the
    method returns without counting.

    Args:
        class_name (str): The name of the class to count instances of.
    """
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
