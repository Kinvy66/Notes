#存储多个学生的成绩
dict1 = {'s1':87,'s2':82,'s3':90}

#元素的访问
#1.获取   语法：字典名[key]
print(dict1['s1'])


#get()
result = dict1.get('s2')
print(result)

#添加,当指定的键不存在的时候，则表示添加
dict1['s4']  = 37
print(dict1)

#如果键已经存在，则表示修改valu
dict1['s1'] = 60
print(dict1)

#删除 pop
#注意：通过键直接删除整个键值对
dict1.pop('s1')
print(dict1)



#遍历
dict2 = {'tom':90,'jack':83,'lei':40}

#方式一：只获取键
for key in dict2:
    value = dict2[key]
    print(key,value)


#方式二，只获取值
#valus,得到的结果是一个列表
print(dict2.values())

for value in dict2.values():
    print(value)


#方式三，同时获取键和值
#items 得到的结果是一个列表，列表中的元素是元组
print(dict2.items())   #[('tom', 90), ('jack', 83), ('lei', 40)]


for key, value in dict2.items():
    print(key,value)

#方式四
for index, key in enumerate(dict2):
    value = dict2[key]
    print(index,key,value)
