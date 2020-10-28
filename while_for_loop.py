while True:
    line = input('Please type the input: ')
#    if line[0] == '#':
#        continue
    if line == 'done':
        break
    print(line)
print('Done!')
#===========================
n = 5
while n > 0:
    print(n)
    n = n - 1
print('finish')
#===========================
#--------for_loop----------------
x = open('tekst.txt')
for line in x:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)    