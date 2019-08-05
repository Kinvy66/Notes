#1.转换： eval()
num1 = eval('123')   #int()
print(num1)
print(type(num1))

print(eval('+123'))
print(eval('-123'))

#print(eval('12+32'))   #报错，不能这样使用

#2.计算长度或者某个子字符串出现的次数
# len()     count()

s1 = 'tomorrow is sunny day, today is friday'
print(len(s1))

#在某个区间内查找出现次数
print(s1.count('is',2,15))


#3.大小写字母转换
#lower()    大写字母转换为小写
s2 = 'Tomorrow is sunny day, Today is Friday'
s21 = s2.lower()
print(s21)

#upper()   小转大
s22 = s2.upper()
print(s22)


#swapcase():    大转小，小转大
s23 = s2.swapcase()
print(s23)

#capitalize() 首个单词的首字母大写，其他小写
s24 = s2.capitalize()
print(s24)

#title()  每个单词的首字母大写
s25 = s2.title()
print(s25)


#4.填充字符串
#center(width,fillchar)  将原字符串居中显示，剩余部位用指定字符串填充
s3 = 'tomorrow is sunny day'
print(s3.center(80,'*'))


#ljust()  将原字符串居左对齐，其余位置用指定字符补充
print(s3.ljust(30,'%'))

#rjust()  将原字符串居左对齐，其余位置用指定字符补充
print(s3.rjust(30,'%'))


#zfill()  返回一个长度为width的字符串，原字符串居右对齐，前面用0填充
print(s3.zfill(40))


#5.查找
#find() 默认从头到尾查找，可以指定查找的区间
s4 = 'tomorrow is sunny day'
print(s4.find('day'))   #返回的是子字符串在原字符串中第一字母出现的下标
print(s4.find('435'))   #如果未找到，则返回-1
print(s4.find('is',3,18)) #在指定区间查找


#rfind  从右向左查找
print(s4.rfind('day'))   #返回的是子字符串在原字符串中第一字母出现的下标

#index()  类似find
print(s4.index('day'))


#rindex()  类似于rfind()
print(s4.rindex('day'))


#6.截取
#strip()   删除指定的字符串
s5 = '******abc123*******'
print(s5.strip('*'))


#lstrip()  剔除左边对应的字符
s6 = '*********hello******'
print(s6.lstrip('*'))

#rstrip()  剔除右边对应的字符
s7 = '*******hello********'
print(s7.rstrip('*'))


#7.分隔和合并
#spit()  通过指定的字符串进行分隔，结果为列表
s8 = 'tomorrow is sunny day da da da'
print(s8.split(' '))
print(s8.split(' ',3))  #只分隔前三  ['tomorrow', 'is', 'sunny', 'day da da da']


#splitlines()    \r  \n  \r\n 通过行分隔
s9 = '''tomorrow 
is
sunny
day'''
print(s9.splitlines())

#join()
s10 = '*'
s11 = 'tomorrow is sunny day'
print(s10.join(s11))


#8.替换
#replace(old, new, max)  使用new的字符串替换old的字符串，最大的替换次数不超过max
s12 = 'tomorrow is sunny day tomorrow is sunny day tomorrow is sunny day tomorrow is sunny day'
print(s12.replace('sunny','winda'))   #默认全部替换
print(s12.replace('sunny','wind',2))


#映射替换
#maketrans  创建
t  = str.maketrans('cc','68')














