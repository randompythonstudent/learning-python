import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\mbox-short.txt")
source_file = open(file_path)
count = 0
for line in source_file:
    if line.startswith('From '):
        words = line.split()
        count = count + 1
        print(words[1])
print(count)



