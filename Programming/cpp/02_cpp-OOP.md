# C++核心编程--面向对象



## 1. 内存分区模型

C++ 程序执行时，将内存划分为**4个区域**

* 代码区：存放函数体的二进制代码，有操作系统进行管理
* 全局区：存放全局变量和静态变量以及常量
* 堆区：由编译器自动分配释放，存放函数的参数值，局部变量等
* 堆区：有程序员分配和释放，若程序员不释放，程序结束时有操作系统回收



### 1.1 程序运行前

在程序编译后，生成了exe可执行程序，未执行该程序前分为两个区

**代码区：**

​	存放CPU执行的机器指令

​	代码区是**共享**的，共享的目的是对于频繁被执行的程序，只需要在内存中有一份代码即可

​	代码区是**只读**的，使其只读的原因是防止程序意外地修改了它的指令

**全局区：**

​	全局变量和静态变量存放在此。

​	全局区还包含了常量区，字符串常量和其他常量也存放在此

​	==该区域的数据在程序结束后由操作系统释放==





**示例:**

```c++
#include <iostream>

using namespace std;

//全局变量
int g_a = 10;
int g_b = 10;

//全局常量
const int c_g_a = 10;
const int c_g_b = 10;

int main()
{
	//局部变量
	int a = 10;
	int b = 10;

	//打印地址
	cout << "局部变量a地址：" << (int)&a << endl;
	cout << "局部变量b地址：" << (int)&b << endl;

	cout << "全局变量g_a地址：" << (int)&g_a << endl;
	cout << "全局变量g_b地址：" << (int)&g_b << endl;

	//静态变量
	static int s_a = 10;
	static int s_b = 10;

	cout << "静态变量s_a地址：" << (int)&s_a << endl;
	cout << "静态变量s_b地址：" << (int)&s_b << endl;

	cout << "字符串常量地址：" << (int)&"hello world" << endl;
	cout << "字符串常量地址：" << (int)&"hello world1" << endl;

	cout << "全局常量c_g_a地址：" << (int)&c_g_a << endl;
	cout << "全局常量c_g_b地址：" << (int)&c_g_b << endl;

	const int c_l_a = 10;
	const int c_l_b = 10;
	cout << "局部常量c_l_a地址：" << (int)&c_l_a << endl;
	cout << "局部常量c_l_b地址：" << (int)&c_l_b << endl;

	system("pause");
	
	return 0;

}
```



**打印结果:**

![image-20210530113103121](C:/Users/Kinvy/AppData/Roaming/Typora/typora-user-images/image-20210530113103121.png)



总结:

* C++中程序运行前分为全局区和代码区
* 代码区特点是共享和只读
* 全局区中存放全局变量，静态变量，常量
* 常量区中存放const修饰的全局常量和字符串常量





### 1.2 程序运行后

**栈区:**

​	由编译器自动分配释放，存放函数的参数值，局部变量等

​	注意事项：不要返回局部变量的地址，栈区开辟的数据由编译器自动释放



**示例：**

```c++
#include <iostream>

using namespace std;

int* func()
{
	int a = 10;
	return &a;
}

int main()
{
	int* p = func();

	cout << *p << endl;    //打印10，编译器对改地址的数据做了一次保留
	cout << *p << endl;	  //打印无效数据，栈区数据已释放

	system("pause");

	return 0;
}
```





**堆区：**

​	由程序员分配释放，若程序员不释放，程序结束时有操作系统回收

​	在C++中主要利用 `new` 在堆区开辟内存，用 `delete` 释放内存



**示例:**

```c++
#include <iostream>

using namespace std;

int* func()
{
	int* a = new int(10);
	return a;
}

int main()
{
	int* p = func();

	cout << *p << endl;
	cout << *p << endl;

	delete p;

	//cout << *p << endl;		//报错，p已释放无法访问

	system("pause");

	return 0;
}
```



注: 开辟和释放数组

```c++
int* arr = new int[10];		
delete[] arr;		
```







## 2. 引用

### 2.1 引用的基本使用

**作用：** 给变量取别名

**语法：** `数据类型 &别名 = 原名`



**示例:**

```c++
#include <iostream>

using namespace std;

int main()
{
	int a = 10;
	int b = 20;
	//int& c;			//错误，引用必须初始化
	int& c = a;			//一旦初始化不可以更改			

	c = b;				//此处是赋值操作，对别名c对于的变量a赋值，而不是更改引用
	cout << "a = " << a << endl;
	cout << "b = " << b << endl;
	cout << "c = " << c << endl;

	system("pause");

	return 0;
}
```



**注意：**

* 引用必须初始化
* 引用在初始化后，不可以改变



### 2.2 引用做函数参数

函数传参时，可以利用引用的技术让形参修饰实参，简化指针修改实参。==引用的实质是指针常量==

示例：

```c++
#include <iostream>

using namespace std;

void swap(int& a, int& b)
{
	int temp = a;
	a = b;
	b = temp;
}

int main()
{
	int a = 10;
	int b = 20;

	swap(a, b);
	cout << "a = " << a << "\tb = " << b << endl;

	system("pause");

	return 0;
}
```



