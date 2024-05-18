#!/usr/bin/python3

import re

#def do_User(self, arg):
        #"""this method for reteiving all User object data from json file"""
    
    #found, object_id, data, fun_name, count = get_user_info_state(arg, "User")
    
    
    #if not found or fun_name == ".show()" or fun_name == ".destroy()":
        #print("** no instance found **")
    #elif found and fun_name == ".all()":
        #print(data)
    #elif found and fun_name == ".count()":
        #print(count)
    #elif found and object_id is not None:
        #self.do_destroy(f"User {object_id}")
    #else:
        #print(data)

#def get_user_info_state(self, arg, class_name):
      
    #argument = arg.split(" ")
    #fun_name = argument[0]
    #object_id = get_id(fun_name)
    #data = []
    #found = False
    #count = 0
      
    #try :
        #with open(self.__file_path, "r") as f:
            #json_data = json.load(f)
    #except FileNotFoundError:
        #pass
    #else:
        #for key in json_data:
            #object_name_f = key.split(".")[0]
            #object_id_f = key.split(".")[1]
            #if object_name_f == class_name:
                #count += 1
                #if object_id_f == object_id:
                    #new_obj = self.class_list[object_name_f](**json_data[key])
                    #data.append(new_obj.__str__())
                    #return (True , object_id, data, fun_name, count)
            #else:
                    #new_obj = self.class_list[class_name](**json_data[key])
                    #data.append(new_obj.__str__())
                    #found = True
            
        #return (found, None, data, fun_name, count)



# 77211966-b927-4265-aa71-38d31101fd37

number
= "3.5666"

if re.match(r"^(\d+(\.\d+)?)$", number):
    print("match")
else:
    print("dosn'tmatch")



