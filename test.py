#!/usr/bin/python3

import cmd
import uuid
from datetime import datetime

class MyApp(cmd.Cmd):
    prompt ='myapp>' # Set the prompt

    def do_greet(self, arg):
        """Greet the user"""
        print(f"Hello, {arg}!")
    def do_action(self, arg):
        print("")
    
    def do_id(self, arg):
        """generate Id for user"""
        print(f"this is your id : {uuid.uuid1()}")
    def do_date(self, arg):
        print(f"date: {datetime.now().isoformat(timespec='microseconds')}")

    def do_quit(self, arg):
        """Quit the application"""
        print("Goodbye!")
        return True  # Exit the application
    def do_EOF(self, arg):
        print("")
        return True


if __name__ == '__main__':
    app = MyApp()
    app.cmdloop()  
