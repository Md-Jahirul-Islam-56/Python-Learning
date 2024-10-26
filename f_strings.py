s = "My name is {0} and I am {1} years old" #old fashioned
name="Jahir"
age=22
print(s.format(name,age))

name_1="Tanbin"
age_1=19
s_1 = f"My name is {name_1} and I am {age_1} years old" #using f-string or string formatting
print(s_1)

book_price=205.6777
price=f"This book is {book_price:.2f} taka"
print(price)

print(type(price))

