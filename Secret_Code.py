import random
import string

def generate_random_string(length):
    # Define the characters you want to include in the string
    characters = string.ascii_letters + string.digits
    # Use random.choices to select random characters from the set
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

user_string = input("Enter sentence to encrypt:")
new_string=""

if len(user_string) <= 3:
    first_rand= generate_random_string(3)
    last_rand= generate_random_string(3)
    new_string = first_rand + user_string[1:] + user_string[0] + last_rand
    print(new_string)
else:
    new_string=user_string[::-1]
    print(new_string)


user_dstring = input("Enter sentence to decrypt:")
new_dstring1 =""
new_dstring2 =""


new_dstring1=user_dstring[::-1]
try:
    new_dstring2 =  user_dstring [3:-3]
    new_dstring2 = new_dstring2[-1] + new_dstring2[:-1]
except:
    new_dstring2=None

print(f"Your data is either this: {new_dstring1}\nor this: {new_dstring2}")

