a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity

#idenity operator (is)
a = [1, 2, 3]
b = a # a and b now share the same space in memory. Object is passed by reference to the other variable

print(a == b) # True 

print(a is b) # True (checks to see if object has same space in memory)

print(id(a), id(b)) # 2615233064128 2615233064128 (id() returns id in memory of object)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True (unlike JS, equality will be True if values in object are the same)

print(a is b) # False

print(id(a), id(b)) # 2071785486336 2071785433664

#Boolean conversions
print(int(True)) # 1

print(int(False)) # 0

print(bool("dog")) # True

print(bool(" ")) # True

print(bool("")) # False

print(bool(42)) # True

print(bool(1)) # True

print(bool(0)) # False

# Adding booleans to numbers

print(42 + True) # 43

print(42 + False) # 42

