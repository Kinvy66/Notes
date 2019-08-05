set1 = set([1,2,3,4,5,6])
print(set1)


#添加
#add(), 添加重复的元素无效
set1.add(9)
print(set1)

#set1.add([12,32])   #set的元素不能是列表，因为列表是可变de
set1.add((12,43))   #可添加元组，元组是不可变的
print(set1)
#set1.add({10:0})   #不能添加字典，字典是可变的value


#update()  插入整个list、tuple或者字符串，打碎插入
set2 = set([1,23,45,2,5])

#插入list
set2.update([11,124])
print(set2)

#插入tuple
set2.update((111,121))
print(set2)

#插入字符串
set2.update("hello")
print(set2)

#插入数字
#set2.update(329)   #不能插入数字，只能插入可遍历对象



#删除  remove()
set3 = ([1,2,3,4,5])
print(set3)
set3.remove(4)      #直接删除的是元素
print(set3)


#遍历
set4 = set([10,20,30,40,50,60])
#集合没有索引【无序】
#print(set4[2])



for i in set4:
    print(i)


