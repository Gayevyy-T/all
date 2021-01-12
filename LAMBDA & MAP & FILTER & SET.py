#===========Lambda================
def echo_word(word1, echo):
    words = word1 * echo
    return words
echo_word('hey', 5)

'''is the same'''
 echo_word = (lambda word1, echo: word1 * echo)
result = echo_word('hey', 5)
print(result)

'''another ex. - lambda inside function'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) # == 11*2 --> 22
print(mytripler(11)) # == 11*3 --> 33

'''another ex'''
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
  
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) #[5, 7, 9]

#============MAP=====================
#The map() function in Python takes in a function and a list.
# will use all element from the 'my_list'
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)#[2, 10, 8, 12, 16, 22, 6, 24]

'''another ex.'''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
y = map(str,my_list )  #conver to list of str --> ['1', '5', '4', '6', '8', '11', '3', '12']
y = ''.join(map(str, my_list))#create 'str' from list --> '1546811312'

'''another ex.'''
l = ['sat', 'bat', 'cat', 'mat'] 
  
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) #[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]

#==============Filter===============
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)#[4, 6, 8, 12]



#============SET================
# empty set
print(set())        #set()
# from string
print(set('Python'))        #{'P', 'o', 't', 'n', 'y', 'h'}
# from tuple
print(set(('a', 'e', 'i', 'o', 'u')))       #{'a', 'o', 'e', 'u', 'i'}
# from list
print(set(['a', 'e', 'i', 'o', 'u']))       #{'a', 'o', 'e', 'u', 'i'}
# from range
print(set(range(5)))        #{0, 1, 2, 3, 4}
# from set
print(set({'a', 'e', 'i', 'o', 'u'}))       #{'a', 'o', 'i', 'e', 'u'}
# from dictionary
print(set({'a':1, 'e': 2, 'i':3, 'o':4, 'u':5}))       #{'a', 'o', 'i', 'e', 'u'}
# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print(set(frozen_set))       #{'a', 'o', 'i', 'e', 'u'}
