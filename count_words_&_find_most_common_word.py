name = input('Enter the file name: ')
handle = open(name, 'r')

#count word frequency
counts = {}
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
#print(counts, counts.keys(), counts.items())

#find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigcount, bigword)
