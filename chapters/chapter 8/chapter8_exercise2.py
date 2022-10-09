fname = open('mbox.txt')

for line in fname:
    if not line.startswith('From '): continue
    words = line.split()
    print(words[1])