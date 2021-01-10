#Multi Line strings

msg = """Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""

# print(msg)

# .find() attribute

msg = 'Welcome to Python 101: Strings'

print(msg.find("Python")) # 11 (index of where substring starts)

# .replace()

msg = 'Welcome to Python 101: Strings'

print(msg.replace("Python", "Ruby")) # Welcome to Ruby 101: Strings

#Strings are immutable so you will either have to save to a new variable or reassign to same variable

msg_1 = msg.replace("Python", "Ruby")

msg = msg.replace("Python", "JavaScript")

print(msg_1) # Welcome to Ruby 101: Strings  

print(msg) # Welcome to JavaScript 101: Strings

#Membership

msg = "I like turtles"

print("turtles" in msg)
print("cat" in msg)

print("turtles" not in msg) # False
print("cats" not in msg) # True

#String Interpolation / f-strins

name = "Terry"
hobby = "fight"

msg = f"{name} loves to {hobby}"

print(msg) # Terry loves to fight