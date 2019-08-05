import math
import random

#数学功能

#1.求绝对值 ；abs
a1 = -10
print(abs(a1))


#2.求最值 max  min
print(max(12,32,43,32423))
print(min(23,324,12,3,213,234))

#3.求x的y次方
print(pow(10,2))  #10的2次方


#需要导入math

#1.ceil(x):向上取整
print(math.ceil(129.3))
print(math.ceil(133.9))

#2.floor(x):向下取整
print(math.floor(12.9))
print(math.floor(12.1))

#3.modf: 获取一个浮点数的整数部分和小数部分，结果为一个元组
print(math.modf(12.3))

#4.求平方根,sqrt,结果为浮点数
print(math.sqrt(19))


#随机数，需要导入random

#1.从指定的列表中随机取出一个数
n1 = random.choice([2,21,32,35,546,133])

#2.
n2 = random.choice(range(5))  #[0,1,2,3,4]
n3 = random.choice('hello')   #['h','e','l','l','o']


#2.random()
print(random.random())  #产生一个[0,1]之间的随机数，结果为浮点型


#3. randrange(start,end,step)
'''
start ：开始值，包含在范围内，默认是0
end：结束值，不包含在范围内
step：步长，默认为1
'''
#从1~100之间选取一个奇数
print(random.randrange(1,100,2))

#shuffle:将列表中的元素进行随机排序
list1 = [1,2,3,4,5]
random.shuffle(list1)
print(list1)

#uniform  随机产生一个实数，[3,9],结果为浮点型
print(random.uniform(3,9))










