#列表生成式

#生成一个1~10的整数列表
list1 = list(range(1,11))
print(list1)

#生成列表  [1*1,2*2,......]
list2 = []
for x in range(1,11):
    list2.append(x*x)
print(list2)



#列表生成式: []
#需要生成的元素x*x放到最前面，后面就是for-in循环
list3 = [x * x for x in range(1,11)]
print(list3)


#生成偶数的平方的列表
list4 = [x*x for x in range(1,11) if x % 2 == 0]
#list4 = [x*x for x in range(2,11,2) ]
print(list4)

#可以在列表生成式中使用两层循环
list5 = [m+n for m in 'ABC' for n in 'XYZ']
print(list5)
















