import functools

#函数的默认参数：设定参数的默认值

#偏函数:对参数做一些控制的函数
#偏函数一般不需要自己定义，直接使用

#模块functools其中就有偏函数的功能
#int()将字符串或浮点型转换为整型，当传入字符串时，默认按照十进制进行转换
print(int('123'))   #123

#int()中还提供了一个额外的参数base，默认值是10
print(int('123',base = 10))  #123

#如果传入base参数，则可以进行N进制的转换
print(int('12345',base = 8))  #5349   将1234作为8进制的数，然后输出为十进制

#二进制
print(int('110',2))   #6  将110作为2进制的数，以十进制的方式打印出来

'''
def int2(x,base):
    return int(x,base)
'''



#functools.partial  帮助我们创建一个偏函数，不需要重新定义int2()
#参数一：需要创建偏函数的函数名， 参数二：需要设定的默认值
int2 = functools.partial(int, base=2)   #创建一个偏函数
print(int2('1101'))   #二进制

print(int2('110',base = 10))













