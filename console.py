#!/usr/bin/python3
"""
Console module for AirBnB clone project.
Contains the entry point of the command interpreter.
"""
import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone"""

    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def default(self, line):
        """Handle Class.method() syntax"""
        match = re.match(r'^(\w+)\.(\w+)\((.*)\)$', line)
        if match:
            class_name = match.group(1)
            method = match.group(2)
            args = match.group(3)
            
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            
            if method == "all":
                self.do_all(class_name)
            elif method == "count":
                self.do_count(class_name)
            elif method == "show":
                obj_id = args.strip('"').strip("'")
                self.do_show(f"{class_name} {obj_id}")
            elif method == "destroy":
                obj_id = args.strip('"').strip("'")
                self.do_destroy(f"{class_name} {obj_id}")
            elif method == "update":
                self.handle_update(class_name, args)
        else:
            print(f"*** Unknown syntax: {line}")

    def handle_update(self, class_name, args):
        """Handle update with dictionary or attributes"""
        import ast
        args = args.strip()
        
        # Try to match dictionary update
        dict_match = re.match(r'^"([^"]+)",\s*(\{.+\})$', args)
        if dict_match:
            obj_id = dict_match.group(1)
            dict_str = dict_match.group(2)
            try:
                update_dict = ast.literal_eval(dict_str)
                key = f"{class_name}.{obj_id}"
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                    return
                obj = objects[key]
                for attr, value in update_dict.items():
                    if attr not in ['id', 'created_at', 'updated_at']:
                        setattr(obj, attr, value)
                obj.save()
                return
            except:
                pass
        
        # Regular update with attribute name and value
        parts = [p.strip(' ",\'') for p in args.split(',')]
        if len(parts) >= 3:
            obj_id = parts[0]
            attr_name = parts[1]
            attr_value = parts[2]
            self.do_update(f"{class_name} {obj_id} {attr_name} {attr_value}")

    def do_count(self, arg):
        """Count instances of a class"""
        if not arg:
            return
        class_name = arg.strip()
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        count = sum(1 for key in objects if key.startswith(class_name + "."))
        print(count)

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it and prints the id
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print string representation of an instance
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances
        Usage: all [class name]
        """
        args = shlex.split(arg)
        objects = storage.all()
        obj_list = []
        if not arg:
            for obj in objects.values():
                obj_list.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            for key, obj in objects.items():
                if key.startswith(class_name + "."):
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        if attr_name in ['id', 'created_at', 'updated_at']:
            return
        obj = objects[key]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except (ValueError, TypeError):
                pass
        else:
            try:
                attr_value = int(attr_value)
            except ValueError:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
