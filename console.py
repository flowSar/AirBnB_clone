#!/usr/bin/python3
""" console module hava a class for implement CLI
    command line interface for this application
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
import json

msg = """
Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all
"""


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    __file_path = "file.json"
    class_list = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def is_class_exist(self, class_name):
        """this method for checking if class exist in out list
            Return:
                True is exist an dFalse if doesn't
        """
        exist = False
        for cls in self.class_list:
            if (cls == class_name):
                exist = True
        return exist

    def emptyline(self):
        """method triggered when theres not command"""
        arg = ""

    def do_quit(self, arg):
        """Quit the application
            Args:
                arg: argument that was passed with quit command
        """
        return True  # Exit the

    def do_EOF(self, arg):
        """quit the application with CTRL^D"""
        print("")
        return True

    def do_help(self, arg):
        """ovvriding help method and comstumize it for our application
            Args:
                arg: argument that was passed with help command
        """
        argument = arg.split(" ")
        if (len(argument[0]) >= 1):
            print("Quit command to exit the program\n")
        else:
            print(msg)

    def do_create(self, arg):
        """create new Instance of a class BaseModel and save it to json file
            Args:
                arg: argument that was passed with create command
        """
        argument = arg.split(" ")
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (not self.is_class_exist(argument[0])):
            print("** class doesn't exist **")
        else:
            new_object = self.class_list[argument[0]]()
            storage.reload()
            new_object.save()
            print(new_object.id)

    def do_show(self, arg):
        """show BaseModel for giving id if it's exist in json file
            Args:
                arg: argument that was passed with show command
        """
        argument = arg.split(" ")
        found = False
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (not self.is_class_exist(argument[0])):
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
                    new_obj = self.class_list[argument[0]](**json_data[obj])
                    print(new_obj)

            if not found:
                print("** no instance found **")

    def do_destroy(self, arg):
        """delete BaseModel instance from the file if exist
            Args:
                arg: argument that was passed with destroy command
        """
        argument = arg.split(" ")
        found = False
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (not self.is_class_exist(argument[0])):
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
        """print a list of all instance that exist in json file
            Args:
                arg: argument that was passed with all command
        """
        argument = arg.split(" ")
        data = []
        
        if (len(argument[0]) > 0):
            if (not self.is_class_exist(argument[0])):
                print("** class doesn't exist **")
            else:
                with open(self.__file_path, "r") as f:
                    json_data = json.load(f)
                for key in json_data:
                    class_name = key.split(".")[0]
                    if class_name == argument[0]:
                        new_obj = self.class_list[class_name](**json_data[key])
                        data.append(new_obj.__str__())
                print(data)
        else:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)
            for key in json_data:
                class_name = key.split(".")[0]
                new_obj = self.class_list[class_name](**json_data[key])
                data.append(new_obj.__str__())
            print(data)

    def do_update(self, arg):
        """this method for updating BaseModel instance attributes
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        found = False
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (not self.is_class_exist(argument[0])):
            print("** class doesn't exist **")
        elif (len(argument) < 2):
            print("** instance id missing **")
        elif (len(argument) < 3):
            print("** attribute name missing **")
        elif (len(argument) < 4):
            print("** value missing **")
        else:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)
            for obj in json_data:
                obj_id = obj.split(".")[1]
                if obj_id == argument[1]:
                    found = True
                    new_object = self.class_list[argument[0]](json_data[obj])

                    if ("." in argument[3]):
                        json_data[obj][argument[2]] = float(argument[3])
                    elif (argument[3][0] == "\""):
                        json_data[obj][argument[2]] = argument[3][1:-1]
                    else:
                        json_data[obj][argument[2]] = int(argument[3])
                    break

            if not found:
                print("** no instance found **")
            with open(self.__file_path, "w") as f:
                json.dump(json_data, f)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