### 2.3 引用做函数的返回值

作用： 引用是可以作为函数的返回值存在的

注意：**不要返回局部变量引用**

用法: 函数调用作为左值



**示例:**

```c++
#include <iostream>

using namespace std;

//返回局不变量引用
int& test01()
{
	int a = 10;
	return a;
}

//返回静态变量引用
int& test02()
{
	static int a = 20;
	return a;
}

int main()
{
	//不能返回局部变量的引用
	int& ref = test01();
	cout << "ref = " << ref << endl;  //与指针一致，同样编译器做了一次保留
	cout << "ref = " << ref << endl;

	//如果函数做左值，那么必须返回引用
	int& ref2 = test02();
	cout << "ref2 = " << ref2 << endl;
	cout << "ref2 = " << ref2 << endl;
	
	//函数做左值
	test02() = 1000;		//等同于赋值给ref2
	cout << "ref2 = " << ref2 << endl;
	cout << "ref2 = " << ref2 << endl;

	system("pause");

	return 0;
}
```







### 2.4 常量引用



**作用:** 常量引用主要用来修饰形参，防止误操作



在函数形参列表中， 可以加==const修饰形参==，防止形参改变实参



**示例：**

```c++
#include <iostream>

using namespace std;

void showValue(const int& v)
{
	//v += 10;
	cout << v << endl;
}

int main()
{
	//int& ref = 10;		//错误，引用本身需要一个合法的内存空间
	//加入const就可以了，编译器优化代码,  int temp = 10; const int& ref = temp;
	const int& ref = 10;

	//ref = 100;		//加入const后不可以修改变量

	//函数中利用常量引用防止误操作修改实参
	int a = 10;
	showValue(a);

	system("pause");

	return 0;
}
```





## 3. 类和对象

C++面向对象的三大特性为：==封装、继承、多态==



### 3.1 封装

#### 3.1.1 封装的意义

**封装的意义一：**将实物的属性和行为写一起，以类的形式在程序中体现封装

**语法:** `class 类名{访问权限: 属性 / 行为}`



**示例1：** 设计一个圆类，求圆的周长

```c++
#include <iostream>
using namespace std;
const double PI = 3.14;

class Circle 
{
public:
	//属性
	int m_r;	//半径

	//行为
	//获取圆的周长
	double calculateZC()
	{
		return 2 * PI * m_r;
	}

};

int main()
{

	Circle c1;
	c1.m_r = 10;
	cout << "圆的周长: " << c1.calculateZC() << endl;

	system("pause");

	return 0;
}
```



**封装的意义二:** 可以把属性和行为放在不同的权限下，加以控制

访问权限有三种：

1. public			公共权限，类内可以访问，类外可以访问
2. protected    保护权限，类内可以访问，类外不可以访问
3. private        私有权限，类内可以访问，类外不可以访问

示例略



#### 3.1.2 struct和class区别

在c++中struct和class唯一的区别就在于**默认的访问权限不同**

* struct默认访问权限为公共
* class默认访问权限为私有





### 3.2  构造函数和析构函数



#### 3.2.1  基本语法

构造函数一般用来初始化类，析构函数则是完成清理工作，**我们不提供构造和析构，编译器会提供，编译器提供的构造和析构是空实现**

* 构造函数：主要作用在于创建对象是为对象成员属性赋值，构造函数有编译器自动调用，无须手动调用
* 析构函数：主要作用在于对象销毁前系统自动调用，执行一些清理工作



**构造函数语法:** `类名(){}`

1. 构造函数，没有返回值，也不写void
2. 函数名称与类名相同
3. 构造函数可以没有参数，因此可以发生重载
4. 程序在调用对象时候会自动调用构造，无须手动调用，而且只会调用一次



**析构函数语法:** `~类名(){}`

1. 析构函数，没有返回值也不写void
2. 函数名称与类名相同，在名称前加上符号 `~`
3. 析构函数不可以有参数，因此不可以发生重载
4. 程序在对象销毁前自动调用析构，无须手动调用，而且只会调用一次



```c++
#include <iostream>
using namespace std;
const double PI = 3.14;

class Person 
{
public:
	Person()
	{
		cout << "构造函数调用" << endl;
	}

	~Person()
	{
		cout << "析构函数调用" << endl;
	}

};

void test01()
{
	Person p;
}

int main()
{

	test01();

	system("pause");

	return 0;
}
```





#### 3.2.2 构造函数的分类及调用

两种分类方式：

​	按参数分为：有参构造和无参构造

​	按类型分为：普通构造和拷贝构造

三种调用方式：

​	括号法

​	显示法

​	隐式转换法



