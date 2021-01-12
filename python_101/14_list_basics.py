re1 = ["chris", "jill", "wesker", "barry", "rebecca"]

print(re1[1]) # jill

print(re1[-2]) # barry

print(re1[1:3]) # ['jill', 'wesker'] (remember the last value is exclusive)

print(re1[3:]) # ['barry', 'rebecca']

print(re1[:]) # ['chris', 'jill', 'wesker', 'barry', 'rebecca'] (the whole list)

print(re1[:2]) # ['chris', 'jill'] (everything up until index 2. last value is exclusive)

print(len(re1)) # 5 (length of list)

print(re1.index("rebecca")) # 4 (returns the index of object we are looking for)

print(re1.count("wesker")) # 1 (returns the number of occurances of an object)