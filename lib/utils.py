from os import startfile
from os import system as ossystem
from platform import system as plsystem
from tkinter import messagebox, filedialog#
from io import StringIO

class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Append(self, str):
        self._file_str.write(str)

    def __str__(self):
        return self._file_str.getvalue()

class Utils(object):

    dirname = None

    def select_directory(self):
        self.dirname = filedialog.askdirectory()

    def open_directory(self):
        if self.dirname is not None:
            if self.get_os() == "Windows":
                startfile(self.dirname)
            elif self.get_os() == "Linux":
                ossystem('open "%s"' % self.dirname)
        else:
            messagebox.showerror("Error", "Kein Download Ordner gewählt!")

    def get_os(self):
        return plsystem()

    def clear(self):
        if self.get_os() == "Windows":
            ossystem("cls")
        elif self.get_os() == "Linux" or self.get_os() == "Darwin":
            ossystem("clear")
