from watchdog.events import FileSystemEventHandler
import zipfile as zp  , os


def extract_zip(zip_file, destination_folder):
     # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Open the ZIP file
    with zp.ZipFile(zip_file, 'r') as zip_ref:
        # Extract all files
        zip_ref.extractall(destination_folder)

class DownloadEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the added file is a zip file
        if event.is_directory or not event.src_path.endswith('.zip'):
            return "not zip file"
        
        print(f"Detected new zip file: {event.src_path}")
        # Define your target directory
        
        # Call your function to process the new zip file
        extract_zip(event.src_path,'/home/mohamed/test_automation')

