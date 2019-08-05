#list的内置功能

#1.append  在列表结尾添加元素或者新的列表
list1 = [1, 2, 3, 4, 5]

#追加元素
list1.append(100)
print(list1)

#追加列表,将列表作为一个元素追加
list1.append([6, 7, 8])
print(list1)


#2.extend  在列表的末尾一次性追加另一个列表中的元素
list2 = [1, 2, 4, 5 , 100]
list2.extend([64, 34, 745])
print(list2)


#3.insert  在指定索引出插入一个元素，原有的元素向后移
list3 = [1, 3, 4]
print(list3)
#插入元素
list3.insert(2,433)  #在2的索引位置插入433
print(list3)

#插入列表
list3.insert(2,[7545,312])
print(list3)


#4.pop   移除列表中指定的元素
list4 = [1, 2, 3, 4, 5, 100]
print(list4)
#默认移除最后一个元素
list4.pop()
print(list4)
#移除指定下标的元素
list4.pop(3)
print(list4)


#5.remove  移除元素
list5 =[32, 23, 987, 43, 523]
#如果元素不存在，则出错误
#list5.remove(5)  #移除list中的5这个元素
list5.remove(43)
print(list5)



#6.clear   清空列表
list6 = [12, 3, 4, 32, 6, 64]
list6.clear()   #清空之后是一个空列表
print(list6)




#7.index    从列表中查询第一个匹配的元素
list7 =[11, 332, 435, 235, 545, 65, 11]
print(list7)
#在整个列表中查询
print(list7.index(11))

#只在部分列表中查询
print(list7.index(11,2,7))  #2,7表示开始和结束下表，左闭右开


#8.len    获取列表中元素的个数【获取列表的长度】
list8 = [12, 312, 23, 45, 76, 3, 87, 329, 328, 3219]
#注意：len直接使用
print(len(list8))


#9.max    获取列表中最大的值
print(max(list8))

#10.min   获取列表中的最小值
print(min(list8))


#11.count    查看元素在列表中出现的次数
print(list8.count(12))   #查看12出现的次数


#12.reverse   将列表实现倒序
list8.reverse()
print(list8)



#  排序

#sort 和 sorted
#13. sorted
list9 = [11, 32, 443, 2, 4, 532, 234]
#默认实现升序排序
list1 = sorted(list9)
print(list1)

#可以实现降序排序
list2 = sorted(list9,reverse=True)
print(list2)

#根据字符串长度排序
list10 = ['hello', 'good', 'ki', 'jackde']
list3 = sorted(list10,key=len)
print(list3)

#sort  在原列表里排序
list9.sort()       #升序
#list.sort(reverse = True)  #降序
print(list9)




