movie = {
    'title': 'Resident Evil',
    'year': 1996,
    'cast': ['chris', 'jill', 'barry']
}

print(movie['title']) # Resident Evil

# print(movie['fart']) # Error

# To avoid errors use the .get() attribute/method

print(movie.get('fart')) # None

# We can specify a default value if key cannot be found

print(movie.get('year', 'not found')) # 1996 

print(movie.get('fart', 'not found')) # not found

# Modifying a value

movie['title'] = "Resident Evil 2"

print(movie.get("title")) # Resident Evil 2

# Adding new key value pair

movie["budget"] = 2

print(movie) # {'title': 'Resident Evil 2', 'year': 1996, 'cast': ['chris', 'jill', 'barry'], 'budget': 2}

# Updating entire dictionary

movie.update({'sub title': 'Resident Evil 96', 'year' : 2001, 'cast': ['bob', 'tom', 'jerry']})

print(movie) # {'title': 'Resident Evil 2', 'year': 2001, 'cast': ['bob', 'tom', 'jerry'], 'budget': 2, 'sub title': 'Resident Evil 96'}

# Removing key value pair from dictionary

# 1. del command - permently deletes key value pair 

del movie['sub title']

print(movie) # {'title': 'Resident Evil 2', 'year': 2001, 'cast': ['bob', 'tom', 'jerry'], 'budget': 2}

# 2. .pop() - can store value in varialbe

budget = movie.pop('budget')

print(movie) # {'title': 'Resident Evil 2', 'year': 2001, 'cast': ['bob', 'tom', 'jerry']}

print(budget) # 2

# Get length len()

movie = {
    'title': 'Resident Evil',
    'year': 1996,
    'cast': ['chris', 'jill', 'barry']
}

print(len(movie)) # 3

# Get keys .keys()

print(movie.keys()) # dict_keys(['title', 'year', 'cast'])

# Get values .values()

print(movie.values()) # dict_values(['Resident Evil', 1996, ['chris', 'jill', 'barry']])

# Get items .items()

print(list(movie.items())) # dict_items([('title', 'Resident Evil'), ('year', 1996), ('cast', ['chris', 'jill', 'barry'])])

# Looping through dictionary

movie = {
    'title': 'Resident Evil',
    'year': 1996,
    'cast': ['chris', 'jill', 'barry']
}

for key in movie:
    print(key)

# title
# year
# cast


for key, value in movie.items():
    print(key, value)

# title Resident Evil
# year 1996
# cast ['chris', 'jill', 'barry']