#!/usr/bin/python3
""" a console for the Airbnb project using cmd module"""
import cmd
import sys
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
            class_name = args[0]
            # Instantiate dynamically
            new_instance = globals()[class_name]()
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
            all_objs = storage.all()  # fix
            if key in all_objs.keys():
                print(all_objs[key])
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
            all_objs = storage.all()  # fix
            if key in all_objs.keys():
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of all
        instances bases on class names or all class
        Usage: all <class name>
        """
        args = arg.split()
        obj_list = []
        if not args or args[0] in self.valid_classes:
            for key, obj in storage.all().items():
                if not args or key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
                    print(obj_list)
                else:
                    print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and
        id by adding an attribute
        Usage: update [class name]
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
            all_objs = storage.all()  # fix
            if key in all_objs.keys():
                obj = all_objs[key]
                # fix
                if len(args) % 2 == 0:  # correct pairs of attrib & val
                    for i in range(2, len(args), 2):
                        attr_nme = args[i]
                        attr_val = args[i + 1].strip('"')
                        # check if attrib exists
                        if hasattr(obj, attr_nme):
                            setattr(obj, attr_nme,
                                    type(getattr(obj, attr_nme))(attr_val))
                        else:
                            # add new attrib otherwise
                            setattr(obj, attr_nme, attr_val)
                obj.save()
            else:
                print("** no instance found **")

    def default(self, arg):
        """Handle default behaviour when input is not recognized
        """
        method_dict = {
            'all': self.do_all,
            'count': self.do_count,
            'destroy': self.do_destroy,
            'show': self.do_show,
            # 'update': self.do_update
        }

        if "." in arg:
            cls_name, params = arg.split(".", 1)  # split only once
            if "(" in params and params.endswith(")"):
                method, _args = params.split("(", 1)
                if method == "update":
                    update_args = params.rstrip(")").split("(")[1]
                    # Split arguments by comma and strip whitespace
                    upd_args = [arg.strip().strip('"')
                                for arg in update_args.split(",")]
                    cls_and_id = cls_name.split()
                    cls_name = cls_and_id[1] if len(cls_and_id) > 1 else ""
                    upd_call = f"{cls_name} {cls_and_id[0]} "
                    return self.do_update(upd_call + ' '.join(upd_args))

                if '"' in _args and _args.count('"') == 2:
                    _args = _args.rstrip(")")  # remove the ")"
                    _args = _args.replace('"', '')  # remove quotes
                    if method in method_dict:
                        call = f"{cls_name} {_args}"
                        return method_dict[method](call)
                else:
                    _args = ""
                    if method in method_dict:
                        call = f"{cls_name} {_args}"
                        return method_dict[method](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class.
        Usage: <class name>.count()
        """
        args = arg.split()
        if not args:
            return
        elif args[0] not in self.valid_classes:
            return
        else:
            class_name = args[0]

        count = 0
        for key in storage.all().keys():
            stored_class_name, instance_id = key.split(".")
            if class_name == stored_class_name:
                count += 1
        print(count)

    def precmd(self, line):
        """Non-interactive functioning of console
        """
        if not sys.stdin.isatty():
            print()
        return line

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