```c++
#include <iostream>
using namespace std;
const double PI = 3.14;

class Person 
{
public:
	//无参（默认）构造
	Person()
	{
		cout << "无参构造函数调用" << endl;
	}

	//有参构造
	Person(int a)
	{
		cout << "有参构造函数调用" << endl;
	}

	//拷贝构造
	Person(const Person& p)
	{
		age = p.age;
		cout << "拷贝构造函数调用" << endl;
	}

	~Person()
	{
		cout << "析构函数调用" << endl;
	}

public:
	int age;

};

//调用无参构造
void test01()
{
	Person p;
}

//调用有参构造
void test02()
{
	//1，括号法常用
	Person p1(10);		
	//注意1：无参构造不能加括号，如果加了编译器会认为是一个函数声明
	//Person p2();		//会被认为函数p2返回值是Person类

	//2，显示法
	Person p2 = Person(10);
	Person p3 = Person(p2);
	//Person(10)单独写就是匿名对象  当前行结束之后，马上析构

	//3，隐式转换法
	Person p4 = 10;		//Person p4 = Person(10);
	Person p5 = p4;		//Person p5 = Person(p4);

	//注意2：不能利用拷贝构造函数  初始化匿名对象  编译器认为是对象声明
	//Person p5(p4);

}

int main()
{

	//test01();

	test02();

	system("pause");

	return 0;
}
```



#### 3.2.3 构造函数调用规则

默认情况下，c++编译器至少给一个类添加3个函数

1. 默认构造函数（无参，函数体为空）
2. 默认析构函数（无参，函数体为空）
3. 默认拷贝构造函数，对属性进行==值拷贝==



构造函数调用规则如下：

* 如果用户定义有参构造函数，c++不再提供默认无参构造，但是会提供默认拷贝构造
* 如果用户定义拷贝构造函数，c++不会再提供其他构造函数







#### 3.2.4  深拷贝与浅拷贝

浅拷贝：简单的赋值拷贝操作

深拷贝：在堆区重写申请空间，进行拷贝操作

**在类中用了指针变量一般都需要使用深拷贝**



```c++
#include <iostream>
using namespace std;
const double PI = 3.14;

class Person 
{
public:
	//无参（默认）构造
	Person()
	{
		cout << "无参构造函数调用" << endl;
	}

	//有参构造
	Person(int age, int height)
	{
		cout << "有参构造函数调用" << endl;
		m_age = age;
		m_height = new int(height);
	}

	//拷贝构造
	Person(const Person& p)
	{
		cout << "拷贝构造函数调用" << endl;
		//如果不利于深拷贝在堆区创建新内存，会导致浅拷贝带来的重复释放堆区问题
		m_age = p.m_age;
		m_height = new int(*p.m_height);
	}

	~Person()
	{
		cout << "析构函数调用" << endl;
		if (m_height != nullptr) {
			delete m_height;
		}
	}

public:
	int m_age;
	int* m_height;

};

void test01()
{
	Person p1(18, 180);
	Person p2(p1);

	cout << "p1 age :" << p1.m_age << "\t p1 height:" << *p1.m_height << endl;
	cout << "p2 age :" << p2.m_age << "\t p2 height:" << *p2.m_height << endl;

}

int main()
{

	test01();

	system("pause");

	return 0;
}

```



注：

==**在类中有指针变量时，使用浅拷贝的话，调用拷贝函数创建的新实例会和原有的实例指向同一个内存地址，只是名字不一样而已，在修改属性值和释放堆区内存空间是就不能实现预期的操作**==



#### 3.2.5 初始化列表

C++提供了初始化列表语法，用来初始化属性

**语法：** `构造函数(): 属性1(值1),属性2(值2)...{}`



**示例:**

```c++
#include <iostream>
using namespace std;
const double PI = 3.14;

class Person 
{
public:
	/*
	//传统方式初始化
	Person(int a, int b, int c)
	{
		m_A = a;
		m_B = b;
		m_C = c;

	}
	*/

	//初始化列表初始化
	Person(int a, int b, int c):m_A(a),m_B(b),m_C(c) {}
	
	void printPerson()
	{
		cout << "mA:" << m_A << endl;
		cout << "mB:" << m_B << endl;
		cout << "mC:" << m_C << endl;

	}

private:
	int m_A;
	int m_B;
	int m_C;

};

int main()
{
	Person p(1, 2, 3);
	p.printPerson();

	system("pause");

	return 0;
}
```





#### 3.2.6 类对象作为类成员

C++类中的成员可以是另一个类的对象，我们称改成员为对象成员

例如：

```c++
class A {}
class B 
{
    A a;
}
```



对于以上这种情况，A与B的构造和析构顺序，见下面示例

```c++
#include <iostream>
using namespace std;
const double PI = 3.14;

class A
{
public:
	A()
	{
		cout << "A 构造" << endl;
	}
	~A()
	{
		cout << "A析构" << endl;
	}
};

class B
{
public:
	B()
	{
		cout << "B 构造" << endl;
	}
	~B()
	{
		cout << "B析构" << endl;
	}

	A a;
};

void test01()
{
	B b;
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```



![image-20210530182757209](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210530182757209.png)







