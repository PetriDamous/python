# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("Enter first name: ")
miles = float(input("Enter kilometers traveled: "))

def convert(kilo):
    return kilo / 1.609

print(f"Hello {name}, you have travled {round(convert(miles), 1)} miles")


   





