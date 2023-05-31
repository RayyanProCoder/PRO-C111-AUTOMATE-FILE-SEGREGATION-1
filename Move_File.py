import os
import shutil

from_dir = "Downloads"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    file_path = os.path.join(from_dir, file_name)
    if os.path.isfile(file_path):
        name, extension = os.path.splitext(file_name)
        print("File Name:", name)
        print("File Extension:", extension)
        destination = os.path.join(to_dir, file_name)
        shutil.move(file_path, destination)