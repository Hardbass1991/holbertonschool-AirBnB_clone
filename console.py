#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
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

    def create(self):
        

def parse(arg):
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
