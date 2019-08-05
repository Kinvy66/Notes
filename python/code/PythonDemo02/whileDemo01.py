'''
#打印十次hello world
n = 0
while n < 10 :
    print(n,'hello world')
    n += 1

# 求1~100之间所有整数的和

sum = 0
n = 0
while n < 101:
    sum += n
    n += 1
print("1~100的和是",sum)


#求1~100之间所有偶数的和
sum = 0
n = 0
while n < 101:
    sum += n
    n += 2
print(sum)

#求10的阶乘
sum = 1
n = 1
while n <=10:
    sum *= n
    n += 1
print('sum=',sum)

#统计100~1000被6整除的个数
a = 100
n = 0
while a <= 1000:
    if a % 6 == 0:
        n += 1
    a += 1

print('n = ',n)

'''


#打印9*9乘法表
i = 1
j = 1
while i <= 9:
    while j <= i:
        print('%dx%d=%d'%(i,j,i*j),end = ' ')  # end = ' ' 阻止换行，以空格结束
        j += 1
    i += 1
    j = 1
    print('\n')







