import os , zipfile as zp


def extract_zip(zip_file, destination_folder):
     # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Open the ZIP file
    with zp.ZipFile(zip_file, 'r') as zip_ref:
        # Extract all files
        zip_ref.extractall(destination_folder)


