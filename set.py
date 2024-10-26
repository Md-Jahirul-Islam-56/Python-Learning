data = {123,123,123,345,34,56,True} #this is same as tuple but the order does not remain same (the data is saved at random indices). And sets do not allow duplicate values. 

print(data) #only one 123 is printed

s=set() #to declare a blank set
print(type(s))

s_1={"Xavi","Messi","Neymar","Iniesta","Suarez",34,56}
print(s_1.union(data)) #helps to add or do union of two sets. This doesn't change the previous set
# s_1.update(data) #this will change the previous s_1 set
# print(s_1) 

print(s_1.intersection(data)) #gives intersection of two sets
# s_1.intersection_update(data) #this will change the previous s_1 set
# print(s_1)

print(s_1.symmetric_difference(data)) #only similar data gets canceled
# print(s_1.symmetric_difference_update(data)) #changes the set as well
print(s_1.difference(data)) #similar data and the set inside difference both gets canceled

print(s_1.isdisjoint(data)) #checks whether two sets have intersections or not

s_2={"Suarez","Messi","Neymar"}
print(s_1.issuperset(s_2)) #checks whether s_1 set is superset of s_2 set or not
print(s_2.issubset(s_1)) #checks whether s_2 set is subset of s_1 set or not

s_2.add("Iniesta") #adding new data in set
print(s_2)

s_2.remove("Iniesta") #removing data in set
print(s_2)
# s_2.remove(23) #removing data in set and if not found then it gives error message
# print(s_2)
s_2.discard("Iniesta") #removing data in set
print(s_2)
s_2.discard(23) #it does not give error message
print(s_2)

print(s_2.pop()) #removes a random data
print(s_2)

s_2.clear() #clears everything in s_2
del s_2 #deletes s_2 completely








