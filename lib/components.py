from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from os import startfile, system

from lib.utils import StringBuilder
from lib.yt import Yt


class Components(Yt):

    # Create object of Tk
    tk = Tk()
    url_list = []

    def __init__(self):
        # Some Variables
        self.downloadtype = IntVar()

        # Create the Frames
        self.frame_menubar = Frame(self.tk)
        self.frame_listbox = Frame(self.tk)
        self.frame_buttons_entry = Frame(self.tk)
        self.frame_entry_url = Frame(self.tk)
        self.frame_buttons_download = Frame(self.tk)
        self.frame_progressbar = Frame(self.tk)

        # Add Menu to frame_menubar
        self.menubar = Menu(self.tk)

        # Deactivate ugly ---- (tearoff) in the Menus
        self.menu_file = Menu(self.menubar, tearoff=0)
        self.menu_info = Menu(self.menubar, tearoff=0)

        # Create the Listbox with its Scrollbar and add to frame_listbox
        self.scrollbar = Scrollbar(self.frame_listbox, orient=VERTICAL)
        self.listbox = Listbox(self.frame_listbox, width=50, selectmode="multiple", yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(pady=15)

        # Create the Buttons to add or delete to/from Listbox and add to frame_buttons_entry
        self.button_add = Button(self.frame_buttons_entry, text="Hinzufügen", command=lambda: self.add_to_listbox(self.entry.get()))
        self.button_del = Button(self.frame_buttons_entry, text="Löschen", command=lambda: self.del_from_listbox())
        self.button_add.grid(row=0, column=0)
        self.button_del.grid(row=0, column=1)

        # Create the Entry field and add it to frame_entry_url
        self.entry = Entry(self.frame_entry_url, width=60)
        self.label = Label(self.frame_entry_url, text="Format")
        self.entry.pack()
        self.label.pack()

        # Create the Radiobuttons to select Download Format and add to frame_buttons_download
        self.button_audio = Radiobutton(self.frame_buttons_download, text="Audio", variable=self.downloadtype, value=1)
        self.button_video = Radiobutton(self.frame_buttons_download, text="Video", variable=self.downloadtype, value=2)
        self.button_audio.grid(row=1, column=0)
        self.button_video.grid(row=1, column=1)

        # Create the Progressbar to show the progress of Downloads, a Button to start/stop Download
        # and add to frame_progressbar
        self.button_download = Button(self.frame_progressbar, text="Download", command=lambda: self.download(self.downloadtype.get(), self.dirname, self.progressbar, self.get_listbox_data()))
        self.progressbar = Progressbar(self.frame_progressbar, orient=HORIZONTAL, length=350, mode="determinate")
        self.button_download.pack()
        self.progressbar.pack()

        # Add the MenuItems to the Menu
        ## Add to Menu_File
        self.menu_file.add_command(label="Speicherort wählen", command=self.select_directory)
        self.menu_file.add_command(label="Speicherort öffnen", command=self.open_directory)
        self.menu_file.add_command(label="Beenden", command=self.quit)
        self.menubar.add_cascade(label="Datei", menu=self.menu_file)
        self.menubar.add_cascade(label="Info", menu=self.menu_info)
        ## Add to Menu_Info
        self.menu_info.add_command(label="Info", command=self.show_infos)

    def show_infos(self):
        sb = StringBuilder()
        sb.Append("    Dieses Program wurde ausschließlich zum Lernen\n")
        sb.Append("und für private Nutzung programmiert, jegliche Nutzung\n")
        sb.Append("        unberechtigeter Personen ist untersagt.\n")
        messagebox.showinfo("Informationen", sb)

    # Return the URLs from Listbox as a List
    def get_listbox_data(self):
        for i in self.listbox.curselection():
            self.url_list.append(self.listbox.get(i))
        return self.url_list

    # Add URL from Entry to Listbox then clear the Entry
    def add_to_listbox(self, url):
        url_length = len(self.entry.get())
        if url_length > 0:
            self.listbox.insert(END, url)
            self.listbox.select_set(1, END)
        self.entry.delete(0, END)

    # Deletes selected URLs from the Listbox
    def del_from_listbox(self):
        for i in self.listbox.curselection():
            self.listbox.delete(i)

    def mainloop(self):
        self.tk.config(menu=self.menubar)
        self.tk.mainloop()

    def quit(self):
        self.tk.quit()
