import os
file_path = '/users/ceo/downloads/jdk-19_linux-x64_bin.rpm'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has been successfully been deleted")
else:
    print("This file does NOT exist")