# Lab01



## Problem1: Fix the Bug

问题1是修改下面的函数使得功能正确

```python
def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a and b % 2 == 1 # You can replace this line!
```

这个给出的函数的功能是判断`a` , `b` 两个数是否都为奇数

显然，由数学知识我们知道一个整数为奇数的话，那么应该满足"不能被2整除"这个条件，而用python表示就是

`x % 2 == 1`  ,  a, b 都要满足这个条件所以修改的代码:

```python
return a % 2 == 1 and b % 2 == 1
```

测试

> `python ok -q both_odd` 



## Problem2: Factorial

写一个函数，计算阶乘。函数接收一个参数 `n` ，需要返回结果是 $n!$ 即 $1\times 2 \times 3\dots \times (n-1)\times n$ .

```python
def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    pass  # YOUR CODE HERE
```

这个问题有两种解法，分别是非递归和递归

**非递归**

我们很容易就能想到使用循环，循环的计数 1~n，每计一个就乘起来，代码如下

```python
result = 1
    while n > 1:
        result *= n
        n -= 1   
return result 
```

循环可以用 `while` 和 `for` 两者都可以实现，这里设置了一个结果的初始值 `result = 1` 

> Tips ： 计算累乘，一般初始值设置为 1, 计算累加一般设置为 0



**递归**

递归要注意的就是需要有终止条件，这里的终止条件就是 当 `n == 1`

```python
if n == 1:
        return 1
return factorial(n-1) * n
```

递归后面好像还有单独的lab



## Problem3: Is Triangle?

写一个函数，给定三个值，判断是否可以组成一个三角形

数学知识: 给定三边（正值），==任意==两边之后大于第三边才能构成一个三角形

```python
def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    pass  # YOUR CODE HERE
```

有一点需要注意的， `a, b, c` 的值不一定是正值，只要出现一个负值就是 `False` , 所以首先就需要判断是否有负值，这里判断负值是求三个数的最小值，当然我们也可以把三个值大于0的条件用 `and` 组合 

```python
if min(a, b, c) <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True
```



## Problem 4: Number of Six

写一个函数计算一个正整数中有几个 `6`

```python
def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    """
    pass  # YOUR CODE HERE
```

这个问题就是取出一个多位数的每一位的数字，计数其中有几个 `6`

```python
count = 0
while n > 0:
    if n % 10 == 6:
        count += 1
     n = n // 10
return count
```

一般取一个多位数的每一位的数字这种问题都是使用 `%` (取余) 和 `//` (整除）运算

 先取出个位数  `n % 10`  判断是否为 `6` 如果是的话就计数加一，然后用取整运算把个位剔除，因为我们不知道传入的数是几位的，所以这里使用了 `while` 循环。传入的参数会被逐位剔除，所以循环退出的条件就是 `n==0`



## Problem 5: Max Digit

写一个函数，找出一个非负整数中最大的数字，和上一个问题有一定关联，都是需要分解一个多位数

```python
def max_digit(x):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    pass  # YOUR CODE HERE

```

基本和上一个问题一样，唯一不同的是这里需要找一个最大的值，我们定义一个最大的值 `max_num = 0` , 如果说取出的数字有比前一次的值大就替换掉 `max_num`

```python
max_num = 0
while x > 0:
    if x % 10 > max_num:
        max_num = x % 10
        x = x // 10
return max_num
```

