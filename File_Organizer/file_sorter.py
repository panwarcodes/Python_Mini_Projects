# File Organizer by @panwarcodes/github
# Makes separate folders for each file type 
# and sorts out each file type to its folder
import os
import shutil

file_extension = input("Enter the file extension you want to sort (e.g., .txt, .jpg): ").lower()

# Extensions
# Popular file types - using tuple instead of list because
# .endswith() method doesn't work with lists.
Images = ('.jpg', '.png', '.jpeg', '.tiff', '.gif', '.webp')
Videos = ('.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv')
Documents = ('.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.odt')
Audio = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a')
Archives = ('.zip', '.tar', '.rar', '.7z', '.gz', '.bz2')
Code_Files = ('.py', '.js', '.html', '.css', '.java', '.cpp')

# --------------------------------------- START START START ----------------------------------
# Select folder where you want to sort files
path_to_folder = input("Enter the path of the folder containing files\neg. /path/to/your/destination_folder (dont add '/' at the end): ")
path_to_sendfiles_folder = input("Enter the destination folder path\neg. /path/to/your/destination_folder (dont add '/' at the end): ")
# --------------------------------------- END END END -------------------------------------

file_types = [Images, Videos, Documents, Audio, Archives, Code_Files]

# Find type of file and print them
def file_classifier():
    for file_type in file_types:
        if file_extension.endswith(file_type):
            if file_type == Images:
                return "Images"
            elif file_type == Videos:
                return "Videos"
            elif file_type == Documents:
                return "Documents"
            elif file_type == Audio:
                return "Audio"
            elif file_type == Archives:
                return "Archives"
            elif file_type == Code_Files:
                return "Code_Files"

# Get subfolder name from classifier
subfolder_name = file_classifier()
destination_folder = os.path.join(path_to_sendfiles_folder, subfolder_name)

# Create the subfolder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move files
for filename in os.listdir(path_to_folder):
    source_path = os.path.join(path_to_folder, filename)
    if filename.endswith(file_extension) and os.path.isfile(source_path):
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")