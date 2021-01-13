set_1 = {"dog", "turtle", "cat", "rat", "rat"}

set_2 = {"cat", "moneky", "dog", "bird", "bird"}

# Duplicates are removed
print(set_1) # {'dog', 'rat', 'cat', 'turtle'}

print(set_2) # {'dog', 'bird', 'cat', 'moneky'}

# .intersection()
# finds items that are alike between two sets and returns a new set with those items

print(set_1.intersection(set_2)) # {'dog', 'cat'}

print(set_2.intersection(set_1)) # {'dog', 'cat'}

# .difference()
# finds items that do not exist between two sets and returns a new set with those items

print(set_2.difference(set_1)) # {'bird', 'moneky'}

print(set_1.difference(set_2)) # {'rat', 'turtle'} 

# .union()
# combines both sets together

print(set_1.union(set_2)) # {'moneky', 'dog', 'bird', 'cat', 'rat', 'turtle'}

print(set_2.union(set_1)) # {'moneky', 'dog', 'bird', 'cat', 'rat', 'turtle'}

# Creating empty lists lists, tuples, and sets

#Empty list

empty_list = []
empty_list = list()

#Empty tuple

empty_tuple = ()
empty_tuple = tuple()

#Empty set

empty_set = {} # will not create an empty set. Will create an empty dictionary instead
empty_set = set() # only way to create empty set. 