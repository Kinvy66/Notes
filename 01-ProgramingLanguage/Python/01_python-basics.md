# python基础



## 0. 计算机基础知识

### 1. 关于进制

在计算机中所有的数据无论是存储还是处理都是以二进制的形式进行的。像python等高级编程语言虽然不需要之间使用二进制，但是编程的话还是需要了解二进制的一些基本知识。

二进制和我们平时使用的十进制不同的在于二阶制的数是只有 `0`和 `1` 两个数字表示，十进制是逢十进一，而二进制是逢二进一，以下是0~15数码对应的十进制，二进制和十六进制表示(逢16进1)

| 十进制 | 二进制 | 十六进制 |
| :----: | :----: | :------: |
|   0    |   0    |    0     |
|   1    |   1    |    1     |
|   2    |   10   |    2     |
|   3    |   11   |    3     |
|   4    |  100   |    4     |
|   5    |  101   |    5     |
|   6    |  110   |    6     |
|   7    |  111   |    0     |
|   8    |  1000  |    0     |
|   9    |  1001  |    9     |
|   10   |  1010  |    A     |
|   11   |  1011  |    B     |
|   12   |  1100  |    C     |
|   13   |  1101  |    D     |
|   14   |  1110  |    E     |
|   15   |  1111  |    F     |



### 2. 二进制的运算

- 与
- 或
- 非
- 异或



## 1. 基础

### 1.1 第一个python程序

新建文件 `01_hello.py`, 输入以下代码

```python
#01_hello.py
'''
这是第一个python程序
功能：打印输出 
hello pyhton!
你好
hello pyhton!
你好
'''
print("hello python!")
print("你好")
print('''hello python!
你好''')
```



### 1.2 程序说明

1. **注释**

   在编程语言中，注释是一种说明性的语句，它不会执行。在python中注释的方式有两种：

   - 单行注释，格式是以`#`开头一直到行尾的都属于是注释，这种格式的注释==不可以换行==

     ```python
     # 这是一条注释
     print("hello")   #注释也可以写在一条语句的后面
     ```

   - 多行注释，格式，用 一对 `'''` （这是三个单引号）括起来的都属于注释，多行注释可以换行

     ```ptyhon
     '''
     这是
     多行
     注释
     '''
     print("hello")
     ```

   > 注意： python程序中使用的标点符号都英文标点符号，大部分编程语言都是使用的英文标点符号的。
   >
   > 但输出部分的字符可以使用中文



2. **字符串**

   字符串，从字面意思上来说就是一串字符，通常我们打印输出字符串都是使用 `print()` 语句，但是不能直接的`()` 中写入字符串的内容，还需要使用引号将字符串括起来，引号是语法的一部分。

   **单引号**，使用单引号将字符串括起来，引号内可以写任意的字符，只要可以输出打印的字符都可以的。

   **双引号**，和单引号的使用没有区别，两者一样的，是可以替换的。

   **三引号** ,可以是三个单引号`'''`或三个双引号`"""` .三引号主要是用来打印多行字符

   

3. **转义字符**

   我们需要打印这样一句话 `It's OK!` ,可以看到这句话中是有一个单引号的，打印单引号，这里有两种方法，第一种，就是使用双引号或是三引号将我们需要的打印的字符串括起来；第二种就是使用转义字符，

   转义字符的形式是： `\` +` 需要打印的字符。 比如打印 单引号 ` '`，输入 `\'` 

   ```python
   print('It\'s OK!')  #输出 It's OK!
   ```

   如果说需要输出 `\` ,那需要使用 `\\` 来实现

   ```python
   print('输出 \\')  # 打印：  输出 \
   ```

   常用的转义字符

   | 转义字符 |     说明     | 转义字符 | 说明 |
   | :------: | :----------: | :------: | :--: |
   |   `\\`   |      \       |   `\'`   |  '   |
   |   `\n`   |     换行     |   `\"`   |  "   |
   |   `\t`   | 制表符（tab) |   `\b`   | 退格 |
   |   `\r`   |     回车     |   `\a`   | 响铃 |
   |          |              |          |      |





## 2. 变量

变量就是用来存储某个数据所定义的一个==标识符==。比如说我们有一个表示某个人名字的字符串`"Tom"`, 这是为了方便我们可以给这个字符串起一个名字，就叫 `name`, 给了字符串一个名字我们就可以使用`print()`的时候就可以直接在括号里输入`name`. 当然，我们还可以给某个数一个标识符，下面的程序中是变量定义的格式

```python
#变量定义格式
#变量名 = 数据
name = "Tom"		#定义了一个叫name的变量，其初始值是 “Tom”
age = 18			#定义了一个叫age的变量，其初始值是 18
print("我是" + name)
print(age, "岁。")
```

变量命名需要并不是没有任何限制的，需要遵守以下的规则：

* 第一个字符必须是字母（大写和小写）或下划线 `__`
* 其他部分（除第一个字符）可以是字母，数字下划线
* 标识符名称区分大小写，比如 `Name` 和 `name` 是两个不同的标识符（变量）
* 标识符（变量名）不能包含空格
* 标识符（变量名）不能使用python的关键字和保留字



