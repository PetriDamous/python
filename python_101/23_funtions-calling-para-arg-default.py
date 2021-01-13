def greeting(name, age=28):
    print("Hello " + name + ". You are " + str(age) + " years old.") # do need to convert integer
    print(f"Hello {name}. You are {age} years old.") # do not need to convert integer

name = input("Enter your name: ")

greeting(name)