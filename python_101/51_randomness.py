import random, string 
from random import random, uniform, randint, randrange, choice, choices, sample, shuffle
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

############### Working with Numbers #########################

### random() function ###
# genrates a random number from 0 and up to 1 but does not include 1

# print(random())

### Generating 4 random numbers with for loop and range ###

# for i in range(4):
#     print(random())

### Generating number up to certian number ###
# Simply mulitply by the number you wish to go up to

# print(random() * 6) # Goes up to 6 but will not include 6

### uniform() function ###
# Allows us to specify a range we want our random number to be in

# Random number between 1 and 6
# print(uniform(1, 6))

### randint() function ###
# Same as uniform but returns a randomn integer within the given range

# Random integer between 1 and 6
# print(randint(1, 6))

### randrange() function ###
# allows you to choose a random range like randint but 
# has a third argument that allows you to specify a step like range()

# print(randrange(1, 100, 2))

################ Randomness with iterables ###########################

### choice() function ###
# allows us to pick a random item from an iterable
# Note: look into choices on w3schools

animals = ["dog", "cat", "monkey", "bird"]

# print(choice(animals))

### sample() function ###
# Allows you to draw more than one item from iterable
# First argument is the iterable 
# Second argument is how many random items we want from the iterable

animals = ["dog", "cat", "monkey", "bird", "dog", "cat"]

# print(sample(animals, 3))

### shuffle() function ###
# shuffles items in a list
# shuffles in place so you have to run it before you print it

# shuffle(animals) 

# print(animals)

################## Working with strings #################################

# Have to import the string module 

# ascii_letters, ascii_lowercase, ascii_uppercase, digits are attributes from the string module

# ascii_letters gives us all the letters in the alphabet lower and upper case
# ascii_lowercase only lower case letters
# ascii_uppercase only upper case letters
# digits all the numbers 0 - 9

# print(ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
# print(ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(digits) # 0123456789

### Generating Random string of numbes and letters ###

# Creates a strig of all upper and lower case letters and numbers 0 - 9
lets_nums = ascii_letters + digits
word = ''

# Loop way with choice()
for i in range(7):
    word += choice(lets_nums)

print(word)

# .join() way with sample
# sample() used on a string will split the string into a list

# print(sample(lets_nums, 7))

word = ''.join(sample(lets_nums, 7))

print(word)

# chocies() way

word = ''.join(choices(lets_nums, k=7))

print(word)