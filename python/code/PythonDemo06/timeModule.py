import time

#时间参数有九个，是以元组的形式
#年(1970~)，月(1~12)，日(1~31)，时(0~23)，分(0~59)，秒(0~59),星期(0~6,0 is Monday)，
#今天是一年中的第几天(1~366),DST(0:正常格式，1：夏令时格式，-1:根据当前的日期时间来判定)



#1.获取当前时间戳
c = time.time()
print(c)


#2.将时间戳转换为UTC时间   生成的数据是一个元组
g = time.gmtime(c)
print(g)


#3.时间戳生成当地时间
l = time.localtime(c)
print(l)

#4.将对应的UTC时间转换为时间戳
c2 = time.mktime(l)
print(c2)

c3 = time.mktime((2019,8,2,9,34,6,4,214,0))  #传入一个元组
print(c3)

#5.将时间戳转换为字符串
c4 = time.ctime(c)
print(c4)


#6.将时间元组转换为格式化字符串
#注意：必须严格按照格式胡的形式书写字符串
s = time.strftime('%Y-%m-%d %H:%M:%S',l)
print(s)

#7.将指定格式的时间字符串转换为时间元组
p  = time.strptime('2019-08-02 09:47:53','%Y-%m-%d %H:%M:%S')
print(p)


#8.休眠
print('**********')

time.sleep(5)  #参数单位秒


print('**********')



#9.用来衡量不同程序的耗时
#time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8:
# use time.perf_counter or time.process_time instead print(time.clock())
print(time.clock())


































