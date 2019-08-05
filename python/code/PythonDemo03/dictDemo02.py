# lis1和list2组成一个dict
list1 = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sum']
list2 = [1,2,3,4,5,6,7]

dict1 = {}

index = 0
if len(list1) == len(list2):
    while index < len(list1):
        dict1[list2[index]] = list1[index]
        index += 1

print(dict1)

