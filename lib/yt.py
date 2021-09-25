class Logger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

class Yt(object):

    percentage = 0
    video_details = []

    def __init__(self):
        pass

    def hook(self, download):
        if download['status'] == 'downloading':
            self.percentage = download['_percent_str']
            self.percentage.replace('%', '')

    def download(self, downloadtype, url):
        ytdl_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'logger': Logger(),
            'progress_hooks': [self.hook()]
        }

    def get_video_details(self, url):
        pass
