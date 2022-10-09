import sys
import os
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
lst = list()
for email, count in list(counts.items()):
    lst.append((count, email))
lst.sort(reverse=True)
# for count, email in lst[:]:
#     print(count, email)
print(lst[0])
#remove_me