tuple1 = (1,2,32,121,1231)

print(tuple1[1])
#print(tuple1[5])  #不可以越界访问


#获取元组中的最后一个元素
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-5])  #第一个元素


tuple2 = (2,32,42,[3,34])
#tuple2[0] = 20    #报错
#修改列表的元素值
tuple2[3][0] = 9
print(tuple2)




