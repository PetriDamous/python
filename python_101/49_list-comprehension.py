### # give me a list with num squared for each num in numbers ###

numbers = [1,2,3,4,5,6,7,8,9]

new_list = []

for num in numbers:
    new_list.append(num*num)

print(new_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# We can rewrite this as a list comprehension

new_list = [num*num for num in numbers]

print(new_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

### give me a list with num for each num in numbers if num is even ###

numbers = [1,2,3,4,5,6,7,8,9]

new_list = []

# for loop way
for num in numbers:
    if num % 2 == 0:
        new_list.append(num)

print(new_list) # [2, 4, 6, 8]

# list comprehension way
new_list = [num for num in numbers if num % 2 == 0]

print(new_list) # [2, 4, 6, 8]

# filter() function way

# filter() syntax: filter(function, iterable)

new_list = filter(lambda num: num % 2 == 0, numbers)

# Returns a filter object
print(new_list) # <filter object at 0x00000282FD2A0FA0>

print(list(new_list)) # [2, 4, 6, 8]

### I want a (letter, num) pair for each letter in 'spam' and each number in '0123' ###

new_list = []

for letter in 'spam':
    for num in range(4):
        new_list.append({letter, num})

print(new_list) # [('s', 0), ('s', 1), ('s', 2), ('s', 3), ('p', 0), ('p', 1), ('p', 2), ('p', 3), ('a', 0), ('a', 1), ('a', 2), ('a', 3), ('m', 0), ('m', 1), ('m', 2), ('m', 3)]

new_list = [(letter,num) for letter in 'spam' for num in range(4)]

print(new_list)