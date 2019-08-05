#从控制台获取数据
name = input("name：")
age = input("age:")
#print('hello',name,age)


#需求：计算还能活多久
#说明，通过input获取的数据全部都是字符串
deat_age= 80
print(deat_age - int(age))  #数据强制转换为int

print("还可以活",deat_age - int(age),"年")  #字符串拼接

#用“+”拼接，可以用在字符串和其他数据类型之间，结果是字符串
print("还可以活"+str(deat_age - int(age))+"年")


#输入两个数并计算和
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
print("sum = ",num1+num2)

