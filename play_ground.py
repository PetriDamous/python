### Play with comprhensions and for loops ###

# movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
# "Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]

# year =[1971,1975,1979,1982,1983,2014]
# names = ['John','Eric','Michael','Graham','Terry','TerryG']

# decorator
# def annouce(f):
#     def wrapper():
#         print("About to run")
#         f()
#         print("Already ran")
#     return wrapper

# @annouce
# def greeting():
#     print("hello")

# greeting()

people = [
    {"name": "chris", "game": "re1"},
    {"name": "leon", "game": "re2"},
    {"name": "wesker", "game": "re1"}
]

people.sort(key= lambda dic: dic["name"])

print(people)