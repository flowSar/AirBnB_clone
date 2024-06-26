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
            giving_id = argument[1]
            try:
                with open(self.__file_path, "r") as f:
                    json_data = json.load(f)

                for obj in json_data:
                    obj_id = obj.split(".")[1]
                    obj_name = obj.split(".")[0]
                    if obj_name == giving_obj:
                        if obj_id == giving_id:
                            found = True
                            object_n = self.class_list[giving_obj]
                            new_obj = object_n(**json_data[obj])
                            print(new_obj)
            except FileNotFoundError:
                pass
            if not found:
                print("** no instance found **")

    def do_destroy(self, arg):
        """delete BaseModel instance from the file if exist
            Args:
                arg: argument that was passed with destroy command
        """
        argument = arg.split(" ")
        giving_obj = argument[0]
        found = False
        if (len(argument[0]) == 0):
            print("** class name missing **")
        elif (not self.is_class_exist(argument[0])):
            print("** class doesn't exist **")
        elif (len(argument) < 2):
            print("** instance id missing **")
        else:
            giving_id = argument[1]
            try:
                with open(self.__file_path, "r") as f:
                    json_data = json.load(f)

                for key in json_data:
                    obj_id = key.split(".")[1]
                    obj_name = key.split(".")[0]
                    if obj_name == giving_obj:
                        if obj_id == giving_id:
                            found = True
                            json_data.pop(key)
                            break
                with open(self.__file_path, "w") as f:
                    json.dump(json_data, f)
            except FileNotFoundError:
                pass
            if not found:
                print("** no instance found **")

    def do_all(self, arg):
        """print a list of all instance that exist in json file
            Args:
                arg: argument that was passed with all command
        """
        argument = arg.split(" ")
        giving_obj = argument[0]
        data = []

        if (len(argument[0]) > 0):
            if (not self.is_class_exist(argument[0])):
                print("** class doesn't exist **")
                return
        try:
            with open(self.__file_path, "r") as f:
                json_data = json.load(f)

            for key in json_data:
                obj = key.split(".")[0]
                if len(giving_obj) > 0:
                    if giving_obj == obj:
                        new_obj = self.class_list[obj](**json_data[key])
                        data.append(new_obj.__str__())
                else:
                    new_obj = self.class_list[obj](**json_data[key])
                    data.append(new_obj.__str__())
        except FileNotFoundError:
            pass
        if len(data) > 0:
            print(data)
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """this method for updating BaseModel instance attributes
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        giving_obj = argument[0]
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
            giving_id = argument[1]
            attribute = argument[2]
            value = argument[3]
            try:
                with open(self.__file_path, "r") as f:
                    json_data = json.load(f)

                for key in json_data:
                    obj_id = key.split(".")[1]
                    obj_name = key.split(".")[0]
                    if giving_obj == obj_name:
                        if obj_id == giving_id:
                            found = True
                            if (re.match(r"^(\d+\.\d+)$", value)):
                                json_data[key][attribute] = float(value)
                            elif (value[0] == "\""):
                                json_data[key][attribute] = value[1:-1]
                            else:
                                json_data[key][attribute] = int(value)
                            break

                with open(self.__file_path, "w") as f:
                    json.dump(json_data, f)
            except FileNotFoundError:
                pass
            if not found:
                print("** no instance found **")

    def do_User(self, arg):
        """this method for reteiving all User
           object data from json file
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        fun_name = argument[0]
        if re.search("update", arg):
            self.parse_and_update(arg, "User")
            return
        if (self.check_for_function(fun_name)):
            print("** instance id missing **")
            return
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]):
                if fun != ".all()" and fun != ".count()":
                    f = False

        if f is False:
            print("** no instance found **")
            return
        found, obj_id, data, count = self.get_obj_info(arg, "User")
        if fun_name == ".count()":
            print(count)
        elif found and fun_name == ".all()":
            print(data)
        elif not found or obj_id is None:
            print("** no instance found **")
        elif found and obj_id is not None:
            if re.match(".destroy", fun_name):
                self.do_destroy(f"User {obj_id}")
            else:
                print(data[0])

    def do_BaseModel(self, arg):
        """this method for reteiving all BaseModel
           object data from json file
            Args:
                arg: argument that was passed with update command
           """
        argument = arg.split(" ")
        fun_name = argument[0]
        if re.search("update", arg):
            self.parse_and_update(arg, "BaseModel")
            return
        if (self.check_for_function(fun_name)):
            print("** instance id missing **")
            return
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]):
                if fun != ".all()" and fun != ".count()":
                    f = False

        if f is False:
            print("** no instance found **")
            return
        found, object_id, data, count = self.get_obj_info(arg, "BaseModel")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found or object_id is None:
            print("** no instance found **")
        elif found and object_id is not None:
            if re.match(".destroy", fun_name):
                self.do_destroy(f"BaseModel {object_id}")
            else:
                print(data[0])

    def do_State(self, arg):
        """this method for reteiving all State
        object data from json file
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        fun_name = argument[0]
        if re.search("update", arg):
            self.parse_and_update(arg, "State")
            return
        if (self.check_for_function(fun_name)):
            print("** instance id missing **")
            return
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]):
                if fun != ".all()" and fun != ".count()":
                    f = False

        if f is False:
            print("** no instance found **")
            return
        found, object_id, data, count = self.get_obj_info(arg, "State")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found or object_id is None:
            print("** no instance found **")
        elif found and object_id is not None:
            if re.match(".destroy", fun_name):
                self.do_destroy(f"State {object_id}")
            else:
                print(data[0])

    def do_Place(self, arg):
        """this method for reteiving all
        Place object data from json file
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        fun_name = argument[0]
        if re.search("update", arg):
            self.parse_and_update(arg, "Place")
            return
        if (self.check_for_function(fun_name)):
            print("** instance id missing **")
            return
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(fun_name):
                if fun != ".all()" and fun != ".count()":
                    f = False

        if f is False:
            print("** no instance found **")
            return
        found, object_id, data, count = self.get_obj_info(arg, "Place")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found or object_id is None:
            print("** no instance found **")
        elif found and object_id is not None:
            if re.match(".destroy", fun_name):
                self.do_destroy(f"Place {object_id}")
            else:
                print(data[0])

    def do_City(self, arg):
        """this method for reteiving all
        City object data from json file
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        fun_name = argument[0]
        if re.search("update", arg):
            self.parse_and_update(arg, "City")
            return
        f = False
        if (self.check_for_function(fun_name)):
            print("** instance id missing **")
            return
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]):
                if fun != ".all()" and fun != ".count()":
                    f = False

        if f is False:
            print("** no instance found **")
            return
        found, object_id, data, count = self.get_obj_info(arg, "City")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found or object_id is None:
            print("** no instance found **")
        elif found and object_id is not None:
            if re.match(".destroy", fun_name):
                self.do_destroy(f"City {object_id}")
            else:
                print(data[0])

    def do_Review(self, arg):
        """this method for reteiving all
        Review object data from json file
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        fun_name = argument[0]
        if re.search("update", arg):
            self.parse_and_update(arg, "Review")
            return
        if (self.check_for_function(fun_name)):
            print("** instance id missing **")
            return
        f = False
        for fun in self.function_list:
            if re.match(fun, argument[0]):
                f = True
            if len(fun) == len(argument[0]):
                if fun != ".all()" and fun != ".count()":
                    f = False

        if f is False:
            print("** no instance found **")
            return
        found, object_id, data, count = self.get_obj_info(arg, "Review")
        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found or object_id is None:
            print("** no instance found **")
        elif found and object_id is not None:
            if re.match(".destroy", fun_name):
                self.do_destroy(f"Review {object_id}")
            else:
                print(data[0])

    def do_Amenity(self, arg):
        """this method for reteiving all Amenity
        object data from json file
            Args:
                arg: argument that was passed with update command
        """
        argument = arg.split(" ")
        fun_name = argument[0]
        if re.search("update", arg):
            self.parse_and_update(arg, "Amenity")
            return
        if (self.check_for_function(fun_name)):
            print("** instance id missing **")
            return

        f = False
        for fun in self.function_list:
            if re.match(fun, fun_name):
                f = True
            if len(fun) == len(fun_name):
                if fun != ".all()" and fun != ".count()":
                    f = False

        if f is False:
            print("** no instance found **")
            return
        found, obj_id, data, count = self.get_obj_info(arg, "Amenity")

        if found and fun_name == ".all()":
            print(data)
        elif fun_name == ".count()":
            print(count)
        elif not found or obj_id is None:
            print("** no instance found **")
        elif found and obj_id is not None:
            if re.match(".destroy", fun_name):
                self.do_destroy(f"Amenity {obj_id}")
            else:
                print(data[0])

    def get_id(self, argument):
        """this method parse the command line and get the id
            if he was giving and return it or return None
            if he wasn't giving.
            Args:
                arg: argument that was passed with update command
        """
        arg = argument
        object_id = None
        if ".show(" in arg:
            if arg[5:] != "()":
                object_id = arg[7:-2]
        elif ".destroy(" in arg:
            if arg[8:] != "()":
                object_id = arg[10:-2]
        return object_id

    def get_obj_info(self, arg, cls_name):
        """
            ths fnction work on getting all ifnfo about object
            if he's exist on the file his id , number of this object
            in the file , and return all data of this object
            all this data we return it in tuple
            args:
                arg: command line
                cls_name: class name that we are looking for in the file
        """
        argument = arg.split(" ")
        fun_name = argument[0]
        object_id = self.get_id(argument[0])
        data = []
        found = False
        count = 0

        try:
            if len(arg) <= 1:
                return (False, None, [], None, 0)
            else:
                with open(self.__file_path, "r") as f:
                    js_data = json.load(f)
                for key in js_data:
                    obj_name_f = key.split(".")[0]
                    object_id_f = key.split(".")[1]
                    if obj_name_f == cls_name:
                        count += 1
                        if object_id_f == object_id:
                            object_n = self.class_list[obj_name_f]
                            new_obj = object_n(**js_data[key])
                            data.append(new_obj.__str__())
                            return (True, object_id, data, count)
                        else:
                            new_obj = self.class_list[cls_name](**js_data[key])
                            data.append(new_obj.__str__())
                            found = True
                return (found, None, data, count)
        except FileNotFoundError:
            return (False, None, [], 0)

    def check_for_function(self, fun_name):
        """this method for checking if the function match a specific
            name so we can know which action we will take
            Args:
                fun_name: function name
        """
        pattern = r"\.show\(\)$|\.destroy\(\)$|.update()$"
        if re.match(pattern, fun_name):
            return True
        else:
            return False

    def parse_and_update(self, arg, obj_name):
        """this method woks on parse command line
            for updating the object
            Args :
                arg: command line.
                obj_name: object that we are working on.
        """
        args = arg.split(",")
        pattern = r'\{[^}]*\}'

        if re.search(pattern, arg):
            self.hand_dictionay_case(arg, obj_name, args[0][9:-1].strip())
            return

        if args[0] == ".update()":
            print("** instance id missing **")
            return
        elif len(args) < 2:
            print("** attribute name missing **")
            return
        elif len(args) < 3:
            print("** value missing **")
            return
        obj_id = args[0][9:-1].strip()
        if isinstance(eval(args[1][:-1]), dict):
            print("yes dictionay")
        attribute = args[1][2:-1].strip()
        value = args[2][:-1].strip()
        self.do_update(f"{obj_name} {obj_id} {attribute} {value}")

    def hand_dictionay_case(self, arg, obj_name, obj_id):
        """this handle case when we use update function with
        dictionay of attributes and its values"""
        found = 0
        extracted_striny = ""
        for c in arg:
            if c == '{':
                found += 1
            if found == 1:
                extracted_striny += c
                if c == '}':
                    break
        attributes_value = extracted_striny[1:-1].split(", ")
        for att_v in attributes_value:
            data = att_v.split(": ")
            self.do_update(f"{obj_name} {obj_id} {data[0][1:-1]} {data[1]}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
