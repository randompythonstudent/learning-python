import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\mbox-short.txt")
source_file = open(file_path)
counts = dict()
for line in source_file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in counts:
            counts[words[2]] = 1
        else:
            counts[words[2]] += 1
print(counts)