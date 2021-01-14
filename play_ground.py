# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

counter = 1
star = "*"

while counter < 6:
    print(f"{counter}. {star * counter}Loops are great{star * counter}")
    counter += 1 