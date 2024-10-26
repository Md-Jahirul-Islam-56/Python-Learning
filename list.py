list_1= [0.8 , 30 , 2024, "Date", True] #similar to array but more advance. We can store any datatype in this.

print(list_1)
print(list_1[4])

if 2024 in list_1: #it can find any data in the list with a simple if statement
    print("2024 is found")
else:
    print("2024 is not found")

for i in range(2,4): #we can access any data by mentioning the index
    print(list_1[i],end=" ")
print("")

list_2=[i for i in range(1,11) if i%2==0 ] #we can store data in list by giving such conditions

print(list_2) #list of even numbers from 1 to 100 

list_names=["Abdullah", "Jaman", "Saud", "Majed"]
list_names_withS=[name_S for name_S in list_names if "S" in name_S] #stores names with character S from list_names list

print(list_names_withS)

list_3=[8,2,5,3,4,6,9,1,7,3,3,3,3,3]

list_3.append(10) #will add 10 at the end of the list
print(list_3)
list_3.sort() #sorting of list
print(list_3)
#list_3.sort(reverse=True) #reverse sorting
#print(list_3)
list_3.reverse() #reverse sorting
print(list_3)
#print(list_3.index(1)) #prints value of index 1
print(list_3.count(3)) #counts number of time 3 repeats in a list


# m=list_3 #it copies list_3 to new list m but problem is if we change list m then list_3 will also be changed
# m[2]=0
# print(m)
# print(list_3)

list_4=list_3.copy() #this is more better approach then previous one which will help to copy list_3 in list_4
print(list_4)
list_4.insert(9,0) #inserts a variable without deleting and the next indices moves 1 step forward
print(list_4)

k=[100,101,102]
# l=list_4+k #list contatenation
# print(l)

list_4.extend(k) #adds the specified list elements (or any iterable) to the end of the current list
print(list_4)


del list_4[2:8]  # To delete single value
print(list_4)
del list_4        # To delete whole list
#print(list_4) #gives error


