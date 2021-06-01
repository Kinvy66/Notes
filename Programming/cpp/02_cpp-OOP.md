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



> 总结:
>
> * C++中程序运行前分为全局区和代码区
> * 代码区特点是共享和只读
> * 全局区中存放全局变量，静态变量，常量
> * 常量区中存放const修饰的全局常量和字符串常量





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

#### 3.2.7 静态成员

静态成员就是在成员变量和成员汉化苏前加上关键字static，称为静态成员

静态成员分为：

* 静态成员变量
  * 所有对象共享同一分数据
  * 在编译阶段分配内存
  * 类内声明，类外初始化
* 静态成员函数
  * 所有对象共享同一个函数
  * 静态成员函数只能访问静态成员变量



**示例1：** 静态成员变量

```c++
#include <iostream>
using namespace std;

class Person
{
public:
	static int m_A;  //静态成员变量

private:
	static int m_B;
};
int Person::m_A = 10;
int Person::m_B = 20;

void test01()
{
	//静态成员变量两种访问方式

	//1.通过对象
	Person p1;
	p1.m_A = 100;
	cout << "p1.m_A = " << p1.m_A << endl;

	Person p2;
	p2.m_A = 200;
	cout << "p1.m_A = " << p1.m_A << endl;
	cout << "p2.m_A = " << p2.m_A << endl;

	//2.通过类名
	cout << "m_A = " << Person::m_A << endl;

	//cout << "m_B = " << Person::m_B << endl;		//私有权限无法访问
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```



**示例2：**静态成员函数

```c++
#include <iostream>
using namespace std;

class Person
{
public:
	static void func()
	{
		cout << "func()" << endl;
		m_A = 100;

	}

	static int m_A;		//静态成员
	int m_B;

private:
	static void func2()
	{
		cout << "func2()" << endl;
	}
};
int Person::m_A = 10;

void test01()
{
	//静态函数两种访问方式

	//1.通过对象
	Person p1;
	p1.func();

	//2.通过类名
	Person::func();
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```





### 3.3 C++对象模型和this指针



#### 3.3.1 成员变量和成员函数分开存储



在c++中，类内的成员变量和成员函数分开存储

只有非静态成员变量才属于类的对象上

```c++
#include <iostream>
using namespace std;

class Person
{
public:
	Person()
	{
		mA = 10;
	}

	//非静态成员变量占对象空间
	int mA;
	//静态成员变量不占对象空间
	static int mB;
	//函数也不占对象空间，所有函数共享一个函数实例
	void func()
	{
		cout << "mA = " << this->mA << endl;
	}
	//静态成员函数也不占对象空间
	static void sfunc()
	{

	}
};

int main()
{
	cout << sizeof(Person) << endl;

	system("pause");

	return 0;
}
```



注：上面程序打印输出是 4 ,即只有非静态成员变量占用空间，==如果类中没有非静态成员变量，则类的大小为1==



#### 3.3.2  this指针概念

**this指针指向被调用的成员函数所属的对象**

this指针是隐含每一个非静态成员函数内的一种指针

this指针不需要定义，直接使用即可



this指针的用途：

* 当形参和成员变量同名是，可用this指针来区分
* 在类的非静态成员函数中返回对象本身，可使用 `return *this`



```c++
#include <iostream>
using namespace std;

class Person
{
public:
	Person(int age)
	{
		//1.当形参和成员变量同名是，可用this指针来区分
		this->age = age;
	}
	Person& PersonAddPerson(Person p)
	{
		this->age += p.age;
		//返回对象本身
		return *this;
	}

	int age;
};

void test01()
{
	Person p1(10);
	cout << "p1.age = " << p1.age << endl;

	Person p2(10);
	p2.PersonAddPerson(p1).PersonAddPerson(p1).PersonAddPerson(p1); //链式编程
	cout << "p2.age = " << p2.age << endl;
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```





#### 3.3.3 空指针访问成员函数

