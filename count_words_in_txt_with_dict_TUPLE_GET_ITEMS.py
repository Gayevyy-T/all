name = input("Enter file:")
handle = open(name)
n_dict = {}

for line in handle:
    if line.startswith('From:'):
        line = line.strip().split()
        word = line[1]
        n_dict[word] = n_dict.get(word, 0) + 1        
#        if word not in n_dict:
#            n_dict[word] = 1
#        else:
#            n_dict[word] += 1
b_word = None
n_word = None
for k, v in n_dict.items():
    if n_word == None or v > n_word:
        b_word = k
        n_word = v
print(b_word, n_word)