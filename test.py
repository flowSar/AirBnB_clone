#!/usr/bin/python3
import re
class Animal:
    """
    this is Animal class
    it continue all Animal functions
    """
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        """this meyhod print the name if instance animal"""
        print(f"you're name is {self.__name}")


pattern = r"^(\d+\.\d+)$"

if re.match(pattern, "6.5"):
    print("match")
else:
    print("doesn't match")
