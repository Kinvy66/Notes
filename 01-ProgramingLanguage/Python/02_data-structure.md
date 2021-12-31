# 数据结构

数据结构就是数据在计算机内存中存放的空间结构，在python语言中提供了四种内置的数据结构--列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set），同时还提供了一些对于这些数据结构的操作，比如切片，迭代等。



## 1. 列表（list）

`列表` 是一种用于保存一系列有序项目的集合，也就是说，你可以利用列表保存一串项目的序列。其中的元素是可以改变的。

在Python中，用方括号（`[]`）来表示列表，并用逗号来分隔其中的元素，列表中的元素的类型没有限制，可以是基本的数据类型，字符串，甚至是另一个列表。

例如

```python
l1 = [1, 4, 9, 4]	#全是整数型的一个list
l2 = [1, 3.9, 10, 'cat']	#多种数据类型的list
l3 = ['cc', [1, 2, 4], 9.0] #list中包含另一个list
```

获取list的元素，格式 ：`listname[index]` , index是元素的索引，索引是从0开始的

list元素的访问

```python
fruit = ['apple', 'mango', 'carrot', 'banana']		#定义一个list
print(fruit)     #打印整个list的元素
print(fruit[0])  #打印第一个元素
print(fruit[-1]) #打印倒数第一个

```

元素的增删改查

```python
 #len()查询list的容量
print(len(fruit))             

#在末尾追加元素
fruit.append('orange')         
print(fruit) 

#在指定的位置插入元素
fruit.insert(2,'watermelon')   
print(fruit)

#删除某个元素
del fruit[0]
print(fruit)

#删除最后一个元素，同时可获得最后元素的值
print(fruit.pop())  
print(fruit) 

#删除指定值的元素
fruit.remove('carrot')
print(fruit)
```





**示例**，list01.py

```python
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

```

输出

```shell
$ python list01.py
I have 4 items to purchase.
These items are: apple mango carrot banana 
I also have to buy rice.
My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
The first item I will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
```





## 2. 元组（tuple)

元组`tuple` 和列表一样都是可以将多个对象保存到一起，但是tuple相比于list多了一些限制，比如tuple是不可以改变的。tuple的定义是用 `()` 来表示，元素之间用逗号隔开。

tuple的定义

```python
t1 = (1, 2, 3)
print(t1)
t2 = ()    #这是一个空的tuple
t3 = (1,)  #这是一个只有一个元素的tuple
```

> 定义一个空tuple只写一个空的`()` ，对于只有一个元素的tuple不能这样定义 `t = (1)`, 这个语句的中的 `()` 会被解释为数学运算中的括号，所以这里的 `t` 是一个整数。为了避免歧义，一个元素的tuple应该在元素后加一个逗号



因为tuple是不可变的，所以对于tuple没有 `append`,`remove`,`insert` 等操作，对于tuple的访问和list是一样的，使用索引， `tuplename[index]`

示例，tuple01.py

```python
# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
len(new_zoo)-1+len(new_zoo[2]))
```

输出

```shell
$ python tuple01.py
Number of animals in the zoo is 3
Number of cages in the new zoo is 3
All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))
Animals brought from old zoo are ('python', 'elephant', 'penguin')
Last animal brought from old zoo is penguin
Number of animals in the new zoo is 5
```



## 3. 字典（dict）

字典的数据结构就像是我们使用的字典，拼音和汉字是一一对应的。在python中的字典是key-value（键-值）一一对应的，key值和value的值是是关联在一起的。

在一个dict类型的数组中，还具有以下的特点：

* key的值不可以重复
* key值只能是不可变对象，例如字符串，value值没有限制，可以是可变或不可变对象
* dict中的数据是无序的







## 4. 集合（set)





## 







##　5. 高级特性



### 5.1 切片





### 5.2 迭代





### 5.3 列表生成式





### 5.4 生成器





### 5.5 迭代器



 

