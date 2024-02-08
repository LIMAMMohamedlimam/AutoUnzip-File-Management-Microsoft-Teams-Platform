from watchdog.events import FileSystemEventHandler
from threading import Timer
from Processingfunct import extract_zip



class DownloadEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.timer = None
        self.delay = 5

    def handle_file(self,path):
        if path.endswith('.zip'):
            print(f"Processing zip file: {path}")
            extract_zip(path, '/home/mohamed/test_automation')
        else:
            print("File is not a zip, ignoring.")


    def on_created(self, event):
        if event.is_directory:
            return 
        
        if self.timer is not None :
            self.timer.cancel()

        self.timer = Timer(self.delay , self.handle_file , [event.src_path])
        self.timer.start()