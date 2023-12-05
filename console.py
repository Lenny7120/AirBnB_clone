#!/usr/bin/python3
""" a console for the Airbnb project using cmd module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ the Airbnb console with hbnb as a prompt
    """
    prompt = "(hbnb)"

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
