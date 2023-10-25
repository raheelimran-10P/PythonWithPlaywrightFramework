import os

class DownloadsPathFinder:
    def __init__(self, username=None):
        self.username = username if username else os.getlogin()
        self.downloads_path = os.path.join("C:\\Users", self.username, "Downloads")

    def get_downloads_path(self):
        if os.path.exists(self.downloads_path):
            return self.downloads_path
        else:
            return None