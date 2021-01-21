my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'

# .sort() and sorted()

# print(my_list.sort()) # None (list sorts in place. None is returned because there is no return value)

# print(sorted(my_list)) # [1, 2, 3, 5, 7] (A new list is returned that is sorted.)

# print(id(my_list)) # 1760065330304 

# my_list.sort() # [1, 2, 3, 5, 7]

# print(id(my_list)) # 1760065330304 

# sorted_list = sorted(my_list)

# print(id(sorted_list)) # 1760065334208 (id is different from the above due to it being a new sorted object)

# print(my_list == sorted(my_list)) # True (==  checks if items are the same)

# print(my_list is sorted(my_list)) # False (is checks to see if objects are the same)


# .reverse()

# my_list.reverse()

# print(my_list) # [2, 7, 3, 5, 1]

# .sort(), reverse(), sorted() on tuples

# my_tuple = ('d','c','e','a','b')

# # .sort() .reverse() only work with lists
# # sorted() however works with tuples

# print(sorted(my_tuple))
# print(tuple(sorted(my_tuple)))

# .sort() .reverse() and sorted() on string

# .sort() and .reverse() do not work on strings because strings are imutable
# sorted() works on strings

# sorted() on a string will return a list
# if ou wish to have sorted string you have to convert it yourself

my_string = 'python'

# print(sorted(my_string)) # ['h', 'n', 'o', 'p', 't', 'y']

# sorted_string = "".join((sorted(my_string)))

# print(sorted_string)

# sorted() on dictinary

my_dict = {'car':4,'dog':2,'add':3,'bee':1}

print(my_dict.items()) # dict_items([('car', 4), ('dog', 2), ('add', 3), ('bee', 1)])

print(type(my_dict.items())) # <class 'dict_items'>

print(sorted(my_dict)) #['add', 'bee', 'car', 'dog']

print(sorted(my_dict.items())) # [('add', 3), ('bee', 1), ('car', 4), ('dog', 2)]

print(sorted(my_dict.values()))

print(sorted(my_dict.values(), reverse=True))

# reversed()
my_dict = {'car':4,'dog':2,'add':3,'bee':1}

print(reversed(my_dict)) # <dict_reversekeyiterator object at 0x000001E7EE246BD0>

print(tuple(reversed(my_dict))) # ('bee', 'add', 'dog', 'car')

# Reversing list with [::-1]

# only works on lists

num_list = [3, 2, 1]

print(num_list[::-1]) # [1, 2, 3]

# sorted and key value

# Sorting sub lists with sorted() and lambda fucntions

my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

print(sorted(my_llist, key = lambda item: item[1]))