from tkinter import *

from lib.yt import Yt
from lib.components import Components

# TODO: check on init if FFmpeg is installed if not install it in path

class Gui(Components, Yt):
    def __init__(self):
        super(Gui, self).__init__()

        # Init GUI
        self.tk.title("pYTLoader")
        self.tk.geometry("400x400")
        self.tk.eval('tk::PlaceWindow . center')
        self.tk.resizable(False, False)

        # Init Components
        self.frame_menubar.pack()
        self.frame_listbox.pack()
        self.frame_buttons_entry.pack()
        self.frame_entry_url.pack()
        self.frame_buttons_download.pack()
        self.frame_progressbar.pack()

        self.mainloop()
