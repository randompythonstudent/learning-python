import os
import string
counts = 0
d = dict()
r = list()
parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\romeo-full.txt")
source_file = open(file_path)

for line in source_file:
    line = line.translate(str.maketrans('','', string.digits))
    line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
for key, val in list(d.items()):
    r.append((val / counts, key))
r.sort(reverse=True)
for key, val in r:
    print(key, val)