def factorial(n):
    if n < 2:
        return 1
    return n + factorial(n-1)
print(factorial(5))


def fact(n):
    if len(n) < 1:
        return []   #base case
#    if len(n) == 1:
#        return n   #base case
    else:
        return [n.pop()] + fact(n)
        
print(fact([1,2,3,4,5]))