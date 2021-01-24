# def multi(a, b):
#     return a * b

# print(multi(2, 3))

# def multi(a,b): return a * b

# Used like anonymous functions in JS
# lambda functions can be stored in varibles and called on later on

### lambda function as named function ###
multi = lambda x,y: x * y

print(multi(2, 3)) # 6

### lambda function as anonymous fuction ###

names = ["petri williams", "nu type", "akky king", "barry burton"]

# Sorts by last name using lambda function
names.sort(key = lambda name: name.split()[-1])

print(names) # ['barry burton', 'akky king', 'nu type', 'petri williams']

### function call with key value in sort() method ###

# Sorts by first name using function declaration as key value
def sort_first(name):
    return name.split()

names.sort(key=sort_first)

print(names) # ['akky king', 'barry burton', 'nu type', 'petri williams']

