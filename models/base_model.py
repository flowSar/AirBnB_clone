#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    
	def __init__(self, f, *args, **kwargs):
		self.id = uuid.uuid4()
		self.created_at = datetime.now().isoformat(timespec='microseconds')
		self.updated_at = datetime.now().isoformat(timespec='microseconds')

	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		self.updated_at = datetime.now().isoformat(timespec='microseconds')
    
	def to_dict(self):
		dict_class = {"__class__":self.__class__.__name__}
		dict_class.update(self.__dict__)
		return dict_class
    

if __name__ == "__main__":
	my_model = BaseModel()
	my_model.name = "My First Model"
	my_model.my_number = 89
	print(my_model)
	my_model.save()
	print(my_model)
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	for key in my_model_json.keys():
		print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    

