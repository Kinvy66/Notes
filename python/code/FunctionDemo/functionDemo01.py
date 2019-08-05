#函数的声明
#def fun_name(参数1，参数2):
#    #语句
#    return

#定义函数
def test():
    print("fun1")
#调用函数
test()


#函数的参数
#分类： 1.形参    2.实参
def f1(name,age):
    print("i am %s,age is %d"%(name,age))

f1('jack',18)
#注意:python中，形参的类型由实参的类型决定，一般情况下，由函数的具功能决定



#求圆的面积
def  area(r):
    s = 3.14 * r ** 2
    return s

print(type(area(2)))







