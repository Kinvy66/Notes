#函数的参数

#1.必须参数
def fun1(a,b,c):
    print(a,b,c)

fun1(1,2,True)


#2.关键字参数
def fun2(name, age):
    print('i am',name,' i am ',age)
#fun2('jack',18)

#使用关键字参数, 顺序可以调换
fun2(name = 'jack',age = 18)
fun2(age = 18,name = 'jack')


#3.默认参数
#如果在调用函数时，对默认参数不传值，则使用默认的值
#定义函数时，默认参数只能出现在最后面
def fun3(name,age = 10):
    print('i am', name, ' i am ', age)

fun3('jack')
fun3(age = 18,name = 'jack')


#4.不定长参数【可变参数】
#能处理比当初声明函数更多的参数
#*  类型是tuple
def fun4(name,*hobby):
    print(type(hobby))
    for x in hobby:
        print(x)

fun4('tom','book','read')

#**
def fun5(**args):
    #**的不定长参数被当做字典处理
    print(type(args))
    print(args)   #{'x': 1, 'y': 3}

fun5(x = 1, y = 3)  #参数：key = value



















