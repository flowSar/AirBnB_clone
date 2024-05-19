#!/usr/bin/python3
#from models import storage
#from models.base_model import BaseModel
#from models.user import User
#from datetime import datetime

#all_objs = storage.all()

#dict_test = {"__class__": "BaseModel",
            #"id": "709cb71f-fd9f-4b1e-a2a9-c042f25e2c18",
            #"created_at": "2024-05-18T23:23:31.377466",
            #"updated_at": "2024-05-18T23:23:31.377730",
            #"email": "email@gmail.com"}
#base = BaseModel()
#base.email = "email@gmail.com"
#base.save()
#ssar = base.__dict__
#print(str(base.__dict__['updated_at']))
#if "datetime.datetime(2024, 5, 18, 23, 23, 31, 377730)" == BaseModel.__dict__["updated_at"]:
    #print("match")
#else:
    #print("doesn't match")
#print(ssar)
#print(datetime.fromisoformat("2024-05-18T23:23:31.377466"))
#print(base.__dict__['created_at'])


my_dict = {"name": "brahim"}

for key, value in my_dict.items():
    print(f"{key}: {value}")
