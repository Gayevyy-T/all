largest = None
smallest = None
number = 0
while True:
    num = input("Enter a number: ")    
    if num == "done" : 
        break
    try:
        x = int(num)
    except:
        print('Invalid input')    
        continue
    if smallest is None:
        smallest = x
    elif smallest > x:
        smallest = x
    if largest is None:
        largest = x
    elif largest < x:
        largest = x
#    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)