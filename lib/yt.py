import youtube_dl
from threading import Thread
from tkinter import messagebox

from lib.utils import Utils

class Logger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

class Yt(Utils):

    progressbar = ""

    def __init__(self, tk):
        self.status = ""
        self.percentage = 0

    def hook(self, download):
        if download['status'] == 'downloading':
            self.status = download['status']
            self.percentage = download['_percent_str'].replace('%', ' ')
            self.progressbar['value'] = self.percentage

    def download(self, downloadtype, savepath, progressbar, url):
        self.progressbar = progressbar

        if savepath:
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

            if url:
                if downloadtype == 1:
                    with youtube_dl.YoutubeDL(ytdl_options) as ydl:
                        for i in url:
                            thread = Thread(target=ydl.download, args=(url,))
                            thread.start()

                elif downloadtype == 2:
                    ytdl_options['format'] = 'bestvideo+bestaudio'
                    del ytdl_options['postprocessors']
                    with youtube_dl.YoutubeDL(ytdl_options) as ydl:
                        for i in url:
                            thread = Thread(target=ydl.download, args=(url,))
                            thread.start()
                else:
                    messagebox.showerror("Error", "Bitte ein Format wählen.")
            else:
                messagebox.showerror("Error", "Bitte YouTube Links hinzufügen.")
        else:
            messagebox.showerror("Error", "Kein Download Ordner gewählt!\n     Bitte wähle diesen unter:\n\n\n -> Datei -> Speicherort wählen")
