### Simple way to make a dict out of two list ###
animals = ["dog", "cat", "monkey"]
nums = [23, 33, 44]

# print(list(zip(animals, nums))) # [('dog', 23), ('cat', 33), ('monkey', 44)]

new_dic = dict(zip(animals, nums))

# print(new_dic) # {'dog': 23, 'cat': 33, 'monkey': 44}

### for loop way of making a dict using two list ###

animals = ["dog", "cat", "monkey"]
nums = [23, 33, 44]

new_dic = {}

for animal,num in zip(animals, nums):
    new_dic[animal] = num    

# print(new_dic) # {'dog': 23, 'cat': 33, 'monkey': 44}

### Dictonary Comprehension ###

animals = ["dog", "cat", "monkey"]
nums = [23, 33, 44]

new_dic = {animal:num for animal,num in zip(animals,nums)}

print(new_dic) # {'dog': 23, 'cat': 33, 'monkey': 44}

# Adding comparisons
new_dic = {animal:num for animal,num in zip(animals,nums) if num > 30}

print(new_dic) # {'cat': 33, 'monkey': 44}

#######################################################

### Instructor Examples ###

# # Dictionary comprehensions
# movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
# "Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
# year =[1971,1975,1979,1982,1983,2014]
# names = ['John','Eric','Michael','Graham','Terry','TerryG']
# print(list(zip(movies, year)))
# # give me a dict('movies': year) for each movies, year in zip(movies, year)
# new_dict = dict()
# for movie, yr in zip(movies,year):
#     new_dict[movie] = yr
# print(new_dict)

# new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
# print(new_dict)
# n1 =[[name + "s favorite movie was " + movie + " from " + str(yr)] for name,movie,yr in zip(names,movies,year) if yr < 1981 ]
# print(n1)