> 更多的变量名使用建议和规范的命名方是会在各个部分提及



## 3. 数据类型

在数学的概念里，我们对数有不同的分类。而在python这门编程语言中，我们将数大致的分为两类，分别是 `整型` 和 `浮点型`

**整型**

整型类似于数学概念上的整数，比如 `1`  `5` `-10` `204` 这些数，我们就叫做整型数据



**浮点型**

Python将带小数点的数字都称为浮点数，比如 `1.2` `2.0` `5.9` 这些都叫做浮点型数据



**布尔型**

布尔型只有两个取值，`True`和`Flase`



>  Python是一种弱类型的语言，就是在声明变量是不需要指定数据的类型， 比如声明一个变量 `a = 19` ,Python解释器会自动的把 `a` 变量看做是一个整型数据。对于强类型的语言，比如 c，声明一个变量需要指定数据类型， `int b = 10;` 表示声明一个名为 `b` 的整型变量。



## 4. 运算符和表达式



### 4.1 运算符

在数学中，运算符有加减乘除等，同样在python中也支持这些运算符，下面是python可用运算符的速览：

**算数运算符**

* `+` 加，比如 `2+5` 输出 `7`, `'a'+'b'` 输出 `ab`
* `-` 减， 比如 `5-3` 输出 `2`
* `*` 乘，比如 `2*2` 输出 `4`
* `**` 乘方， 比如 `3**2` 表示 `3的2次方` 计算的结果是 `9`
* `/` 除， `13/3` 输出 `4.333333333333333`
* `//` 整除，两数相除对结果向下取整至最接近的整数， `13 // 3` 输出 `4`
* `%` 取模，计算余数， `13%3` 计算的结果是 `1`



**位运算符**

- `<<` 左移，将数字的位向左移动指定的位数，`2 << 2`输出 `8` 。 2 用二进制数表示为10向左移 2 位会得到1000 这一结果，表示十进制中的 8 。

- `>>` 右移，将数字的位向右移动指定的位数。`11 >> 1` 输出 `5` ，11 在二进制中表示为 1011 ，右移一位后输出 101 这一结果，表示十进制中的5 
- `&`  按位与，对数字进行按位与操作，`5 & 3` 输出 `1` 
- `| `  按位或，对数字进行按位或操作，`5 | 3` 输出 `7` 
- `^ ` 按位异或，对数字进行按位异或操作，`5 ^ 3 `输出 `6` 
- `~ `  按位取反，`x `的按位取反结果为 `-(x+1)`，`~5` 输出 `-6 `



**逻辑运算符**

- `< ` 小于，返回 x 是否小于 y。所有的逻辑运算符返回的结果均为 `True `或 `False` 。`5 < 3` 输出 `False` ，`6` 输出`True` 。比较可以任意组成组成链接： `3 < 5 < 7` 返回 `True` 
- `<` 大于，返回 x 是否大于 y。`5 > 3` 返回 `True `。如果两个操作数均为数字，它们首先将会被转换至一种共同的类型。否则，它将总是返回 `False`
- `<= `小于等于，返回 x 是否小于或等于 y。`x = 3; y = 6; x<=y` 返回 `True` 
- `>=  ` 大于等于返回 x 是否大于或等于 y。`x = 4; y = 3; x>=3` 返回 `True` 
- `== `（等于）比较两个对象是否相等。`x = 2; y = 2; x == y` 返回 `True`  ;`x = 'str'; y = 'stR'; x == y` 返回 `False` 。`x = 'str'; y = 'str'; x == y` 返回 `True` 
- `!=` 不等于，比较两个对象是否不相等，`x = 2    y = 3   x != y` 返回 `True` 。
- `not`  布尔“非”，如果 `x` 是 `True` ，则返回 `False` 。如果 `x` 是 `False` ，则返回 `True` 
- `and`  布尔“与”，如果 `x` 是 `False` ，则 `x and y` 返回 `False` 
- `or ` 布尔“或”，如果 `x` 是 `True` ，则返回 `True` ，否则它将返回 y 的计算值。`x = Ture; y = False; x or y` 将返回 `Ture` 



**赋值运算符**

* `=` 赋值，将一个数值给一个变量，或是一个变量的值给另一个变量， `a = 5` 表示给变量 `a` 赋值为 `5`, `a = 5;  b = a` 表示把 `a` 的值赋给 `b`，此时  a和b都为5
* `+=` 表示是加上一个数再赋值，例如 `a += 3` 等价于 `a = a + 3` 
* `*=` , `a *= 3` 等价于 `a =  a * 3`
* `/=`,  `a /= 3` 等价于 `a = a / 3`
* `%=`,  `a %= 3` 等价于`a = a % 3`

> 注意：以上各个符号和等号之间是没有空格的，这些运算符是一个整体的。



### 4.2 运算顺序

