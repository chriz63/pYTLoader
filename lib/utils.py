from os import system as ossystem
from platform import system as plsystem

class Utils(object):

    def get_os(self):
        return plsystem()

    def clear(self):
        if self.get_os() == "Windows":
            ossystem("cls")
        else:
            ossystem("clear")