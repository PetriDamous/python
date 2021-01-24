### Zipping ###

num_str = '1234'
nums = nums = [1,2,3,4] 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

letters_nums = zip(nums, letters)

# letters_nums is a zip object
print(letters_nums) # <zip object at 0x00000170642F02C0>

# We can change letters_nums into a list so we can read it
letters_nums = list(zip(nums, letters))

# We get a list of tuples with the matching items per index inside of the tuples
print(letters_nums) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Note: zip works on any iterable including strings

str_letters = list(zip(num_str, letters))

print(str_letters) # [('1', 'a'), ('2', 'b'), ('3', 'c'), ('4', 'd')]

### We can also turn the zip object into a dictionary ###
# This comes in handy when we want a dictionary

dict_str_letters = dict(zip(letters, num_str))

print(dict_str_letters) # {'a': '1', 'b': '2', 'c': '3', 'd': '4'}

### We can also zip multiple iterables ###
combo_itr = list(zip(num_str, names, letters))

print(combo_itr) # [('1', 'John', 'a'), ('2', 'Eric', 'b'), ('3', 'Michael', 'c'), ('4', 'Graham', 'd')]

### Unzipping ###

# Unzipping is basically unpacking like in JS
# We unzip/unpack each iterable into a variable

nums = [1,2,3,4] 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

combo = list(zip(nums, letters, names))

# Unpacking
num, let, nam = zip(*combo)

# We get our iterable items unpacked into their varibles
print(num) # (1, 2, 3, 4)
print(let) # ('a', 'b', 'c', 'd')
print(nam) # ('John', 'Eric', 'Michael', 'Graham')

# They are returned to us as tuples
# Of course we can turn them back there original iterale type if we want

print(list(num)) # [1, 2, 3, 4]
print(" ".join(list(let))) # a b c d
print(list(nam)) # ['John', 'Eric', 'Michael', 'Graham']

### Use full dictionary case use ###

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

en = keys.split()
sv = values.split()

en_sv_trans = dict(zip(en, sv))

print(en_sv_trans) # {'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}

### Dictionary comprehension ###

# Template for dictionary comprehension
# dict_variable = {key:value for (key,value) in dictonary.items()}

# https://www.datacamp.com/community/tutorials/python-dictionary-comprehension

# Reminds me of using .reduce() in JS to create and manipulate objects

# Differnt way of doing above 

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

en = keys.split()
sv = values.split()

trans = {key:value for key, value in zip(en, sv)}

print(trans) # {'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}

# Other example of dictionary comprehention (this one doesn't use zip)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# *2 will multiply the values in the dictionary by 2
double_dict = {key:value * 2 for key, value in dict1.items()}

print(double_dict) # {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

# Unpacking dict way 1
my_dict = {'a':1, 'b':2, 'c':3}

keys, values = list(my_dict.keys()), list(my_dict.values())

print(keys) # ['a', 'b', 'c']
print(values) # [1, 2, 3]

#Unpacking dict way 2 with zip()
my_dict = {'a':1, 'b':2, 'c':3}

keys, values = zip(*my_dict.items())

keys = list(keys)
values = list(values)

print(keys) # ['a', 'b', 'c']
print(values) # [1, 2, 3]