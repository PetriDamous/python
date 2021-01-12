# .list() on string

string = "hello"

print(list(string)) # ['h', 'e', 'l', 'l', 'o']

# .split()

string = "what is this?"

print(string.split()) # ['what', 'is', 'this?']

print(string.split("w")) # ['', 'hat is this?']

# .join()
msg = ['h', 'e', 'l', 'l', 'o']

print("".join(msg)) # hello

print("-".join(msg)) # h-e-l-l-o

print("-".join(msg + msg))

# .replace()
string = "hello"

print(string.replace("l", "7"))