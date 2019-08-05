#语法：lambda[arg1,arg2,.......argn]: 函数体
def add(num1,num2):
    return num1+num2

print(add(10,13))



#匿名函数
sum = lambda num1,num2:num1+num2
print(sum(19,32))


#匿名函数也可以使用关键字参数
g = lambda x,y:x ** 2 + y **2
print(g(2,3))

print(g(x = 2,y = 3))

#匿名函数也可以使用默认参数
h = lambda  m = 0, n = 0: m*n
print(h(2,3))
print(h())
print(h(n = 3))


#if __name__ == "__main__":
#    print('main')








