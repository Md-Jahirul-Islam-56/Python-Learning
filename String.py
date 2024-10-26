name='Jahirul'

print(len(name)) #len(name)=5
print(name[0:4],end='') #including zero but not 4th index
print(name[4:7]) #including 4th to 6th index

print(name[-5:-2]) #[len(name)-5 : len(name)-2] == [7-5 : 7-2]. It including 2nd to 4th index of the string.

last='Islam!!!!!'
last_name=last.rstrip('!')

print(name+last_name)
print(name.upper(),name.lower())

a="I have a friend. Arif is very smart. Arif is intelligent"
print(a.replace('Arif','He')) #replaces Arif to He
print(a.split()) #splits a word until it finds a space
print(len(a))
print(a.startswith("I")) #Checks whether the string starts with "I" or not and gives boolean output
print(a.endswith(".")) #Checks whether the string ends with a fullstop or not and gives boolean output
print(a.endswith("friend",0,15)) #Checks whether in first 15 indices the string ends with "friend" or not and gives boolean output
print(a.count("Arif")) #Finds how many times Arif is there in the string
print(a.find("Arif")) #Finds first index where it finds Arif in the string. Returns -1 if not found.
#print(a.index("Bakar")) #Finds first index where it finds Arif in the string. Returns an error message if not found.
print(a.center(80)) #makes new indices and move the a string to the center
print(a.center(80,"-")) #makes new indices and move the a string to the center and adds '-' in the new indices

b='i haVe A FrIeNd' 
print(b.capitalize()) #only capitalizes the first character
print(b.isspace()) #checks if everything is a space or not
print(b.istitle()) # if the string was b = 'I Have A Friend', then b.istitle() would return True.
print(b.swapcase()) 
print(b.title())

c='ArifIsVerySmart9'
print(c.isalnum()) #checks whether the string is alphanumeric or not 
print(c.isalpha()) #checks whether the string is alphabetic or not 

print(c.isupper()) #checks whether the string is upper case or not
print(c.islower()) #checks whether the string is lower case or not
print(c.isprintable()) #checks whether everything in the string is printable or not. \n,\t,\b,etc are not printable

