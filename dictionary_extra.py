num = ( 1,2,2,2,2,3,3,4,5,4,4,5)

freq = {x:num.count(x) for x in num}
print(freq)


num_lst = [5,3,12,23,4,56,7,8,4,46,6,7,34,23,34,45]

freq_lst = {x:num_lst.count(x) for x in num_lst}
print(freq_lst)

merge_dic = {**freq,**freq_lst}
print(merge_dic)