import os
import youtube_dl
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from os import startfile, system
from threading import Thread

from lib.utils import Utils

class Logger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

class Gui(Utils):

    tk = Tk()

    status = ''
    percentage = 0
    downloadtype = IntVar()
    dirname = None

    def __init__(self):
        super().__init__()
        print("Initializing pYTLoader...")
        self.tk.title("pYTLoader")
        self.tk.geometry("400x400")
        self.tk.resizable(False, False)

        self.create_menu()
        self.create_listbox()
        self.create_buttons_entry()
        self.create_entry_url()
        self.create_buttons_download()
        self.create_progressbar()

        self.clear()

    def create_menu(self):
        print("create_menu")
        self.menubar = Menu(self.tk)

        self.menu_file = Menu(self.menubar, tearoff=0)
        self.menu_info = Menu(self.menubar, tearoff=0)

        self.menu_file.add_command(label="Speicherort wählen", command=self.select_directory)
        self.menu_file.add_command(label="Speicherort öffnen", command=self.open_directory)
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

        self.button_select_audio = Radiobutton(self.frame_buttons_download, text="Audio", variable=self.downloadtype, value=1)
        self.button_select_video = Radiobutton(self.frame_buttons_download, text="Video", variable=self.downloadtype, value=2)
        self.button_select_audio.grid(row=1, column=0)
        self.button_select_video.grid(row=1, column=1)

        self.frame_buttons_download.pack()

    def create_progressbar(self):
        print("create_progressbar")
        self.frame_progressbar = Frame(self.tk)
        self.button_download = Button(self.frame_progressbar, text="Start Download", command=self.testDownload).pack()
        self.progress_bar = Progressbar(self.frame_progressbar, orient=HORIZONTAL, length=350, mode="determinate")

        self.progress_bar.pack()
        self.frame_progressbar.pack()

    def insert_to_listbox(self, url):
        url_length = len(self.entry_url.get())
        if url_length > 0:
            print("insert_to_listbox")
            self.listbox_url.insert(END, url)
        self.entry_url.delete(0, END)

    def remove_from_listbox(self):
        for i in self.listbox_url.curselection():
            print("remove_from_listbox")
            self.listbox_url.delete(i)

    '''
    Testing Function
    '''
    def testDownload(self):
        print("testDownload")
        print(self.downloadtype.get())
        #download_thread = Thread(self.download(downloadtype=self.get_download_type(), savepath=self.dirname, url="https://www.youtube.com/watch?v=AsGGH_iI5p8"))
        self.download(downloadtype=self.get_download_type(), savepath=self.dirname, url="https://www.youtube.com/watch?v=g7yIGvlnU2c")

    '''
    Testing Function
    '''
    def testProgBar(self):
        from time import sleep
        percentage = 0
        for i in range(6):
            print("i " + str(i) + " percentage " + str(percentage))
            self.progress_bar['value'] = percentage
            self.tk.update_idletasks()
            percentage = percentage + 20
            sleep(1)

    def get_download_type(self):
        if self.downloadtype.get() == 1:
            return "audio"
        elif self.downloadtype.get() == 2:
            return "video"

    def select_directory(self):
        self.dirname = filedialog.askdirectory()

    def open_directory(self):
        if self.dirname is not None:
            if self.get_os() == "Windows":
                os.startfile(self.dirname)
            elif self.get_os() == "Linux":
                os.system('open "%s"' % self.dirname)

    def download(self, downloadtype, savepath, url):
        ytdl_options = {
            'format': 'bestaudio/best',
            'outtmpl': savepath + '/' + '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'logger': Logger(),
            'progress_hooks': [self.hook]
        }

        uri = [url]

        if downloadtype == "audio":

            with youtube_dl.YoutubeDL(ytdl_options) as ydl:
                print("!!!")
                thread = Thread(target=ydl.download, args=(uri,))
                thread.start()
                print(":)")

        elif downloadtype == "video":

            ytdl_options['format'] = 'bestvideo+bestaudio'
            del ytdl_options['postprocessors']

            with youtube_dl.YoutubeDL(ytdl_options) as ydl:
                print("!!!")
                thread = Thread(target=ydl.download, args=(uri,))
                thread.start()
                print(":)")

    def hook(self, download):
        if download['status'] == 'downloading':
            self.status = download['status']
            self.percentage = download['_percent_str'].replace('%', ' ')
            self.progress_bar['value'] = self.percentage

    def mainloop(self):
        print("mainloop")
        self.tk.config(menu=self.menubar)
        self.tk.mainloop()

    def quit(self):
        print("quit")
        self.tk.quit()