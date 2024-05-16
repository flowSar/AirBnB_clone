#!/usr/bin/python3
""" console module hava a class for implement CLI
    command line interface for this application
"""

import cmd

msg = """
Documented commands (type help <topic>):
========================================
EOF  help  quit
"""


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def emptyline(self):
        """method triggered when theres not command"""
        arg = ""

    def do_quit(self, arg):
        """Quit the application"""
        return True  # Exit the

    def do_EOF(self, arg):
        """quit the application with CTRL^D"""
        print("")
        return True

    def do_help(self, arg):
        """ovvriding help method and comstumize it for our application"""
        argument = arg.split(" ")
        if (len(argument[0]) >= 1):
            print("Quit command to exit the program\n")
        else:
            print(msg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
