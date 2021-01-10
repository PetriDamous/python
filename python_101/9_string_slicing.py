#String functions

#Capitalize all letters in string
msg_lower = "welcome to Python 101: Strings"

print(msg_lower.upper()) # WELCOME TO PYTHON 101: STRINGS

#Lower case all letters in string
msg_upper = "WELCOME TO PYTHON 101: STRINGS"

print(msg_upper.lower()) # welcome to python 101: strings 

#Captilize and Title
msg = 'welcome to it\'s Python 101: Strings'

#Captilize
print(msg.capitalize()) # Welcome to it's python 101: strings

#Title
print(msg.title()) # Welcome To It'S Python 101: Strings

#len() and count
msg = "welcome to Python 101: Strings"

#len()
print(len(msg)) #30 characters long

#.count()
print(msg.count('python')) # 0 because it is case sensitive
print(msg.count('o')) # o occurs three times

#Slicing strings
msg = "I like turtles"

print(msg[2]) # l
print(msg[3:]) # ike turtles (inclusive so i is included much like JS .slice() method)
print(msg[3:8]) # ike t (second value after : is exclusive so u is not included much like JS .slice() method)
print(msg[:8]) # I like t

#.index()
msg = "I like turtles"

print(msg.index("like")) # 2
print(msg.index("t")) # 7
print(msg[8:].index("t")) # 2 because we are using the sub string "urtles"