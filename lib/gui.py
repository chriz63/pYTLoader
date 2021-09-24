from tkinter import *
from lib.utils import Utils

class Gui(Utils):

    tk = Tk()

    def __init__(self):
        print("Initializing pYTLoader...")
        self.tk.title("pYTLoader")
        self.tk.geometry("400x400")
        self.tk.resizable(False, False)

        self.create_menu()
        self.create_listbox()
        self.create_buttons_entry()
        self.create_entry_url()
        self.create_buttons_download()

        self.clear()

    def create_menu(self):
        print("create_menu")
        self.menubar = Menu(self.tk)

        self.menu_file = Menu(self.menubar, tearoff=0)
        self.menu_info = Menu(self.menubar, tearoff=0)

        self.menu_file.add_command(label="Speicherort wählen")
        self.menu_file.add_command(label="Speicherort öffnen")
        self.menu_file.add_command(label="Beenden", command=self.quit)

        self.menu_info.add_command(label="Info")

        self.menubar.add_cascade(label="Datei", menu=self.menu_file)
        self.menubar.add_cascade(label="Info", menu=self.menu_info)

    def create_listbox(self):
        print("create_listbox")
        self.frame_listbox = Frame(self.tk)
        self.scrollbar_listbox = Scrollbar(self.frame_listbox, orient=VERTICAL)
        self.listbox_url = Listbox(self.frame_listbox, width=50, yscrollcommand=self.scrollbar_listbox.set)

        self.scrollbar_listbox.config(command=self.listbox_url.yview)

        self.scrollbar_listbox.pack(side=RIGHT, fill=Y)
        self.listbox_url.pack(pady=15)
        self.frame_listbox.pack(side=TOP)

    def create_buttons_entry(self):
        print("create_buttons_entry")
        self.frame_buttons_entry = Frame(self.tk)
        self.button_add = Button(self.frame_buttons_entry, text="Hinzufügen", command=lambda: self.insert_to_listbox(self.entry_url.get()))
        self.button_del = Button(self.frame_buttons_entry, text="Löschen", command=lambda: self.remove_from_listbox())
        self.button_add.grid(row=0, column=0)
        self.button_del.grid(row=0, column=1)

        self.frame_buttons_entry.pack()

    def create_entry_url(self):
        print("create_entry_url")
        self.frame_entry_url = Frame(self.tk)

        self.entry_url = Entry(self.frame_entry_url, width=60)
        self.entry_url.pack()

        Label(self.frame_entry_url, text="Was soll heruntergeladen werden?").pack()

        self.frame_entry_url.pack()

    def create_buttons_download(self):
        print("create_buttons_download")
        self.frame_buttons_download = Frame(self.tk)

        self.button_download_audio = Button(self.frame_buttons_download, text="Audio")
        self.button_download_video = Button(self.frame_buttons_download, text="Video")
        self.button_download_audio.grid(row=1, column=0)
        self.button_download_video.grid(row=1, column=1)

        self.frame_buttons_download.pack()

    def insert_to_listbox(self, url):
        url_length = len(self.entry_url.get())
        if url_length > 0:
            print("insert_to_listbox")
            self.listbox_url.insert(END, url)

    def remove_from_listbox(self):
        for i in self.listbox_url.curselection():
            print("remove_from_listbox")
            self.listbox_url.delete(i)


    def mainloop(self):
        print("mainloop")
        self.tk.config(menu=self.menubar)
        self.tk.mainloop()

    def quit(self):
        print("quit")
        self.tk.quit()