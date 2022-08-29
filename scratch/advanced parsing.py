import string

import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\romeo-full.txt")
source_file = open(file_path)

counts = dict()
for line in source_file:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
print(counts['juliet'])