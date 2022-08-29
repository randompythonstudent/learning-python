import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\words.txt")
source_file = open(file_path)

source = source_file.read()
t = dict()
t = source
print(t)