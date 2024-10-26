a= int(input("Enter integer:"))

if a>0 and a<201:
    print(a)
else:
    raise ValueError("a variable should be between 1-200") #it will raise an error to the user


# declaring Custom Error:

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...