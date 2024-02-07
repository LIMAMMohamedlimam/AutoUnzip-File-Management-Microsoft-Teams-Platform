import time
from HandlerClass import DownloadEventHandler
from watchdog.observers import Observer

def start_monitoring(path):
    event_handler = DownloadEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

