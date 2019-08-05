#引用传递和值传递

#值传递
def fun1(a):  #形参 a = 5
    a = 100
    print(id(a))

#实参
temp = 5
fun1(temp)  #a = temp
print(temp)
print(id(temp))

#引用传递
def fun2(l):
    l[1] = 100
    print(id(l))

list1 = [1,2,3,4]
print(list1)

fun2(list1)    #传递的是引用【地址】
print(list1)
print(id(list1))

#总结：值传递传的是数据，引用传递传的是地址