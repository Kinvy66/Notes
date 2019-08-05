import calendar


#1.直接放回指定年和月的万年历表示形式
print(calendar.month(2019,8))

#2.返回万年历的二维列表表示形式
print(calendar.monthcalendar(2019,8))

#3.直接返回指定年份的万年历形式
print(calendar.calendar(2019))

#4.判断某年是否为闰年
print(calendar.isleap((2019)))
print(calendar.leapdays(2000,2020))   #从2000~2020(不包括)的闰年数


#5.返回指定月的第一天的星期和这个月的所有天数
print(calendar.monthrange(2019,7))


print(calendar.monthcalendar(2019,8))   #当月的日期二维数组显示


print(calendar.weekday(2019,8,11))  #某个日期的星期



