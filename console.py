#!/usr/bin/python3
""" console module hava a class for implement CLI
    command line interface for this application
"""

import cmd
import re
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
    function_list = [".all()",
                    ".destroy()",
                    ".show()",
                    ".count()"]

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
        giving_obj = argument[0]
        found = False
        if (len(giving_obj) == 0):
            print("** class name missing **")
        elif (not self.is_class_exist(giving_obj)):
            print("** class doesn't exist **")
        elif (len(argument) < 2):
            print("** instance id missing **")
        else:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)
            for obj in json_data:
                obj_id = obj.split(".")[1]
                obj_name = obj.split(".")[0]
                if obj_name == giving_obj:
                    if obj_id == argument[1]:
                        found = True
                        new_obj = self.class_list[giving_obj](**json_data[obj])
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
 
    def do_User(self, arg):
        """this method for reteiving all User object data from json file"""
        argument = arg.split(" ")
        fun_name = argument[0]
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]) and fun != ".all()" and fun != ".count()":
                f = False

        if f == False:
            print("** no instance found **")
            return
        found, object_id, data, fun_name, count = self.get_object_info_state(arg, "User")
        if fun_name == ".count()":
            print(count)
        elif found and fun_name == ".all()":
            print(data)
        elif not found:
            print("** no instance found **")
        elif found and object_id is not None and re.match(".destroy", fun_name):
            self.do_destroy(f"User {object_id}")
        else:
            print(data)

   
    def do_BaseModel(self, arg):
        """this method for reteiving all BaseModel object data from json file"""
        argument = arg.split(" ")
        fun_name = argument[0]
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]) and fun != ".all()" and fun != ".count()":
                f = False

        if f == False:
            print("** no instance found **")
            return
        found, object_id, data, fun_name, count = self.get_object_info_state(arg, "BaseModel")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found:
            print("** no instance found **")
        elif found and object_id is not None and re.match(".destroy", fun_name):
            self.do_destroy(f"BaseModel {object_id}")
        else:
            print(data)


    def do_State(self, arg):
        """this method for reteiving all State object data from json file"""
        argument = arg.split(" ")
        fun_name = argument[0]
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]) and fun != ".all()" and fun != ".count()":
                f = False

        if f == False:
            print("** no instance found **")
            return
        found, object_id, data, fun_name, count = self.get_object_info_state(arg, "State")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found:
            print("** no instance found **")
        elif found and object_id is not None and re.match(".destroy", fun_name):
            self.do_destroy(f"State {object_id}")
        else:
            print(data)


    def do_Place(self, arg):
        """this method for reteiving all Place object data from json file"""
        argument = arg.split(" ")
        fun_name = argument[0]
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]) and fun != ".all()" and fun != ".count()":
                f = False

        if f == False:
            print("** no instance found **")
            return
        found, object_id, data, fun_name, count = self.get_object_info_state(arg, "Place")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found:
            print("** no instance found **")
        elif found and object_id is not None and re.match(".destroy", fun_name):
            self.do_destroy(f"Place {object_id}")
        else:
            print(data)

            
    def do_City(self, arg):
        """this method for reteiving all City object data from json file"""
        argument = arg.split(" ")
        fun_name = argument[0]
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]) and fun != ".all()" and fun != ".count()":
                f = False

        if f == False:
            print("** no instance found **")
            return
        found, object_id, data, fun_name, count = self.get_object_info_state(arg, "City")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found:
            print("** no instance found **")
        elif found and object_id is not None and re.match(".destroy", fun_name):
            self.do_destroy(f"City {object_id}")
        else:
            print(data)

            
    def do_Review(self, arg):
        """this method for reteiving all Review object data from json file"""
        argument = arg.split(" ")
        fun_name = argument[0]
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]) and fun != ".all()" and fun != ".count()":
                f = False

        if f == False:
            print("** no instance found **")
            return
        found, object_id, data, fun_name, count = self.get_object_info_state(arg, "Review")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found:
            print("** no instance found **")
        elif found and object_id is not None and re.match(".destroy", fun_name):
            self.do_destroy(f"Review {object_id}")
        else:
            print(data)

        
    def do_Amenity(self, arg):
        """this method for reteiving all Amenity object data from json file"""
        argument = arg.split(" ")
        fun_name = argument[0]
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]) and fun != ".all()" and fun != ".count()":
                f = False

        if f == False:
            print("** no instance found **")
            return
        found, object_id, data, fun_name, count = self.get_object_info_state(arg, "Amenity")

        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found:
            print("** no instance found **")
        elif found and object_id is not None and re.match(".destroy", fun_name):
            self.do_destroy(f"Amenity {object_id}")
        else:
            print(data)

        
    def get_id(self, argument):
        arg = argument
        object_id = None
        if ".show(" in arg:
            if arg[5:] != "()":
                object_id = arg[6:-1]
        elif ".destroy(" in arg:
            if arg[8:] != "()":
                object_id = arg[9:-1]
        return object_id

    def get_object_info_state(self, arg, class_name):
            argument = arg.split(" ")
            fun_name = argument[0]
            object_id = self.get_id(argument[0])
            data = []
            found = False
            count = 0
            
            if len(arg) <= 1:
                return (False, None, [], None, 0)
            try :
                with open(self.__file_path, "r") as f:
                    json_data = json.load(f)
            except FileNotFoundError:
                pass
            else:
                for key in json_data:
                    object_name_f = key.split(".")[0]
                    object_id_f = key.split(".")[1]
                    if object_name_f == class_name:
                        count += 1
                        if object_id_f == object_id:
                            new_obj = self.class_list[object_name_f](**json_data[key])
                            data.append(new_obj.__str__())
                            return (True , object_id, data, fun_name, count)
                        else:
                            new_obj = self.class_list[class_name](**json_data[key])
                            data.append(new_obj.__str__())
                            found = True
                return (found, None, data, fun_name, count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
