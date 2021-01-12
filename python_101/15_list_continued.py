re1 = ["chris", "jill", "wesker", "barry", "rebecca"]

num = [911, 130, 328, 535, 740, 308]

#reverse()
re1.reverse()

print(re1) # ['rebecca', 'barry', 'wesker', 'jill', 'chris']

#sort()
re1.sort()

print(re1) # ['barry', 'chris', 'jill', 'rebecca', 'wesker']

#sort reverse
re1.sort(reverse=True)

print(re1) # ['wesker', 'rebecca', 'jill', 'chris', 'barry']

#min()
print(min(re1)) # barry (lowest letter value based on first letter)

#max()
print(max(re1)) # wesker (highest letter value based on first letter)

#min()
print(min(num)) # 130

#max()
print(max(num)) # 911

#sum()
print(sum(num)) # 2952 (sums all numbers in list together)

# .append
animals = ["dog", "cat", "turtle"]

animals.append("rat") # .append(value to add to end of list)

print(animals) # ['dog', 'cat', 'turtle', 'rat']

# .insert()
animals = ["dog", "cat", "turtle"]

animals.insert(1, "monkey") # .insert(idex to insert, value to insert)

print(animals) # ['dog', 'monkey', 'cat', 'turtle']

#overwriting value
animals = ["dog", "cat", "turtle"]

animals[1] = "bird" # overwrites value with new value at index we provide

print(animals) # ['dog', 'bird', 'turtle']

# .extend()
animals = ["dog", "cat", "turtle"]

nums = [1, 2, 3]

animals.extend(nums)

print(animals) # ['dog', 'cat', 'turtle', 1, 2, 3]

print(nums) # [1, 2, 3] (remains untouched)

# .remove()
animals = ["dog", "cat", "turtle"]

animals.remove("cat") # completly removes item from list (not stored in memory)

print(animals) # ['dog', 'turtle']

# .pop()
animals = ["dog", "cat", "turtle"]

turtle = animals.pop() # we can store popped values in varialbes (value is stored in memory)

print(animals) # ['dog', 'cat']

print(turtle) # turtle

# .pop() by index
animals = ["dog", "cat", "turtle"]

dog = animals.pop(0) # can enter index to pop specific item

print(animals) # ['cat', 'turtle']

print(dog) # dog

# .clear()
animals = ["dog", "cat", "turtle"]

animals.clear()

print(animals) # []

# del list
animals = ["dog", "cat", "turtle"]

# del animals (completly removes list from memory. we will get an error if we try to print animals list now)

# print(animals)

#del specific item in list
animals = ["dog", "cat", "turtle"]

del animals[1]

print(animals) # ['dog', 'turtle']

#3 ways to copy list

# 1 range [:]
animals = ["dog", "cat", "turtle"]

new_animals = animals[:] # [:] returns entire list then we just assign it to the variable

print(new_animals) # ['dog', 'cat', 'turtle']

# 2 .copy()
animals = ["dog", "cat", "turtle"]

new_animals = animals.copy()

print(new_animals) # ['dog', 'cat', 'turtle']

# 3. list()
animals = ["dog", "cat", "turtle"]

new_animals = list(animals)

print(new_animals) # ['dog', 'cat', 'turtle']


