#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed 

# Basic Exception

try:
    num = 1
    print(f"{num/0}")
except:
    print("error") # error (Except runs because you cannot divide 0 by 0)

# ValueError Exception
# Has to come before default exception

try:
    x = int("dog")
    print(x)
except ValueError:
    print("ValueError yo!!!") # ValueError yo!!!
except:
    print("boo")

# ZeroDivisionError Exception

try:
    x = 2 / 0
    print(x)
except ValueError:
    print("ValueError yo!!!") # skips this exception
except ZeroDivisionError:
    print("Zero div error yo!!") # Zero div error yo!!
except:
    print("boo")

# as key work
# allows us to get the specific error

try:
    # x = 2 / 0
    x = int("dog")
    print(x)
except ValueError as fuck:
    print(fuck)
except ZeroDivisionError as err:
    print(err) # invalid literal for int() with base 10: 'dog'
except:
    print("boo")

# else and finally blocks
# else runs if code is error free
# finally runs no matter what happens

try:
    num = 2
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err,num, "Bad Value not between 1 and 30!")
except:
    print("Invalid Input!")
else:
    print("30 divided by",num, "is: ", 30/num) # 30 divided by 2 is:  15.0 
finally:
    print("**Thank you for playing!**") # **Thank you for playing!**

# raise