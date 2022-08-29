import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\mbox-short.txt")
source_file = open(file_path)
counts = dict()
try:
    source_file = open(file_path)
except:
    print('File cannot be opened:', source_file)
    exit()

for line in source_file:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in counts:
            counts[words[1]] = 1  # First entry
        else:
            counts[words[1]] += 1     # Additional counts
print(counts)