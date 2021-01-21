python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# Membership test

# print('arthur' in holy_grail) # False (case senstive)

# print('Arthur' in holy_grail) # True

# print('Arthur' not in holy_grail) # False 

# print('arthor' not in holy_grail) # True

# Combining dictionaries

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}

people_1 = {}
people_2 = {}
people_3 = {}

# 1 Update (can only update one dictoinary at a time)

people_1.update(python)

print(people_1) # {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}

people_1.update(holy_grail)

print(people_1) # {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34, 'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}

# 2 comprehension (allows you to update using multiple dictionaries at once)

for groups in (python, holy_grail) : people_2.update(groups)

print(people_2) # {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34, 'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}

# 3 unpacking 3.5 later

people_3 = {**python, **holy_grail}

print(people_3) # {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34, 'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}

# Sum of values 

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}

print(sum(python.values())) # 215

