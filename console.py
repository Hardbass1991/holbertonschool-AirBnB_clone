#!/usr/bin/python3
"""Module that defines a console for manipulating 
instances of imported classes
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """Console for manipulating objects"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        'Quit command to exit the program'
        self.close()
        quit()
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        self.close()
        quit()
    
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def do_create(self, arg):
        'Creates an empty instance of input class'
        m = {
            "BaseModel": BaseModel, 
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if not arg:
            print("** class name missing **")
        elif arg not in m.keys():
            print("** class doesn't exist **")
        else:
            new_obj = m[arg]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        'Shows existing instance of input class and id'
        objs = storage.all()
        classes = list(map(lambda x: x.split(".")[0], objs.keys()))
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name not in classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                id = args[1]
                k = cls_name + "." + id
                if k not in objs.keys():
                    print("** no instance found **")
                else:
                    print(objs[k])

    def do_destroy(self, arg):
        'Deletes existing instance of input class and id'
        objs = storage.all()
        classes = list(map(lambda x: x.split(".")[0], objs.keys()))
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name not in classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                id = args[1]
                k = cls_name + "." + id
                if k not in objs.keys():
                    print("** no instance found **")
                else:
                    del objs[k]
                    storage.save()

    def do_all(self, arg):
        'Displays all instances of input class'
        objs = dict(storage.all())
        classes = list(map(lambda x: x.split(".")[0], objs.keys()))
        class_exists = True
        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
                class_exists = False
            else:
                objs = {k: v for k, v in objs.items() if k.split(".")[0] == arg}
        if class_exists:
            for value in objs.values():
                print(value.__str__())

    def do_update(self, arg):
        'Updates existing instance of input class and id with input value'
        objs = storage.all()
        classes = list(map(lambda x: x.split(".")[0], objs.keys()))
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name not in classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                id = args[1]
                k = cls_name + "." + id
                if k not in objs.keys():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                else:
                    attr_name = args[2]
                    if len(args) == 3:
                        print("** value missing **")
                    else:
                        val = args[3]
                        # print("k: " + attr_name + ", v: " + val)
                        objs[k].__dict__[attr_name] = val
                        # print(objs)
                        storage.save()

def parse(arg):
    return tuple(arg.split())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
