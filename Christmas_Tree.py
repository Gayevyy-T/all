
#for x in range(10):
#    for y in range(x, 10):
#        print(y, end=" ")
#    print()

for i in range(1,20,2):
    print(('*'*i).center(20))

for leg in range(3):
    print(('||').center(20))

print(('\====/').center(20))
#=======================================
for x in range(1, 20, 2):
    print(('*'*x).center(100))
for l in range(3):
    print(('||').center(100))
print(('======').center(100))
#=======================================
n = int(input("how big?"))
for i in range(n):
    for j in range(n-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()
#=======================================    
for x in range(20):
    z=' * '*x
    print(z.center(100))
print('| |'.center(100))
#==========opposite_tree=================
for x in range(20,0,-1):
    z=' * '*x
    print(z.center(100))
print('| |'.center(100))
#=======================================
def triangleShape(n):
    for i in range(n):
        for j in range(n-i):
            print('!', end=' ')
        for k in range(2*i+1):
            print('*',end=' ')
        print()

def poleShape(n):
    for i in range(n):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')

# Input and Function Call
row = int(input('Enter number of rows: '))

triangleShape(row)
triangleShape(row)
poleShape(row)