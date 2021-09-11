# C++泛型编程和STL



## 1. 模板



### 1.1  模板的概念



模板就是建立**通用模具** ，大大提高复用性



模板的特点：

* 模板不可以直接使用，它指示一个框架
* 模板的通用并不是万能的



### 1.2 函数模板



* C++另一种编程思想称为==泛型编程== ，主要利用的技术就是模板
* C++提供两种模板机制：**函数模板**和**类模板**



#### 1.2.1  函数模板语法

函数模板作用：建立一个通用函数，其函数返回值类型和形参类型可以不具体指定，用一个**虚拟的类型**来代表。



**语法：**

```c++
template<typename T>
//函数声明或定义
```

**解释：**

template --- 声明创建模板

typename --- 表明其后的符号是一种数据类型，可以用 `class` 代替

T --- 通用的数据类型，名称可以替换，通常为大写字母



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

//利用模板提供通用的交换函数
template<typename T>
void my_swap(T& a, T& b)
{
	T temp = a;
	a = b;
	b = temp;
}

void test01()
{
	int a = 10;
	int b = 20;
	
	//1、自动推导类型
	my_swap(a, b);

	//2、显式指定类型
	my_swap<int>(a, b);

	cout << "a = " << a << "\t b = " << b << endl;
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
> 1. 函数模板利用关键字 `template`
> 2. 使用函数模板有两种方式：自动推导、显式指定类型
> 3. 模板的目的是为了提高复用性，将类型参数化





#### 1.2.2  函数模板注意事项

**注意事项：**

* 自动类型推导，必须推导出一致的数据类型，才可以使用
* 模板必须要确定出T的数据类型，才可以使用



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

//利用模板提供通用的交换函数
template<typename T>
void my_swap(T& a, T& b)
{
	T temp = a;
	a = b;
	b = temp;
}

//1. 自动类型推导，必须推导出一致的数据类型T，才可以使用
void test01()
{
	int a = 10;
	int b = 20;
	char c = 'c';

	my_swap(a, b);	//正确，可以推导出一致的T
	//my_swap(a, c);	//错误，推导不出一致的T类型
}

//2. 模板必须要确定出T的数据类型，才可以使用
template<class T>
void func()
{
	cout << "func()" << endl;
}

void test02()
{
	//func();	//错误，模板不能独立使用，必须确定出T的类型
	func<int>();	//正确，指定类型
}

int main()
{
	test01();
	test02();
	system("pause");

	return 0;
}
```



> 总结：使用模板时必须确定出通用数据类型T，并且能够推导出一致的类型





#### 1.2.3  普通函数与模板函数的区别

**普通函数与模板函数区别：**

* 普通函数调用时可以发生类型转换（隐式类型转换）
* 函数模板调用时，如果利用自动推导，不会发生类型转换
* 如果利用显示指定类型的方式，可以发生隐式类型转换

**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

//普通函数
int my_add01(int a, int b)
{
	return a + b;
}

//函数模板
template<class T>
T my_add02(T a, T b)
{
	return a + b;
}

//使用函数模板是，如果自动类型推导，不会发生自动类型转换，即隐式类型转换
void test01()
{
	int a = 10;
	int b = 20;
	char c = 'c';
	
	cout << my_add01(a, c) << endl;		//正确，char->int

	//my_add02(a, c);	//错误，使用自动类型推导时，不会发生隐式转换
	my_add02<int>(a, c);//正确，指定类型，可以发生隐式类型转换
}

int main()
{
	test01();
	
	system("pause");

	return 0;
}
```



> 总结：建议使用显示指定类型的方式，调用函数模板，因为可以自己确定通用类型T







#### 1.2.4  普通函数与函数模板的调用规则

调用规则如下：

1. 如果函数模板和普通都可以实现，优先调用普通函数
2. 可以通过空模板参数列表类强制调用函数模板
3. 函数模板也可以发生重载
4. 如果函数模板可以产生更好的匹配，优先调用函数模板



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

//普通函数与函数模板调用规则
void my_print(int a, int b)
{
	cout << "调用普通函数" << endl;
}

template<class T>
void my_print(T a, T b)
{
	cout << "调用模板" << endl;
}

template<class T>
void my_print(T a, T b, T c)
{
	cout << "调用重载模板" << endl;
}

void test01()
{
	//1. 如果函数模板和普通函数都可以实现，优先调用普通函数
	
	int a = 10;
	int b = 20;
	my_print(a, b);	//调用普通函数

	//2. 可以通过空木耙参数列表来强制调用函数模板
	my_print<>(a, b);	//调用函数模板

	//3.函数模板也可以发生重载
	int c = 30;
	my_print(a, b, c);	//调用重载的函数模板

	//4. 如果函数模板可以产生更好的匹配，优先调用函数模板
	char c1 = 'a';
	char c2 = 'b';
	my_print(c1, c2);	//调用函数模板
}

int main()
{
	test01();
	
	system("pause");

	return 0;
}
```



> 总结：既然提供了函数模板，最好就不要提供普通函数，否则容易出现二义性



#### 1.2.5  模板的局限性

**局限性：**

* 模板的通用性并不是万能的

  例如

  ```c++
  template<class T>
  void f(T a, T b)
  {
      a = b;
  }
  ```

  在上述代码中提供的赋值操作，如果传入的a和b是一个数组，就无法实现了

  再例：

  ```c++
  template<class T>
  void f(T a, T b)
  {
      if(a>b) {...}
  }
  ```

  在上述代码中，如果T的数据类型传入的是像Person这样的自定义数据类型，也无法正常运行

  因此C++为了解决这种问题，提供模板的重载，可以为这些特定的类型提供具体化的模板

  **示例：**

  ```c++
  #include <iostream>
  #include <string> 
  using namespace std;
  
  class Person
  {
  public:
  	Person(string name, int age): m_name(name),m_age(age) {}
   
  	string m_name;
  	int m_age;
  };
  
  //普通函数模板
  template<class T>
  bool my_compare(T& a, T& b)
  {
  	if (a == b) {
  		return true;		
  	}
  	else {
  		return false;
  	}
  }
  
  //利用具体化Person的版本实现代码，具体化优先调用
  template<> bool my_compare(Person& p1, Person& p2)
  {
  	if (p1.m_age == p2.m_age && p1.m_name == p2.m_name) {
  		return true;
  	}
  	else {
  		return false;
  	}
  }
  
  void test01()
  {
  	int a = 10;
  	int b = 20;
  
  	//内置数据类型可以直接使用通用的函数模板
  	bool ret = my_compare(a, b);
  	if (ret) {
  		cout << "a == b" << endl;
  	}
  	else {
  		cout << "a != b" << endl;
  	}
  }
  
  void test02()
  {
  	Person p1("tom", 10);
  	Person p2("tom", 10);
  	//自定义数据类型，不会调用普通的函数模板
  	//可以创建具体的Person数据类型的模板，用于特殊处理这个类型
  	bool ret = my_compare(p1, p2);
  	if (ret) {
  		cout << "p1 == p2" << endl;
  	}
  	else {
  		cout << "p1 != p2" << endl;
  	}
  }
  
  int main()
  {
  	test01();
  
  	test02();
  	
  	system("pause");
  
  	return 0;
  }
  ```

  > 总结：
  >
  > * 利用具体化的模板，可以解决自定义类型的通用化
  > * 学习模板并不是为了写模板，而是在STL能够运用系统提供的模板







### 1.3 类模板

#### 1.3.1  类模板语法

类模板作用：

* 建立一个通用类，类中的成员 数据类型可以不具体指定，用一个虚拟的类型来代表

**语法：**

```c++
template<typename T>
//类
```



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

template<class NameType, class AgeType>
class Person
{
public:
	Person(NameType name, AgeType age)
		:m_name(name),m_age(age) {}
	void show_person()
	{
		cout << "name: " << this->m_name << 
			" age: " << this->m_age << endl;
	}

public:
	NameType m_name;
	AgeType m_age;
};

void test01()
{
	//指定NameType为string ，AgeType为int类型
	Person<string, int>p1("jack", 99);
	p1.show_person();
}

int main()
{
	test01();
	
	system("pause");

	return 0;
}
```



#### 1.3.2 类模板与函数模板区别

类模板与函数模板却别主要有两点：

1. 类模板没有自动类型推导的使用方式
2. 类模板在模板参数中可以有默认参数



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

template<class NameType, class AgeType = int>
class Person
{
public:
	Person(NameType name, AgeType age)
		:m_name(name),m_age(age) {}
	void show_person()
	{
		cout << "name: " << this->m_name << 
			" age: " << this->m_age << endl;
	}

public:
	NameType m_name;
	AgeType m_age;
};

void test01()
{
	//指定NameType为string ，AgeType有默认的类型，可以不指定
	Person<string>p1("jack", 99);
	p1.show_person();
}

int main()
{
	test01();
	
	system("pause");

	return 0;
}
```



#### 1.3.3  类模板中成员函数创建时机

类模板中成员和普通类中成员函数创建时机是有区别的：

* 普通类的成员函数一开始就可以创建
* 类模板中的成员函数在调用时才创建



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

class Person1
{
public:
	void showPerson1()
	{
		cout << "Person1 show" << endl;
	}
};

class Person2
{
public:
	void showPerson2()
	{
		cout << "Perso2 show" << endl;
	}
};

template<class T>
class MyClass
{
public:
	T obj;

	//类模板中的成员函数，并不是一开始就创建的，而是在模板调用时再生成

	void fun1() { obj.showPerson1(); }
	void fun2() { obj.showPerson2(); }

};

void test01()
{
	MyClass<Person1> m;
	m.fun1();

	//m.fun2();	//编译出错，说明函数调用才会去创建成员函数
}

int main()
{
	test01();
	
	system("pause");

	return 0;
}
```



#### 1.3.4  类模板对象做函数参数

类模板实例化出对象，向函数传参

三种传入方式：

1. 指定传入的类型	--- 直接显示对象的数据模型
2. 参数模板化           --- 将对象中的参数变为模板进行传递
3. 整个类模板化       --- 将这个对象类型模板化进行传递



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

template<class NameType, class AgeType = int>
class Person
{
public:
	Person(NameType name, AgeType age)
		: mName(name), mAge(age) {}

	void showPerson()
	{
		cout << "name: " << this->mName << " Age: " << this->mAge << endl;
	}

public:
	NameType mName;
	AgeType mAge;

};

//1.指定传如的类型
void printPerson1(Person<string, int>& p)
{
	p.showPerson();
}

void test01()
{
	Person<string, int> p("tom", 100);
	printPerson1(p);
}

//2. 参数模板化
template <class T1, class T2>
void printPerson2(Person<T1, T2>& p)
{
	p.showPerson();
	cout << "T1的类型为：" << typeid(T1).name() << endl;
	cout << "T2的类型为：" << typeid(T2).name() << endl;

}

void test02()
{
	Person<string, int> p("jack", 90);
	printPerson2(p);
}

//3.整个类模板化
template<class T>
void printPerson3(T& p)
{
	cout << "T 的类型为： " << typeid(T).name() << endl;
	p.showPerson();
}

void test03()
{
	Person<string, int>p("alice", 30);
	printPerson3(p);
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



#### 1.3.5  类模板与继承

当类模板碰到继承，需要注意一下几点：

* 当子类继承的父类是一个类模板时，子类在声明的时候，要指出父类中T的类型
* 如果不指定，编译器无法给子类分配内存
* 如果想灵活指定出父类中T的类型，子类也需变为类模板



**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

template<class T>
class Base
{
	T m;
};

//class Son:public Base  //错误，c++编译器需要给子类分配内存，必须知道父类中T的类型才可以向下继承
class Son : public Base<int>
{

};

void test01()
{
	Son c;
}

//类模板继承类模板，可以用T2指定父类中的T类型
template<class T1, class T2>
class Son2 : public Base<T2>
{
public:
	Son2()
	{
		cout << typeid(T1).name() << endl;
		cout << typeid(T2).name() << endl;
	}
};

void test02()
{
	Son2<int, char> child1;
}

int main()
{
	test01();
	test02();

	system("pause");

	return 0;
}


```



#### 1.3.6 类模板成员函数类外实现

**示例：**

```c++
#include <iostream>
#include <string> 
using namespace std;

//类模板成员函数类外实现
template <class T1, class T2>
class Person 
{
public:
	//成员函数类内声明
	Person(T1 name, T2 age);
	void showPerson();

public:
	T1 mName;
	T2 mAge;

};

//构造函数 类外实现
template<class T1, class T2>
Person<T1, T2>::Person(T1 name, T2 age)
{
	this->mAge = age;
	this->mName = name;
}

//成员函数 类外实现
template<class T1, class T2>
void Person<T1, T2>::showPerson()
{
	cout << "Name:" << this->mName << "   Age:" << this->mAge << endl;
}



void test01()
{
	Person<string, int>p("tom", 20);
	p.showPerson();
}



int main()
{
	test01();


	system("pause");

	return 0;
}
```



#### 1.3.7  类模板分文件编写

类模板分文件编写的方式

1. 直接包含.cpp源文件
2. 将声明和实现写到同一个文件中，并更改后缀名为.hpp, ==hpp是约定的名称，并不是强制的==





## 2. STL 初识



STL 从广义上分为： **容器(container),算法(algorithm),迭代器(iterator)**

容器和算法之间通过迭代器进行无缝连接。



STL大体分为六大组件,分别是容器，算法，迭代器，仿函数，适配器，空间配置

1. 容器：各种数据结构：如 vector，list，deque，set，map等，用来存放数据
2. 算法：各种常用的算法，如sort，find，copy，for_each等
3. 迭代器：扮演类容器与算法之间的胶合剂
4. 仿函数：行为类似函数，可作为算法的某种策略
5. 适配器：一种用来修饰容器或者仿函数或迭代器接口的东西
6. 空间配置器：负责空间的配置和管理



迭代器种类：

| 种类           | 功能                                                   | 支持运算                                                |
| -------------- | ------------------------------------------------------ | ------------------------------------------------------- |
| 输入迭代器     | 对数据的只读访问                                       | 只读， `++` 、`==` 、`!=`                               |
| 输出迭代器     | 对数据只写访问                                         | 只写，`++`                                              |
| 前向迭代器     | 读写操作，并能向前推进迭代器                           | 读写，`++`、`==`、 `!=`                                 |
| 双向迭代器     | 读写操作，并能向前向后操作                             | 读写，`++`、`--`                                        |
| 随机访问迭代器 | 读写操作，可以跳跃的方式访问任意数据，功能最强的迭代器 | 读写，`++`、`--`、`[n]`、`-n` 、`<` 、`<=` 、`>` 、`>=` |



### 2.1  容器算法迭代器初识

以`vector`为例，初步了解容器，算法和迭代器



#### 2.1.1  vector存放内置数据类型

容器：`vector`

算法：`for_each`

迭代器：`vector<int>::iterator`



**示例：**

```c++
#include <iostream>
#include <string> 
#include <vector>
#include <algorithm>
using namespace std;

void myPrint(int val)
{
	cout << val << endl;
}

void test01()
{
	//创建vector容器对象，并且通过模板参数指定容器中存放的数据类型
	vector<int> v;
	//向容器中放数据
	v.push_back(10);
	v.push_back(20);
	v.push_back(20);
	v.push_back(40);

	//每一个容器都有自己的迭代器，迭代器是用来遍历容器中的元素
	//v.begin() 返回迭代器，这个迭代器指向容器中第一个数据
	//v.end() 返回迭代器，这个迭代器指向容器元素最后一个元素的下一个位置
	//vector<int>::iterator  拿到vector<int> 这种容器的迭代器类型

	vector<int>::iterator pBegin = v.begin();
	vector<int>::iterator pEnd = v.end();

	//第一种遍历方式：
	while (pBegin != pEnd) {
		cout << *pBegin << endl;
		pBegin++;
	}
	cout << endl;

	//第二种遍历方式
	for (vector<int>::iterator it = v.begin(); it != v.end(); it++) {
		cout << *it << endl;
	}
	cout << endl;

	//第三种遍历方式
	for_each(v.begin(), v.end(), myPrint);

}

int main()
{
	test01();


	system("pause");

	return 0;
}


```



> vector也可以存放自定义数据类型
>
> vector可以嵌套容器，例如`vector<vector<int>>` (c++11)







## 3. 常用容器

### 3.1 string 容器

string 是C++风格的字符串，而string本质是一个类

**string和char*的区别：**

* char* 是一个指针
* string 是一个类，类内部封装了char* ,管理这个字符串，是一个char*容器

string管理char*所分配的内存，不要担心复制越界和取值越界等，由类内部负责



#### 3.1.1 string的构造函数

构造函数原型：

* `string();` 										创建一个空字符串
* `string(const char* s);`        使用字符串s初始化
* `string(const string& str);`   使用一个string对象初始化另一个string对象
* `string(int n, char c);`           使用n个字符串c初始化

**示例：**

```c++
#include <iostream>
#include <string> 

using namespace std;

//string构造
void test01()
{
	string s1; //创建空字符串，调用无参构造函数
	cout << "str1 = " << s1 << endl;
	const char* str = "hello world";
	string s2(str); //把c_string转换成了string
	cout << "str2 = " << s2 << endl;
	string s3(s2); //调用拷贝构造函数
	cout << "str3 = " << s3 << endl;
	string s4(10, 'a');
	cout << "str3 = " << s3 << endl;
}
int main() 
{
	test01();

	system("pause");

	return 0;
}
```





#### 3.1.2 string 赋值操作

给string字符串进行赋值

赋值的函数原型：

* `string& operator=(const char* s);` //char*类型字符串 赋值给当前的字符串
* `string& operator=(const string &s);` //把字符串s赋给当前的字符串
* `string& operator=(char c);` //字符赋值给当前的字符串
* `string& assign(const char *s);` //把字符串s赋给当前的字符串
* `string& assign(const char *s, int n);` //把字符串s的前n个字符赋给当前的字符串
* `string& assign(const string &s);` //把字符串s赋给当前字符串
* `string& assign(int n, char c);` //用n个字符c赋给当前字符串







#### 3.1.3 string字符串拼接

实现在字符串末尾拼接字符串

**函数原型：**

* `string& operator+=(const char* str);` //重载+=操作符
* `string& operator+=(const char c);` //重载+=操作符
* `string& operator+=(const string& str);` //重载+=操作符
* `string& append(const char *s);` //把字符串s连接到当前字符串结尾
* `string& append(const char *s, int n);` //把字符串s的前n个字符连接到当前字符串结尾
* `string& append(const string &s);` //同operator+=(const string& str)
* `string& append(const string &s, int pos, int n);` //字符串s中从pos开始的n个字符连接到字符串结尾



#### 3.1.4 string查找和替换

查找：查找指定字符串是否存在
替换：在指定的位置替换字符串

**函数原型：**

* `int find(const string& str, int pos = 0) const;` //查找str第一次出现位置,从pos开始查找
* `int find(const char* s, int pos = 0) const;` //查找s第一次出现位置,从pos开始查找
* `int find(const char* s, int pos, int n) const;` //从pos位置查找s的前n个字符第一次位置
* `int find(const char c, int pos = 0) const;` //查找字符c第一次出现位置
* `int rfind(const string& str, int pos = npos) const;` //查找str最后一次位置,从pos开始查找
* `int rfind(const char* s, int pos = npos) const;` //查找s最后一次出现位置,从pos开始查找
* `int rfind(const char* s, int pos, int n) const;` //从pos查找s的前n个字符最后一次位置
* `int rfind(const char c, int pos = 0) const;` //查找字符c最后一次出现位置
* `string& replace(int pos, int n, const string& str);` //替换从pos开始n个字符为字符串str
* `string& replace(int pos, int n,const char* s);` //替换从pos开始的n个字符为字符串s



> 总结：
>
> * find查找是从左往后，rfind从右往左
> * find找到字符串后返回查找的第一个字符位置，找不到返回-1
> * replace在替换时，要指定从哪个位置起，多少个字符，替换成什么样的字符串





#### 3.1.5 string字符串比较

字符串之间的比较

* 比较方式：
  字符串比较是按字符的ASCII码进行对比
  = 返回 0

  \> 返回 1

  < 返回 -1

**函数原型：**

* `int compare(const string &s) const;` //与字符串s比较
* `int compare(const char *s) const;` //与字符串s比较







#### 3.1.6 string字符存取

string中单个字符存取方式有两种

* `char& operator[](int n);` //通过[]方式取字符
* `char& at(int n);` //通过at方法获取字符





#### 3.1.7 string插入和删除

对string字符串进行插入和删除字符操作
**函数原型：**

* `string& insert(int pos, const char* s);` //插入字符串
* `string& insert(int pos, const string& str);` //插入字符串
* `string& insert(int pos, int n, char c);` //在指定位置插入n个字符c
* `string& erase(int pos, int n = npos);` //删除从Pos开始的n个字符







#### 3.1.8 string子串

从字符串中获取想要的子串
**函数原型：**

* `string substr(int pos = 0, int n = npos) const;` //返回由pos开始的n个字符组成的字符串







### 3.2 vector容器

vector数据结构和数组非常相似，也称为单端数组
**vector与普通数组区别：**

* 不同之处在于数组是静态空间，而vector可以动态扩展

**动态扩展：**

* 并不是在原空间之后续接新空间，而是找更大的内存空间，然后将原数据拷贝新空间，释放原空间
* vector容器的迭代器是支持随机访问的迭代器





#### 3.2.1 vector 构造函数

创建vector容器
**函数原型：**

* `vector<T> v;` //采用模板实现类实现，默认构造函数
* `vector(v.begin(), v.end());` //将v[begin(), end())区间中的元素拷贝给本身。
* `vector(n, elem);` //构造函数将n个elem拷贝给本身。
* `vector(const vector &vec);` //拷贝构造函数。





#### 3.2.2 vector赋值操作

给vector容器进行赋值
**函数原型：**

* `vector& operator=(const vector &vec);` //重载等号操作符
* `assign(beg, end);` //将[beg, end)区间中的数据拷贝赋值给本身。
* `assign(n, elem);` //将n个elem拷贝赋值给本身。



#### 3.2.3 vector容量和大小

**功能描述：**

* 对vector容器的容量和大小操作

**函数原型：**

* empty(); //判断容器是否为空

* capacity(); //容器的容量

* size(); //返回容器中元素的个数

* resize(int num); //重新指定容器的长度为num，若容器变长，则以默认值填充新位置。

  //如果容器变短，则末尾超出容器长度的元素被删除。

* resize(int num, elem); //重新指定容器的长度为num，若容器变长，则以elem值填充新位置。

  //如果容器变短，则末尾超出容器长度的元素被删除







#### 3.2.4 vector插入和删除

**功能描述：**

* 对vector容器进行插入、删除操

**函数原型：**

* `push_back(ele);` //尾部插入元素ele
* `pop_back();` //删除最后一个元素
* `insert(const_iterator pos, ele);` //迭代器指向位置pos插入元素ele
* `insert(const_iterator pos, int count,ele);` //迭代器指向位置pos插入count个元素ele
* `erase(const_iterator pos);` //删除迭代器指向的元素
* `erase(const_iterator start, const_iterator end);` //删除迭代器从start到end之间的元素
* `clear();` //删除容器中所有元素





#### 3.2.5 vector 数据存取

**功能描述：**

* 对vector中的数据的存取操作

**函数原型：**

* `at(int idx);` //返回索引idx所指的数据
* `operator[];` //返回索引idx所指的数据
* `front();` //返回容器中第一个数据元素
* `back();` //返回容器中最后一个数据元素

