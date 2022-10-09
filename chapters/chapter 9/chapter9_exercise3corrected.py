import sys
import os
max_val = None
max_key = None
parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\mbox-short.txt")
source_file = None
counts = dict()
try:
    source_file = open(file_path)
except:
    print('File cannot be opened:', source_file)
    sys.exit()

for line in source_file:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    else:
        if words[1] not in counts:
            counts[words[1]] = 1  
        else:
            counts[words[1]] += 1     
            
for key, value in counts.items():
    if max_val is None or value > max_val:
        max_val = value
        max_key = key
        
print('Maximum: ', max_key, max_val)
