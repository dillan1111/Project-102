#program to list contents and folders of a folder
import os

root = os.path.join('C:\\Users\\test\\Downloads')
print(root)
for directory, subdir_list, file_list in os.walk(root):
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)
    print()