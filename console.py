#!/usr/bin/python3
""" console module hava a class for implement CLI
    command line interface for this application
"""

import cmd
from models.base_model import BaseModel
import json

msg = """
Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all
"""


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    __file_path = "file.json"

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

    def do_create(self, arg):
        """create new Instance of a class BaseModel and save it to json file"""
        argument = arg.split(" ")
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (argument[0] != "BaseModel"):
            print("** class doesn't exist **")
        else:
            baseModel = BaseModel()
            baseModel.save()
            print(baseModel.id)

    def do_show(self, arg):
        """show BaseModel for giving id if it's exist in json file"""
        argument = arg.split(" ")
        found = False
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (argument[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif (len(argument) < 2):
            print("** instance id missing **")
        else:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)
            for obj in json_data:
                obj_id = obj.split(".")[1]
                if obj_id == argument[1]:
                    found = True
                    new_obj = BaseModel(json_data[obj])
                    print(new_obj)

            if not found:
                print("** no instance found **")

    def do_destroy(self, arg):
        """delete BaseModel instance from the file if exist"""
        argument = arg.split(" ")
        found = False
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (argument[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif (len(argument) < 2):
            print("** instance id missing **")
        else:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)
            for obj in json_data:
                obj_id = obj.split(".")[1]
                if obj_id == argument[1]:
                    found = True
                    json_data.pop(obj)
                    break
            with open(self.__file_path, "w") as f:
                json.dump(json_data, f)
            if not found:
                print("** no instance found **")

    def do_all(self, arg):
        """print a list of all instance that exist in json file"""
        argument = arg.split(" ")
        data = []
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (argument[0] != "BaseModel"):
            print("** class doesn't exist **")
        else:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)
            for key in json_data:
                new_obj = BaseModel(json_data[key])
                data.append(new_obj.__str__())

        print(data)

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
