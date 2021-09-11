#  C++基础

C++中的基础语法与C基本一样，C++是包含C的所有语法的

## C++概览



### 1. 初识C++

**Hello C++**

```c++
#include <iostream>
using namespace std;

int main()
{
	cout << "Hello C++" << endl;

	system("pause");

	return 0;
}
```



* c++中的关键字

  | asm        | do           | if               | return      | typedef  |
  | ---------- | ------------ | ---------------- | ----------- | -------- |
  | auto       | double       | inline           | short       | typeid   |
  | bool       | dynamic_cast | int              | signed      | typename |
  | break      | else         | long             | sizeof      | union    |
  | case       | enum         | mutable          | static      | unsigned |
  | catch      | explicit     | namespace        | static_cast | using    |
  | char       | export       | new              | struct      | virtual  |
  | class      | extern       | operator         | switch      | void     |
  | const      | false        | private          | template    | volatile |
  | const_cast | float        | protected        | this        | wchar_t  |
  | continue   | for          | public           | throw       | while    |
  | default    | friend       | register         | true        |          |
  | delete     | goto         | reinterpret_cast | try         |          |

  `提示：在给变量或者常量起名称时候，不要用C++得关键字，否则会产生歧义。`



### 2. 数据类型

#### 2.1 整型

| **数据类型**        | **占用空间**                                    | 取值范围         |
| ------------------- | ----------------------------------------------- | ---------------- |
| short(短整型)       | 2字节                                           | (-2^15 ~ 2^15-1) |
| int(整型)           | 4字节                                           | (-2^31 ~ 2^31-1) |
| long(长整形)        | Windows为4字节，Linux为4字节(32位)，8字节(64位) | (-2^31 ~ 2^31-1) |
| long long(长长整形) | 8字节                                           | (-2^63 ~ 2^63-1) |



####  2.2 实型（浮点型）

| **数据类型** | **占用空间** | **有效数字范围** |
| ------------ | ------------ | ---------------- |
| float        | 4字节        | 7位有效数字      |
| double       | 8字节        | 15～16位有效数字 |



#### 2.3 字符型

**作用：**字符型变量用于显示单个字符

**语法：**`char ch = 'a';`



> 注意1：在显示字符型变量时，用单引号将字符括起来，不要用双引号

> 注意2：单引号内只能有一个字符，不可以是字符串



#### 2.4 字符串型

**作用**：用于表示一串字符

* C风格字符串：	`char str[] = "stringValue"`
* C++风格字符串： `string str = "stringValue"`



> 注意：C++风格字符串，需要加入头文件    ==#include < string >==



#### 2.5  布尔类型

bool类型只有两个值：

* true ----真（本质是1）
* false ----假（本质是0）

**bool类型整1个字节大小**





### 3. 运算符

1. 算术运算符：`+` `-` `*` `/` `%`  `++`(前后缀)   `--` (前后缀)
2. 赋值运算符： `=` `+=` `-=` `*=` `/=` `%=` 
3. 比较运算符：`==` `!=` `<` `>` `<=` `>=`
4. 逻辑运算符：`!` `&&` `||`





## 程序流程结构

C/C++支持最基本的三种程序运行结构：==顺序结构、选择结构、循环结构==

* 顺序结构：程序按顺序执行，不发生跳转
* 选择结构：依据条件是否满足，有选择的执行相应功能
* 循环结构：依据条件是否满足，循环多次执行某段代码



###  1. 选择结构

1. `if else` : 包括多层嵌套
2. 三目运算符： `表达式1 ? 表达式2 : 表达式3`

3. `switch ` 语句



### 2.  循环结构

1. `while`循环
2. `do ... while` 循环
3. `for`  循环



### 3. 跳转语句

1. `break` 语句，跳出当前循环或选择结构
2. `continue` 语句，在循环语句中，跳过本次循环中余下尚未执行的语句，继续执行下一次循环
3. `goto` 语句，跳转至标号出执行，**不建议使用**



## 数组

### 1. 一维数组

一维数组定义的三种方式：

1. ` 数据类型  数组名[ 数组长度 ]; `
2. `数据类型  数组名[ 数组长度 ] = { 值1，值2 ...};`
3. `数据类型  数组名[ ] = { 值1，值2 ...};`



### 2. 二位数组(多维数组)

二维数组定义的四种方式：

1. ` 数据类型  数组名[ 行数 ][ 列数 ]; `
2. `数据类型  数组名[ 行数 ][ 列数 ] = { {数据1，数据2 } ，{数据3，数据4 } };`
3. `数据类型  数组名[ 行数 ][ 列数 ] = { 数据1，数据2，数据3，数据4};`
4. ` 数据类型  数组名[  ][ 列数 ] = { 数据1，数据2，数据3，数据4};`



## 函数

c++的函数和c的函数不同点



### 1.函数默认参数

在c++中，函数的形参列表中的形参可以有默认值

**语法：** `返回值类型  函数名 (参数 = 默认值) {}`



示例：

```c++
int func(int a, int b = 10)
{
	return a * b;
}

int main()
{
	cout << "ret = " <<  func(10) << endl;
	cout << "ret = " << func(10,2) << endl;

	system("pause");

	return 0;
}
```



