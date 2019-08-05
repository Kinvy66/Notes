#注意1：创建set需要一个已知的list，tuple或dict作为输入集合
#注意2，重复元素在set中会被自动过滤
s1 = set([12,312,1,3,12])
print(s1)

s2 = set((12,23,43))
print(s2)

s3 = set({'f':32,'dsf':88})  #只存dict的键
print(s3)