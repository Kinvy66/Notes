list1 = [1, 545, 53, 521, 6, 21]

#for-in 遍历
'''
for 变量名 in 列表:
​		语句
'''

for num in list1:
    print(num)


#列表生成式

#
'''
range([start,] end [,step])  # [] 表示可以省略
说明：start表示开始的值，end表示结束的值，step表示步长
其中start和step可以省略，start和step默认值分别为0和1

功能：生成指定的列表

例如：
range(100)： 生成一个0~99的整数列表
range(1,100) : 生成一个1~99之间的整数列表
range(0,100,1) : 生成一个1~99的奇数列表

'''

print(list(range(1,10)))

sum = 0
for n in range(1,100):
    sum += n
print(sum)


