import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\mbox-short.txt")
source_file = open(file_path)


for line in source_file:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])