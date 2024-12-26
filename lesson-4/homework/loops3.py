list1= [1,1,2,3,4]
list2 =[1,3,4,5]
list3 =[]
for element in list1:
    if element not in list2:
        list3.append(element)
for element in list2:
    if element not in list1:
        list3.append(element)
print(list3)