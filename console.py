#!/usr/bin/python3
""" a console for the Airbnb project using cmd module"""
import cmd
# from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models.user import User


class HBNBCommand(cmd.Cmd):
    """ the Airbnb console with hbnb as a prompt
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    def do_create(self, arg):
        """ Create a new instance of the Base Model,
        save it and print the id.
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print string representation of an instance
        based on class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in BaseModel.__objects:
                print(BaseModel.__objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance base on class name and id
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in BaseModel.__objects:
                del BaseModel.__objects[key]
                BaseModel.save_to_file()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of all
        instances bases on class names or all class
        Usage: all [class name]
        """
        args = arg.split()
        obj_list = []
        if not args or args[0] in self.valid_classes:
            for key, obj in BaseModel.__objects.items():
                if not args or key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
                    print(obj_list)
                else:
                    print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and
        id by adding an attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in BaseModel.__objects:
                obj = BaseModel.__objects[key]
                attr_nme = args[2]
                attr_val = args[3].strip('"')
                setattr(obj, attr_nme, type(getattr(obj, attr_nme))(attr_val))
                obj.save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Exit the command-line interface.
        """
        return True

    def do_EOF(self, arg):
        """Handle the End-of-file (EOF) signal
        """
        return True

    def do_help(self, arg):
        """Get help on commands
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing on empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
