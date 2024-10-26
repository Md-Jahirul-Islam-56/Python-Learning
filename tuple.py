t=(1,2,3,4,5,56,4,3,2,"happy",True) #this is same as list but we cannot change the value of tuple.

#t[0]=90 #is not possible
t_list=list(t)  #To change the datas inside tuple we need to make it a list.
print(t_list)
t_list[0]=90 #it is possible
t_list.append("Jahir") #"Jahir" will be added at the end of t_list
t_list.remove(56) #removes first occurance of 56 if not found then gives error message
#t_list.remove(56) #gives error message
t_list.pop(3) #removes data at index 3

print(t_list)

t=tuple(t_list) #now change back to tuple
print(t)


if 56 in t:
    print("56 is present in tuple t")

t_2=t[0:len(t)] #copying elements of t tuple to t_2 tuple
print(t_2.count(3)) 

t_3=("Bangladesh","India","Pakistan")
t_4=("Nepal","Bhutan","SriLanka","Maldives")
t_SAARC=t_3+t_4
print(t_SAARC)

