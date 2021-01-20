re1 = ["chris", "barry", "jill", "wesker"]

#Ways without enumerate() function

# 1 
# for idx in range(len(re1)):
#     print(f"{idx}: {re1[idx]}")

# We get the index and access to items we wish to enumerate over
# but we have limited control.

# We cannot for example control where we want our iteration number
# to start.

# 2
# i = 2

# for char in re1:
#     print(f"{i}: {char}")
#     i += 1

# Close to the enumerate() function.
# We are using a varible.

# enumerate() function way
# for enum, char in enumerate(re1, 2):
#     print(f"{enum}: {char}")

# Cleaner way of implementing a interation number

# Loop must provide two params:
# 1 - Iteration number
# 2 - item we are iterating over

# enumerate() function
# Can take two arguments:
# 1 - What we want to enumerate over.
# 2 - Starting iteration number (optional, default is zero if not provided)

# Behind the sense enumerate() will turn each iterable item into a tuple
# pairing the iteration number and iterable item together

# Ex: re1 = ["chris", "barry", "jill", "wesker"] gets turned into
# re1 = [(2, "chris"), (3, "barry"), (4, "jill"), (5, "wesker")]
# when enumerate(re1, 2) is ran

re1 = ["chris", "barry", "jill", "wesker"]

# enumerate() is its own class/object/data type
# print(type(enumerate(re1))) # <class 'enumerate'>

# #object in memory
# print(enumerate(re1)) # <enumerate object at 0x000002800180A880>

# # We can turn the enumrate object into a list object
# print(list(enumerate(re1))) # [(0, 'chris'), (1, 'barry'), (2, 'jill'), (3, 'wesker')]

# Knowing this we can modify a variable and or put a counter on the variable

# Advance examples

re2 = ["leon", "claire", "sherri", "william"]

# for enum, char in enumerate(re2, 34):
#     print(enum)
#     print(char)
#     print(enum, char)

# 34
# leon     
# 34 leon  
# 35       
# claire   
# 35 claire
# 36       
# sherri   
# 36 sherri
# 37       
# william
# 37 william

# Negative number example

# for enum, char in enumerate(re2, -2):
#     print(enum, char)

# -2 leon  
# -1 claire
# 0 sherri 
# 1 william

# Nested enumerate 

# for enum, char in enumerate(enumerate(re2, 1), -100):
#     print(enum)
#     print(char)
#     print(char[0])
#     print(char[1])
#     print(enum, char)

# print(type(enumerate(enumerate(re2, 1), -100)))

# enumerate() works great on ordered iterables such as:
# 1. strings
# 2. tuples
#3. lists

# does not work so great on un ordered iterables such as:
# 1. dictionaries
# 2. sets

# enumerate on strings

# When using start value iteration number will start at
#specified value

for enum, letter in enumerate("python", start = 5):
    print(enum, letter)