> 注意： 默认参数必须放在参数列表的最后，调用时默认参数不传参使用默认的
>
> 传入参数，使用传入的实参



### 2.  函数占位参数

c++中函数的形参列表里可以有占位参数，用来占位，调用函数时必须填补该位置

**语法：** `返回值类型  函数名 (数据类型) {}`



```c++
void func(int a, int)
{
    cout << "this is func" << endl;
}

int main()
{
    func(10, 10);  //占位参数必须填补
    
    system("pause");

	return 0;
    
}
```



### 3. 函数重载

函数重载的条件：

* 同一作用域下
* 函数名称相同
* 函数参数**类型** 或者 **个数不同** 或者 **顺序不同**



**注意：** 函数的返回值不可以作为函数重载的条件



示例：

```c++
void func()
{
	cout << "func()" << endl;
}

void func(int a)
{
	cout << "func(int a)" << endl;
}

void func(double a)
{
	cout << "func(double a)" << endl;
}

void func(int a, double b)
{
	cout << "func(int a, double b)" << endl;
}

void func(double b, int a)
{
	cout << "func(double a, int b)" << endl;
}

//函数返回值不可以作为函数重载条件
//int func(double b, int a)
//{
//	cout << "func(double a, int b)" << endl;
//
//	return 0;
//}

int main()
{
	func();
	func(10);
	func(3.14);
	func(10, 3.14);
	func(3.14, 10);

	system("pause");

	return 0;
}
```





**函数重载碰到默认参数**

```c++
void func(int a, int b = 10)
{
	cout << "func(int a, int b = 10)" << endl;
}

void func(int a)
{
	cout << "func(int a)" << endl;
}

int main()
{
	int a = 10;

	//func(a);	//错误，默认参数产生歧义

	system("pause");

	return 0;
}
```





## 指针

### 1.  基本概念

**指针作用：** 可以通过指针间接访问内存



* 内存编号从0开始记录的，一般用十六进制数字标识
* 可以用指针变量保存地址





### 2. 指定的定义

**语法：**  `数据类型* 变量名`



```c++
int main()
{
    int a = 10;
    int* p;
    
    p = &a;		//p指向变量a的地址
    
    cout << &a << endl;	//打印数据a的地址
    cout << p << endl;	//打印指针p的地址
    
    cout << "*p" << *p << endl; //通过*操作打印指针指向的地址的数据
    
    system("pause");
    
    return 0;    
}
```



> 说明：所有指针类型在32位操作系统下是4个字节，在64位系统下是8个字节





### 3.  空指针和野指针

**空指针：** 指针变量指向内存编号为0的空间

**用途：** 初始化指针变量

**注意：** 空指针指向的内存是不可以访问的



示例：

```c++
int main()
{
    int* p = nullptr;
     
    cout << *P << endl;  //程序运行异常，空指针指向的内存地址是不允许用户访问
    
    system("pause");

	return 0;
}
```





**野指针：** 指针变量指向非法内存空间

示例：

```c++
int main()
{
	int* p = (int*)0x1100;
	
    //访问野指针报错
	cout << *p << endl;

	system("pause");

	return 0;
}
```



> 总结：空指针和野指针都不是我们申请的空间，因此不要访问。





### 4.  const修饰指针

const修饰指针有三种情况：

1. const修饰指针  --- 常量指针
2. const修饰常量  ---  指针常量
3. const既修饰指针又修饰常量



示例：

```c++
int main()
{
	int a = 10;
	int b = 10;

	//const修饰的是指针，指针指向可以改，指针指向的值不可以更改
	const int* p1 = &a;
	p1 = &b;	//正确
	//*p1 = 100;	//错误

	//const修饰的是常量，指针指向不可以改，指针指向的值可以更改
	int* const p2 = &a;
	//p2 = &b;	//错误
	*p2 = 100;	//正确

	//const既修饰指针又修饰常量
	const int* const p3 = &a;
	//p3 = &b;	//错误
	//*p3 = 100;	//错误

	system("pause");

	return 0;
}
```



> 技巧： 看const右侧跟着的是指针还是常量，是指针就是常量指针，是常量就是指针常量



### 5.   指针和数组

利用指针访问数组中元素，数组名就是数组的首地址



```c++

int main()
{
	int arr[] = { 1,2,3,4,5,6,7,8,9,10 };

	int* p = arr;

	cout << "第一个元素： " << arr[0] << endl;
	cout << "指针访问第一个元素：" << *p << endl;

	for (int i = 0; i < 10; i++) {
		//利用指针遍历数组
		cout << *p << endl;
		p++;
	}

	system("pause");

	return 0;
}
```





### 6.  指针作函数参数

传入指针，可以修改实参的值



示例：

```c++
//值传递
void swap1(int a, int b)
{
	int temp = a;
	a = b;
	b = temp;
}

//地址传递
void swap2(int* p1, int* p2)
{
	int temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

int main()
{
	int a = 10;
	int b = 20;

	//值传递，不会改变实参
	swap1(a, b);
	cout << "a = " << a << endl;
	cout << "b = " << b << endl;

	//地址传递，会改变实参
	swap2(&a, &b);
	cout << "a = " << a << endl;
	cout << "b = " << b << endl;

	system("pause");

	return 0;
}
```



