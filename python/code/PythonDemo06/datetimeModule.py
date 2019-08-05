import datetime


#1.获取当前时间
d1 = datetime.datetime.now()
print(d1)


#2.获取指定时间
d2 = datetime.datetime(2019,8,2,10,8,58,2342)  #年月日时分秒毫秒
print(d2)

#3.将指定时间转换为字符串
d3 = d1.strftime('%Y-%m-%d')
print(d3)




#4.时间间隔计算，相减
d4 = datetime.datetime(2019,8,2,10,8,58,0)
d5 = datetime.datetime(2019,8,5,10,8,50,0)
d6 = d5 - d4
print(d6)
print(d6.days)
print(d6.seconds)



