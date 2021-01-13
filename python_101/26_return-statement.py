def sales_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    # return amount, tax, total_amount # default returns tuple
    # return [amount, tax, total_amount] # modified to return list
    # return {amount, tax, total_amount}
    return f"{amount}, {tax}, {total_amount}"

price = sales_tax(100)

#Returns tuple
# print(price, type(price)) # (100, 25.0, 125.0) <class 'tuple'>

#Returns list
# print(price[1], type(price)) # 25.0 <class 'list'> (we can access an item in the list using [])

#Returns set
# print(price, type(price)) # {25.0, 100, 125.0} <class 'set'>

#Returns string
print(price, type(price)) # 100, 25.0, 125.0 <class 'str'>