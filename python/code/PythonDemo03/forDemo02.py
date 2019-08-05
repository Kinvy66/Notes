list1 = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sum']
list2 = ['Mon', 'Thur', 'Sat', 'Sum']

#显示list1中下标为奇数的yuans
for index , num in enumerate(list1):
    if index % 2 == 1:
        print(index,num)


for i in range(1,len(list1),2):
    num = list1[i]
    print(num)



#将列表list1中属于list2中的元素移除
new_list = list1.copy()   #将列表拷贝一份，保证循环时列表长度不变
for n in new_list:
    if n in list2:
        list1.remove(n)
        
print(list1)