本表格参考 [Python参考手册](https://docs.python.org/3/reference/expressions.html#operator-precedence) 截取了部分常用的，优先级从上到下逐渐减小

| 运算符                           | 描述                           |
| -------------------------------- | ------------------------------ |
| `**`                             | 乘方                           |
| `+` (正号)，`-`(负号)，`~`(取反) | 正号，负号，取反都是一元运算符 |
| `*`,`/` , `//` ，`%`             | 乘，除，整除，取模             |
| `+`, `-`                         | 加，减                         |
| `<<`, `>>`                       | 左移，右移                     |
| `&`                              | 按位与                         |
| `^`                              | 按位异或                       |
| `|`                              | 按位或                         |
| `<`,`<=`,`>`,`>=`,`!=`,`==`      | 逻辑比较运算符                 |
|                                  |                                |





### 4.3 表达式

表达式就是数据和运算符组成的语句

**示例**（expression.py）

```python
length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))

```

输出

```shell
$ python expression.py
Area is 10
Perimeter is 14
它是
```





## 5. 控制流

到目前为止，我们接触到的程序还都只是按我们写的顺序从头到尾的一条一条执行。这的确很符合我们的思考和书写阅读习惯，但是对于一门能够解决实际问题的编程语言来说这是完全不够的，所以我们还需要学会使用语言给我们提供的控制流语句，所谓控制流语句就是是程序可以不用按顺序执行而是可以跳转到我们指定的位置执行。

python支持的控制流语句和大多属于语言一样，有分支判断语句`if`,循环语句 `for` 和 `while`



### 5.1 `if` 语句

`if` 语句用于检查条件：如果条件为真 （True），则执行语句块，如果为假（Flase）则执行另一个语句块

格式： 

```python
#1. if
if condition:
    #statement、

#2. if-else
if conditon:
    #statement
else:
    #statement
    
#3. if-elif
if condition:
    #statement
elif condition:
    #statement
else:
    #statement

```



**示例** （if.py）

```python
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
	# 新块从这里开始
	print('Congratulations, you guessed it.')
	print('(but you do not win any prizes!)')
	# 新块在这里结束
elif guess < number:
	# 另一代码块
	print('No, it is a little higher than that')
	# 你可以在此做任何你希望在该代码块内进行的事情
else:
	print('No, it is a little lower than that')
	# 你必须通过猜测一个大于（>）设置数的数字来到达这里。
print('Done')
# 这最后一句语句将在
# if 语句执行完毕后执行。
```

输出

```shell
$ python if.py
Enter an integer : 50
No, it is a little lower than that
Done
$ python if.py
Enter an integer : 22
No, it is a little higher than that
Done
$ python if.py
Enter an integer : 23
Congratulations, you guessed it.
(but you do not win any prizes!)
Done
```



### 5.2 `while` 语句

在上面的示例中，我们可以看到，这个程序只能执行一次，如果需要继续猜我们设置的数字的话就得重新执行程序。为了解决这个问题，我们需要用到 `while` 循环语句，让程序的不断执行部分的语句块，知道我们猜对正确的数字为为止。

`while` 语句格式

```python
while condition:
    #statement
```



**示例** （while.py）

```python
number = 23
running = True
while running:
	guess = int(input('Enter an integer : '))
	if guess == number:
		print('Congratulations, you guessed it.')
		# 这将导致 while 循环中止
		running = False
	elif guess < number:
		print('No, it is a little higher than that.')
	else:
		print('No, it is a little lower than that.')
        
print('The while loop is over.')
# 在这里你可以做你想做的任何事
    
print('Done')

```

输出

```shell
$ python while.py
Enter an integer : 50
No, it is a little lower than that.
Enter an integer : 22
No, it is a little higher than that.
Enter an integer : 23
Congratulations, you guessed it.
The while loop is over.
Done
```



### 5.3 `for` 语句

`for` 语句和`while` 一样也是循环语句，但是`for` 循环可以指定循环的次数

语句格式： `for ... in`

示例1（for1.py)打印数字1-5

```python
for i in range(1,6):
    print(i)
print("The for loop is over")
```

输出：

```shell
$ python for1.py
1
2
3
4
5
The for loop is over
```



示例2（for2.py)，改进while.py，使得只有三次机会

```python
number = 23
running = True
for i in range(1,4):
	guess = int(input('Enter an integer : '))
	if guess == number:
		print('Congratulations, you guessed it.')
		# 这将导致 while 循环中止
		running = False
	elif guess < number:
		print('No, it is a little higher than that.')
		print("you have " + str(3-i) + " times to try")
	else:
		print('No, it is a little lower than that.')
		print("you have " + str(3-i) + " times to try")
        
print('The while loop is over.')
# 在这里你可以做你想做的任何事
    
print('Done')
```







### 5.4 `break`  和 `continue`  语句

`break` 语句用以中断循环语句，这种中断是无条件的中断，即使循环条件没有变更为 `False` ，或是队列中的项目还没有迭代完。

示例 （break.py)

```python
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
```



`continue` 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭代。

示例（continue.py)

```python
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
print('Input is of sufficient length')
# 自此处起继续进行其它任何处理
```















