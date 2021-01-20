#!/usr/bin/env python3

def fib():
    l=[]
    for x in range(11):
        if x == 0:
            print(x)
            l.append(x)
        elif x == 1:
            print(x)
            l.append(x)
        else:
            l.append(l[x-1]+l[x-2])
    print(l)
            
    

    
    
    
fib()
    