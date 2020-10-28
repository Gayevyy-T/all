#hrs = input("Enter Hours: ")
#h = float(hrs)
#if h <= 40:
#    h = h * 10.5
#else:
#    h = ((h - 40) * (10.5 * 1.5)) + 420
#print(h)
#======================================
def computepay(h,r):
    if h <= 40:
        h = h * r
    else:
        h = ((h - 40) * (r * 1.5)) + 420
    return h

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

p = computepay(h,r)
print("Pay",p)