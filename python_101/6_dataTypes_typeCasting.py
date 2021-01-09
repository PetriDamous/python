#Basic data types

print(type("dog")) # <class 'str'>

print(type(1)) # <class 'int'>  

print(type(2.5)) # <class 'float'>

print(type(True)) # <class 'bool'> 

#double and single quotes work the same as JS
#esaping works the same as in JS

#Type Casting

#Unlike JS there is no automatic typecast
#You have to manually typecast yourself

money = 5

print("I got " + str(money) + " on it!!")

#without the str() for casting the int into a str we would get an error

#Type Casting Examples

a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
#c1 = int("3.4")   # c1 will be an error. Follow c2 for correct type casting
c2 = int(float("3.4")) # c2 will be 3
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a, b, c, c2, d, e, f, g, h, i, j])