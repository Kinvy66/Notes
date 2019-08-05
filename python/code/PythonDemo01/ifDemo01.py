#导入
import random

'''
num1 = 3
num2 = 2

if num1 == num2:
    num1 = 100

print(num1)
'''



#随机获取一个数，和控制台输入的数进行比较，如果相等，则中奖
res = random.choice(range(100)) + 1  #取1-100的随机数

print(res)

num = int(input("输入一个数："))

if res == num:
    print("bingo")

