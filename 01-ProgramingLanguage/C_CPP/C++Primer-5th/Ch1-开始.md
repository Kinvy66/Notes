# 第1章	开始

第一章是C++的概览

## 1. 一个简单的C++程序

从一个简单的C++程序开始

```c++
int main()
{
    return 0;
}
```

由这个程序简单的介绍了函数的定义。

简单的介绍了c++程序在不同的平台编译运行的方式。



## 2. 输入和输出

c++的输入和输出 `cin` `cout` 以及对应的运算符 `<<` `>>`

```c++
std::cout << "hello" << std::endl;
std::cin >> val;
```



## 3. 注释

c++的注释两种：

```c++
//注释1
std::cout << "hello" << std::endl;
/*
注释2
*/
std::cin >> val;
```



## 4. 控制流

循环和判断语句

### 4.1 while



### 4.2  for



### 4.3 if



### 一个示例

读取一串数据并统计每个数字出现的次数 ，windows下的终止键 `ctrl` + `z` 

```c++
#include <iostream>
using namespace std;
int main()
{
	int currVal = 0, val = 0;
	if (cin >> currVal) {
		int cnt = 1;
		while (cin >> val) {
			if (val == currVal) {
				++cnt;
			}
			else {
				cout << currVal << " occurs "
					<< cnt << " times" << endl;
				currVal = val;
				cnt = 1;
			}
		}
		cout << currVal << " occurs "
			<< cnt << " times" << endl;
	}
	system("pause");
	return 0;
}
```



## 5. 类的简介

用书店的示例简单的介绍了类，这里使用的类 `Sales——item` 是已经写好的，所以应该说这小节是使用类。

类就是一种数据类型，叫做 `类类型` ，它和我们使用的普通数据类型一样，同样有 `+`, `-`, `*` , `/` 等基本运算，甚至还有 `>>` 和　`<<` ，这些运算符都是通过 `重载运算符` 操作实现的。不过在这里好像并没有提及运算符的重载。