c++中空指针也是可以调用成员函数的，但是也要注意有没有用到this指针



**示例：**

```c++
#include <iostream>
using namespace std;

class Person
{
public:
	void showClassName()
	{
		cout << "Class Person" << endl;
	}
	void showPerson()
	{
		cout << m_age << endl;
	}

	int m_age;
};

void test01()
{
	Person* p = nullptr;
	p->showClassName();		//空指针，可以调用成员函数
	//p->showPerson;			//成员函数中m_age是隐含this的，而this是空，所以无法访问,可在成员函数加if判断this的空
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```



#### 3.3.4 const修饰成员函数

**常函数:**

* 成员函数后加const后我们称为这个函数为**常函数**
* 常函数内不可以修改成员属性



**常对象:	**

* 声明对象前加const称为该对象为常对象
* 常对象只能调用常函数



**示例:	**

```c++
#include <iostream>
using namespace std;

class Person
{
public:
	Person()
	{
		m_A = 0;
		m_B = 0;
	}

	//this指针的本质是一个指针常量，指针的指向不可修改
	//如果想让指针指向的值不可以修改，需要声明常函数
	void showPerson() const
	{
		//const Type* const pointer;
		//this = nullptr;		//不能修改指针的指向  Person* const this;
		//this->m_A = 100;	//但是this指针指向的对象的数据是可以修改的
		//const修饰成员函数，表示指针指向的内存空间的数据不能修改，除了mutable修饰的变量
		this->m_B = 100;
	}
	void myFunc()
	{
		m_A = 1000;
	}

public:
	int m_A;
	mutable int m_B;	//可修改，可变的

};

void test01()
{
	const Person p;		//常量对象
	cout << p.m_A << endl;
	//p.m_A = 100;		//常量对象不能修改成员变量的值，但可以访问
	p.m_B = 1000;		//但是常对象可以修改mutable修饰成员变量

	//常对象访问成员函数
	//p.myFunc();		//常对象不能调用普通的成员函数

}

int main()
{
	test01();

	system("pause");

	return 0;
}
```





### 3.4 友元

友元的目的是让一个函数或者类访问另一个类中私有私有成员



友元关键字==friend==



友元的三种实现：

* 全局函数做友元
* 类做友元
* 成员函数做友元



```c++
#include <iostream>
#include <string>
using namespace std;

class A;
class B
{
public:
	B();
	void b_func();
	void b_visit();

private:
	A* a;
};

class A
{
	friend void g_func(A* a);		//全局函数做友元
	friend class B;					//类做友元
	friend void B::b_visit();		//成员函数做友元
public:
	A()
	{
		this->m_A = "mA";
		this->m_B = "mB";
	}
public:
	string m_A;

private:
	string m_B;
};


B::B()
{
	a = new A;
}
void B::b_func()
{
	cout << "class B visit " << a->m_A << endl;
	cout << "class B visit " << a->m_B << endl;
}
void B::b_visit()
{
	cout << "class B b_visit() " << a->m_A << endl;
	cout << "class B b_visit()  " << a->m_B << endl;
}


//全局函数
void g_func(A* a)
{
	cout << "g_func() 访问" << a->m_A << endl;
	cout << "g_func() 访问" << a->m_B << endl;

}

//1.全局函数做友元
void test01()
{
	A a;
	g_func(&a);
}

//2.类做友元
void test02()
{
	B b;
	b.b_func();
}

//3. 成员函数做友元
void test03()
{
	B b;
	b.b_visit();
}

int main()
{
	test01();
	test02();
	test03();

	system("pause");

	return 0;
}
```



**注：**在上面的示例中，B的方法必须==类外实现==，因为B的方法访问A，而A只是声明了，并没有定义，只有在定义之后才可以访问。



### 3.5 继承



#### 3.5.1 继承的基本语法

**语法:**  	`class 父类 : 继承方式 子类`  



**继承方式有三种:**

* 公共继承
* 保护继承
* 私有继承





![img](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/clip_image002.png)





