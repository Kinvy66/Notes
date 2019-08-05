#拷贝
#浅拷贝，引用拷贝
list1 = [1, 2, 3, 4, 5]
list2 = list1
print(list1)
print(list2)
list2[2] = 100
print(list1)
print(list2)


#1. copy  深拷贝
list3 = [1, 2, 3, 4, 5]
list4 = list3.copy()
print(list3)
print(list4)
list4[2] = 434
print(list3)
print(list4)