### Currying ###

def price_calc(start, hourly_rate):
    return lambda hours: start + hourly_rate * hours

regular_customer = price_calc(10,30)
premium_customer = price_calc(1,25)

print(regular_customer(10)) # 310
print(premium_customer(1)) # 26

### positional argument notation ###
print((lambda a,b,c: a + b + c)(1,2,3)) # 6

# Default argument example
print((lambda a, b, c=2: a + b + c)(1,2)) # 5

# Named argument 
print((lambda a, b, c: a + b + c)(b=4, a=2, c=7)) # 13

# Unpacking parameter
print((lambda *arg: sum(arg))(4,5,6,50,200)) # 265

print((lambda *arg: print(type(arg)))(2,3,4)) # <class 'tuple'>