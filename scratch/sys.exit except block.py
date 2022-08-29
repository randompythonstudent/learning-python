import sys
import os
parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\romeo.tx")

try:
    source_file = open(file_path)
except:
    print('File cannot be opened:')
    sys.exit()

counts = dict()
for line in source_file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)