#1.获取元组的长度或者计算元组中的元素个数
#len
tuple1 = (32,323,43,76,9,3)
len = len(tuple1)
print(len)

#遍历元组
for index in range(0,len):
    print(tuple1[index])



#2.获取元组中的最值 max min




#3.列表和元组之间的相互转换
#列表====》元组
list1 = [1,34,13,8]
print(list1)
new_tuple = tuple(list1)
print(new_tuple)

#元组=====》列表
list2 = list(tuple1)
print(list2)


