def greeting(name, age=28, color="red"):
    print(f"Hello {name}. Your age is {age} and you like the color {color}.")

print(greeting(age=34, color="green", name="Chris")) # Hello Chris. Your age is 34 and you like the color green.

print(greeting(name="Jill")) # Hello Jill. Your age is 28 and you like the color red.