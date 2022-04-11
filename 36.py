#Write a function to compute 5/0 and use try/except to catch the exceptions.



a=int(input("Enter the number(5) to check:"))
b=int(input("Enter the number(0) to check:"))
def divide():
    try:
        print(a/b)
    except ArithmeticError as e:
        print("Cannot divide a number by zero:",e)
    finally:
        print("executed")
    return "Finished"
print(divide())