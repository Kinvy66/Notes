print('hello')
num = 88   #定义一个变量
del num    #删除num变量
#print(num)  #无法输出，num已经被删除
num = 19   #此处的num是一个新的变量
print(num)

'''
int(xx)  转换为整型

float(xx)  转换为浮点型

str(xx):转换为字符串

chr(xx)：转换为字符
'''

a = 10
a1 = str(a)
print(a)
print(a1)

#type():查看变量类型
print(type(a))
print(type(a1))

#id():查看变量的地址
print(id(a))
print(id(a1))

