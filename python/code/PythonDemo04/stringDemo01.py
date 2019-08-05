#字符串运算


#1.字符串拼接
s1 = 'hello'
s2 = 'world'
s3 = s1 + s2
print(s3)


#2.字符串重复
s4 = s1 * 3
print(s4)

#3.获取字符串中的字符
#语法：字符串名[索引]
print(s1[3])


#4.截取字符串【切片】
s5 = 'wellcomhelloworld'
print(s5[2:6])   #包头不包尾
print(s5[2:])
print(s5[:6])


s6 = 'abc123456'
print(s6[2:5])
print(s6[2:])
print(s6[2::2])
print(s6[::2])
print(s6[::-1])
print(s6[-3:-1])



#5.判断是否包含指定字符串
print('abc' in s6)

