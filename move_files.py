import os
import shutil

from_dir='C:/Users/golea/Downloads'

to_dir='C:/Users/golea/Desktop/Project111'

list_of_files=os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name,extension=os.path.splitext(i)
    print(name,extension)