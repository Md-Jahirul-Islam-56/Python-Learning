dic = { 56: "Jahirul", #{key: value}
        55: "Rohan" }

print(dic)
print(dic[56])
#print(dic[51]) #51 is not in the dictionary so it will throw error
print(dic.get(51)) #51 is not in the dictionary but it will not throw error

#To excess all the keys:
print(dic.keys())

#To excess all the values:
print(dic.values())

# using for loop and f_string we can excess the keys and values:
for key in dic.keys():
    print(f"The value of key {key} is {dic[key]}")

print(dic.items()) #this allows to excess the key and value both at the same time. It gives the key and values in pair. 

for key,val in dic.items(): #with a for loop, we can seperate the key and value that is in pair in items()
    print(key,",",val)

#empty dictionary:
emp = {}

#Like list we can use update(), clear(), del, popitem(), etc 