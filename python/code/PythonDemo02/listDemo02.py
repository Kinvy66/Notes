#1.列表组合
#直接使用加号

list1 = [1,2,43]
list2 = [43,26,8,21]
print(list1+list2)

#2.列表重复
#直接使用乘号
print(list1 * 3)


#3.判断指定元素是否在列表中
#成员运算符： in   ,not in
#运算的结果为布尔值
list3 = ['hello',1,43,False]
print(1 in list3)  #True
print(1 not in list3)  #False


#4.列表的截取【分片，切片】
#语法；列表名【开始下标:结束下表】，表示获取从开始下标到结束下标之间的元素，结果为一个新的列表
#注意： 包头不包尾 ，[开始下标:结束下标)
list4 = ['hello',False,23,'good',435,3,765,79]
print(list4[2:4])

#获取从指定下标到结尾的列表，包含指定下标
print(list4[3:])


#获取从开头到指定下标的列表，不包含指定下标
print(list4[:6])




