# - You sell lemonade over two weeks, the lists
# show number of lemonades sold per week

# - Profit for each lemonade sold is $1.5

# 1. Add another day to week 2 list by capturing a 
# number as input

# 2. Combine the two lists into the list called 'sales'

# 3. Calculate / print how much you have earned on:
# - Best day
# - Worst day
# - Give total

# Hint: 3 prints in total

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

# My solution

new_sale = float(input("Enter new sale: "))

sales_w2.append(new_sale)

sales = sales_w1[:]

# sales = sales_w1.copy()

# sales = list(sales_w1)

sales.extend(sales_w2)

print(f"Best day - number of sales: {max(sales)}, profit made: ${max(sales) * 1.5}")

print(f"Worst day - number of sales {min(sales)}, profit made: ${min(sales) * 1.5}")

print(f"Total sales: {sum(sales)}, total profit: {sum(sales) * 1.5}")



# Instructors solution

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
sales = sales_w1 + sales_w2
#sales.sort()
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')