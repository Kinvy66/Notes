# 第9章  顺序容器



C++的STL可分为六个部件，分别是容器，分配器，算法，迭代器，适配器，仿函数。本章的内容主要讲使用平时比较多的容器，而容器又分为顺序容器和关联容器，这章主要是顺序容器，关联容器在第11章有详细的讲解。

一个容器就是一些特定类型对象的**集合**。 **顺序容器** 是指这些集合中的元素位置是和我们放入容器中的顺序相关的，而且这些元素在内存中是 "连续"的（这里的连续可以是物理空间的连续和逻辑连续）。





## 1. 顺序容器概述

下表是标准库中提供的所有的顺序容器

![image-20220508133428109](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220508133428109.png)

<span style="border:2px solid Red; border-radius:5px;">C++11</span> 其中 `forward_list` 和 `array` 是新 C++ 标准增加的类型。

array 与内置数组相比，是一种更安全、更容易使用的数组类型。与内置数组类似，array的大小是固定的。因此array不支持添加和删除以及改变容器大小的操作。

forward_list是一个单向链表的数据结构，它没有size操作。



##### 确定使用哪种顺序容器

 <span style="background: yellow">通常，使用 vector 是最好的选择，除非你有很好的理由选择其他容器</span>

关于容器的选择，在你不了解的这些容器底层实现使用的数据结构情况下，`vector` 是你的首选。书中也给出了一些选择容器的基本原则，这些原则都是基于容器底层数据结构的特性。我这里就不罗列这些了，只要了解每个容器的底层实现也就自然知道在不同的需求选择哪个合适的容器。

## 2. 容器库概览

容器类型的操作，某些操作是所有容器类型都提供的；另外一些操作仅对顺序容器、关联容器或无序容器；还有一些操作只适用于一小部分容器。

本小结介绍使用于**所有容器**的操作和仅使用于**顺序容器**的操作。

在第3章我们已经使用过 `vector` 容器，其他容器的使用也类似，使用这些容器都需要包含对应的头文件，头文件名称和容器名称一样。容器类型都是模板类，我们声明容器时需要指定元素的类型。

例如：

```cpp
list<Sales_data> s;		// 保存 Sales_data 对象的list
deque<double> d;		// 保存 double 的 deque
vector<vector<string>> lines;	// vector 的vector
```

<span style="border:2px solid Red; border-radius:5px;">C++11</span> 较旧的编译器（不支持C++11以上的版本) 可能需要在两个尖括号之间加上空格， 例如 `vector<vector<string> >`  



虽然我们可以在容器中保存几乎任何类型，但某些容器的操作对元素类型有其自己的特殊要求。也就是说我们使用自己定义的类型作为容器元素，容器的有些操作没有在自定义中的类型定义，那么就不能使用这些操作。例如，容器支持 `<` 关系运算，而我们自定义的类型（如 Sales_data类）并没有定义 `<` ,这时就不能使用这个运算符（虽然容器支持）。

另外一个例子，

```cpp
// 假定 noDefault 是一个没有默认构造函数的类型
vector<noDefault> v1(10, init);    // 正确： 提供了元素初始化器
vector<noDefault> v2(10);		   // 错误： 调用默认构造函数初始化，但是该类型没有定义默认构造函数
```



下表是所有容器共有的操作

![image-20220509110552713](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220509110552713.png)

![image-20220509110612134](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220509110612134.png)



### 2.1 迭代器

<span style="background: yellow"> 迭代器可以看作是一种特殊的指针</span>

迭代器的基本操作在第3章有讲解，比如解引用`*` ，递增  `++` 等一系列的操作，其中有些操作时某些容器不支持的。在表3.6中是迭代器支持的所有操作，其中有一个例外，forward_list 迭代器不支持递减运算符 （`--`)。表3.7列出来了迭代器支持的算术运算符，这些运算只能用于 string、vector、deque和arrary迭代器

![image-20220509185604269](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220509185604269.png)

![image-20220509185623707](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220509185623707.png)



#### 迭代器的范围

一个**迭代器范围**是有一对迭代器表示，两个迭代器分别指同一个容器的元素或者尾元素之后的未知，这两个迭代器通常被称为 `begin` 和 `end` ，如下图所示

![image-20220509191901004](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220509191901004.png)



`begin` 迭代器指向的是容器的第一个元素，对其解引用操作就可以获取到容器第一个位置元素的值；

`end` 迭代器指向的是容器最后一个元素的<span style="background: yellow">后一个位置</span> , 对其解引用是无法获取到任何元素的。

这种元素范围被称为**左闭区间**， 用数学符号描述为:  $[\tt{begin, end})$



#### 使用左闭和范围蕴含的编程假定

使用左闭范围主要是为了方便迭代元素，这种范围具有以下三种性质：

- 如果 begin 与 end 相等，则范围为空
- 如果 begin 与 end 不等，则范围至少包含一个元素，且 begin 指向该范围的第一个元素
- 我们可以对 begin 递增若干次， 使得 begin == end

示例代码

```cpp
while(begin != end) {
	*begin = val;	// 正确： 范围非空， 因此 begin 指向一个元素
    ++begin;		// 移动迭代器， 获取下一个元素
}
```



### 2.2 容器类型成员

下面是容器定义的类型，在这之前我们已经使用过了 `size_type` 、`iterator` 和 `const_iterator`

![image-20220509194452634](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220509194452634.png)

使用这些类型，我们必须显示说明容器具体的类型

```cpp
// iter 是通过 list<string> 定义的一个迭代器类型
list<string>::iterator iter;
// count 是通过 vector<int> 定义的一个 difference_type 类型
vector<int>::difference_type count;
```

通常具体容器的类型别名写起来比较麻烦，一般我们会使用自动类型推断 `auto` 或 `decltype`



### 2.3 begin 和 end 成员

begin 和 end 有多个版本：带 `r` 版本返回反向迭代器；以 `c` 开头的版本返回 `const` 迭代器

示例：

```cpp
list<string> a = {"Milton", "Shakespeare", "Austen"};
auto it1 = a.begin();		// list<string>::iterator
auto it1 = a.rbegin();		// list<string>::reverse_iterator
auto it1 = a.cbegin();		// list<string>::const_iterator
auto it1 = a.crbegin();		// list<string>::const_reverse_iterator
```

不以 `c` 开头的 函数都是被重载过的。也就是说，实际上有两个名为 begin 的成员，一个返回常量成员，一个返回非常量成员。

当 `auto` 与 `begin` 或 `end` 结合使用时，获得的迭代器类型依赖于容器类型，与我们想要如何使用迭代器毫不下相干，如果想使用 `const` 版本可以显示的声明。

```cpp
auto it = a.being();	// it的类型取决于a的类型
```

<span style="background: yellow">当不需要写访问时，应使用 cbegin 和 cend</span>



### 2.4 容器定义和初始化



















