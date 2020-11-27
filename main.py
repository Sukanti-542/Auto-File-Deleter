import os
import pathlib
from datetime import datetime

# Enter directory path from where the files/folders should to be deleted
directory_path = "PATH"  
# Enter the number of days beyond which the files/folders should to be deleted
threshold_days = 30  

all_file = []
all_folder = []


# We are using pathlib.Path().rglob('*') to recursively fetch the files/folders
# We can also use glob.iglob() but it doesn't detect hidden files/folders and also files/folders starting with .
for file in pathlib.Path(directory_path).rglob('*'):
    x = datetime.today()
    file_mtime = datetime.fromtimestamp(os.path.getmtime(file))
    time_diff = int((x - file_mtime).total_seconds() / (60 * 60 * 24))
    if time_diff >= threshold_days and os.path.isfile(file):
        all_file.append({'fileName': os.path.basename(file), 'filePath': file,
                         'modifiedDate': os.path.basename(
                             datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d'))})
    elif time_diff >= threshold_days:
        all_folder.append({'folderName': os.path.basename(file), 'folderPath': file,
                           'modifiedDate': os.path.basename(
                               datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d'))})

print(all_file)
print(all_folder)

confirm = input("Do you want to delete these files yes or no: ")
if confirm == "yes":
    for files in all_file:
        os.remove(files['filePath'])
    all_folder.reverse()
    for folder in all_folder:
        print(folder)
        if len(os.listdir(folder['folderPath'])) == 0:
            os.rmdir(folder['folderPath'])
