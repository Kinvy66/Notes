#列表生成器
#()
#方式一：将列表生成式中的[]替换成()

ge = (x for x in range(1,6))
print(type(ge))


#生成器需要通过next()方法获取数据，调用一次则返回一个数据
'''
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
'''


#注意：如果通过next()函数获取生成器中的数据，当数取完之后将不能再使用next
#print(next(ge))

#遍历
for x in ge:
    print('~~~~',x)



#方式二，通过yield[] 关键字生成
def test(n):
    for i in range(1,n+1):
        yield i

result = test(10)
print(result)

print(next(result))




