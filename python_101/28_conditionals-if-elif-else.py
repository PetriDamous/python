is_raining = True
is_cold = True

# print("Good Morning")

if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Shirt is fine!")

# and Truthy examples
print(True and True) # True

print (1 and 2) # 2

print(True and 1) # 1

# and Falsey examples

print(False and False) # False

print(1 and False) # False

print(True and False) # False

print(0 and 1) # 0

print(2 and 0) # 0

print(False and 0) # False

# advanced and examples
print(1 and False and True) # False

print (True and 2 and 1) # 1

print(0 and (True and True)) # 0

print((0 and True) and True) # 0

print((1 and 2) and True) # True

# or operator is the oposite of the and operator

# not() operator 
# reverses the result, returns false if the result is true

print(not(0)) # True

print(not(1)) # False

print(False and not(0)) # False

print(True or not(1)) # True