*  **继承中的对象模型**

  ==父类中的所有成员都会被子类继承下去，包括私有成员，但是编译器会隐藏私有成员使子类无法访问==



#### 3.5.2 继承中构造和析构顺序



**示例:	**

```c++
#include <iostream>
#include <string>
using namespace std;

class Base
{
public:
	Base()
	{
		cout << "Base构造" << endl;
	}

	~Base()
	{
		cout << "Base析构" << endl;
	}
};

class Son :public Base
{
public:
	Son()
	{
		cout << "Son 构造" << endl;
	}
	~Son()
	{
		cout << "Son析构" << endl;
	}
};

void test01()
{
	Son s;
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```



打印输出结果：

![image-20210531171338376](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210531171338376.png)

> 总结：继承中先调用父类构造函数，在调用子类构造函数，析构顺序与构造相反





#### 3.5.3  继承同名成员处理方式

当子类与父类出现同名的成员

* 访问子类同名成员  直接访问即可
* 访问父类同名成员  需要加作用域



**示例：	**

```c++
#include <iostream>
#include <string>
using namespace std;

class Base
{
public:
	Base()
	{
		m_A = 100;
	}
	void func()
	{
		cout << "Base func()" << endl;
	}
	void func(int a)
	{
		cout << "Base func(int a)" << endl;
	}

	int m_A;
};

class Son :public Base
{
public:
	Son()
	{
		m_A = 200;
	}
	void func()
	{
		cout << "Son func()" << endl;
	}

	
	int m_A;
};

void test01()
{
	Son s;

	cout << "Son m_A: " << s.m_A << endl;
	cout << "Base m_A:" << s.Base::m_A << endl;

	s.func();
	s.Base::func();
	s.Base::func(10);
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```



> 总结：
>
> 1. 子类对象可以直接访问到子类中同名成员
> 2. 子类对象加作用域可以访问到父类同名成员
> 3. 当子类与父类拥有同名的成员函数，子类会隐藏父类中同名成员函数，加作用域可以访问到父类中同名函数



==注： 对于继承同名静态成员处理方式和以上一样，静态成员需要通过类名访问==





#### 3.5.4 多继承

 c++允许 **一个类继承多个类**



语法：`class 子类：继承方式 父类1，继承方式 父类2...`

多继承中可能会引发父类中有同名成员出现，需要加作用域区分



**c++实际开发中不建议用多继承**



#### 3.5.5  菱形继承

**菱形继承概念：**

​	两个派生类继承同一个基类

​	又有某个类同时继承两个派生类

​	这种继承被称为菱形继承，或者钻石继承



![clip_image003](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/clip_image003.jpg)



**菱形继承问题：	**

1. 羊继承了动物的数据，驼同样继承了动物的数据，当草泥马使用数据时，就会产生二义性。
2. 草泥马继承自动物的数据继承了两份，其实我们应该清楚，这份数据我们只需要一份就可以。



**示例：	**

```c++
#include <iostream>
#include <string>
using namespace std;

class Animal
{
public:
	int m_Age;
};

//继承前加virtual关键字后，变为虚继承
//此时公共的父类Animal称为虚基类
class Sheep : virtual public Animal {};
class Tuo	: virtual public Animal {};	
class SheepTuo : public Sheep, public Tuo {};

void test01()
{
	SheepTuo st;
	st.Sheep::m_Age = 100;
	st.Tuo::m_Age = 200;

	cout << "st.Sheep::m_age =  " << st.Sheep::m_Age << endl;
	cout << "st.Tuo::m_age = " << st.Tuo::m_Age << endl;
	cout << "st.m_age = " << st.m_Age << endl;
}

int main()
{
	test01();

	system("pause");

	return 0;
}
```



> 总结
>
> 1. 菱形继承带来的主要问题是子类继承两份相同的数据，导致资源浪费以及毫无意义
> 2. 利用虚继承可以解决菱形继承问题







### 3.6 多态



























