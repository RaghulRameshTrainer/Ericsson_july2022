'''
4 Clauses in Exception:
=======================
try
except
else
finally
'''
try:
    with open("customers.txt",'r') as fo:
        print(fo.read())
    print(5+6)
    print(10/1)
    age=int(input("Enter your age:"))
    if age < 0 or age > 100:
        raise ValueError("Age cannot be less than 0 and greater than 100!")
    print("Your age is :", age)
except FileNotFoundError as e:
    print("Received file error: ", e)
except TypeError as e:
    print("type error:", e)
except ValueError as e:
    print("AGE ISSUE : ", e)
except Exception as e:
    print("Caught by general exception: ", e)
else:
    print("form else since there is no exception")
finally:
    print("From finally that i run always irrespective of the exception!")

print("I am next line to exceptions")