# 第2章	变量和基本类型



##  1. 基本内置类型

C++ 基本的数据类型有 算术类型和空类型，算术类型就是基本的整型和浮点型的数据类型。

不同类型之间的转换需要注意，有的转换可能时我们不想发生的。

**字面值常量**

- 数值型，编译器会根据数字形式对应一种基本的数据类型。
- 字符和字符串字面常量
- 布尔字面值和指针字面值



## 2. 变量

变量提供一个具名的、可供程序操作的存储空间。

###　2.1 变量定义

C++变量的定义要指定变量的类型。

```C++
//变量定义并初始化
int a = 2;
//变量定义
int b;
//变量赋值
b = 1;
```



> 在C++中变量的初始化和赋值是有区别的， `int a = 2;` 的`= ` 运算符表示的是初始化，
>
> 而在 `b=1;`  中的 `=` 是赋值。



<span style="border:2px solid Red">C++11</span>  列表初始化

```cpp
int val = 1;
int val = {0};
int val{0};
int val(0);
```

使用 `{}` 来初始化变量，称为列表初始化，这种方式初始化变量，编译器化检查初始化的变量是否符号定义的变量的类型

```cpp
long double pi = 3.14;
int a{pi};	//错误，编译器会检查类型，无法通过编译
```

> 总结：C++变量初始化的语法形式有三种：`=` , `()` , `{}`



**默认初始化** ，定义变量时没有初始化变量的值，则变量会被默认初始化。默认初始化的值取决于变量定义的类型。==定义在函数体内的局部变量和类中的成员属性是不会被初始化的== 所以不用试图使用任何方式去访问这些变量。



### 2.2 声明和定义

**声明**，使程序知道变量（对象）的存在

**定义**，负责创建于名字关联的实体 



```c++
extern int i;	//声明i
extern int i = 1;	//错误，给i赋值extern失效
int j;		//声明并定义j
```

==变量能且只能被定义一次，但是可以被多次声明==



###  2.3-4 标识符、作用域

#### 标识符

变量命名按照规范，不要使用保留关键字。

==命名规则，供参考：==

- 普通的局部变量和函数参数名使用小驼峰（第一个单词首字母小写，其他单词首字母大写）， 例： `userName`
- 全局变量前加 `g_`, 后面的按小驼峰规则 ， `g_userName`
- 静态变量前加 `s_` , 后面按小驼峰规则， `s_userName`
- 类名使用大驼峰，所有单词的首字母大写 ,  `UserManage`
- 类属性（成员变量）前面加 `m_` ,后面按小驼峰规则  ， `m_userName`
- 常量全部使用大写，多个单词用`_` 分割， `MAX_NUMBER`



#### 作用域

局部变量不能和全局的变量重名，嵌套的块，内部的不要和外部的重名。



## 3. 复合类型

符合类型的声明语句是由一个 **基本数据类型** 和紧随其后的一个 **声明符** 列表组成。

### 3.1 引用

**引用** 就是为变量（对象）起一个别名

```c++
int val = 1024;
int val1 = 102;
int& refVal = val;		//refVal指向val
refVal = val1;			//refVal引用并没有改变，只是改变了refVal指向的变量val的值，val = val1
int &refVal2;			//错误，引用必须初始化
```

> 注意:
>
> 1. 引用必须初始化，且不能改变
> 2.  `&` 符号可以紧靠基本类型(int), 也可以紧靠变量名



```c++
int i1 = 10, i2 = 20;	//i1，i2是 int
int &r = i1, r2 = i2	//r是引用指向i1，r2是int
```



**以上说的引用都是左值引用，C++11还有右值引用**



### 3.2 指针

**指针** 就是一个整数，没有实际的数值大小，只是一个编号，这个编号指向的是内存中的某个地址。

指针的定义

```c++
void *p1, *p2;	//p1, p2都是指针类型， 定义在一条语句中，每个变量都要加 *
```

> 指针无论定义成什么基本类型，其值都是一个固定位数的整数，指针类型数据的大小取决于系统的位数
>
> 32bit的系统指针是4byte = 32 bit, 64 bit系统指针式 8 byte = 64bit



指定类型的指针

```c++
int val = 102;
int *p = &val;	//指针p指向val变量的内存地址
```

> 定义指定类型的指针只是为了提供操作数据时需要操作的字节数。
>
> 例如，`int` 型的指针，在使用指针改变指向的数据时，改变的是以该指针变量为首地址的4个字节内存，
>
> 同样对`int` 型指针的加或减的操作也是以4个字节为基本单位



`*` 和 `&`

```c++
int val = 10;
int *p = nullptr;  	//* 表示定义一个指针变量，并且初始化为空指针
p = &val;			//& 表示取val变s量的地址值
std::cout << *p << std::endl;	//* 表示解引用，取出p地址指向的值，即 val
```



> 指针使用建议：
>
> 1. 指针定义是可以不初始化，但建议定义时初始化，如果没有想好指向哪个变量，可以初始化为空指针
> 2. 操作指针时，须确定操作的不是空指针和野指针（无效指针）





### 3.3 理解复合类型的声明



```c++
int i = 42;
int *p;			//p是int型的指针
int *&r = p;	//r是一个对指针p的引用

r = &i;			//r是一个指针引用，因此给r赋值&i就是令p指向i
*r = 0;			//解引用r,就是解引用指针p,将p指向的变量i的值改为0
```



> Tip: 面对一条比较复杂的指针或引用的声明语句时，从右向左读有助于弄清楚它的真实含义。





## 4. const 限定符

const 用于定义一个不能改变的变量, 所以定义时就必须初始化

```c++
cont int bufSize = 512;		//用字面值常量初始化
cont int i = get_size();	//用函数返回值初始化， 运行时初始化
int j = 10;
cont int k = j;				//用其他变量初始化
```



> `const` 定义的变量只对本文件可见，要使其他文件也可见需使用 `extern` 



### 4.1 const的引用

```c++
const int ci = 1024;
const int &r1 = ci;		//正确，引用r1和ci都是常量
r1 = 42;				//错误， r1 是对常量的引用
int &r2 = ci;			//错误，不能让一个常量引用指向一个常量对象
```



```c++
int i = 42;
cont int j = 10;
const int &r1 = i;			//正确，允许将 const int&绑定到一个普通int对象
r1 = 10;					//错误，不能通过常量引用改变i的值
const int &r2 = 42;			//正确
const int &r3 = r1 * 2;		//正确
int& r4 = j;				//错误
int &r4 = r1 * 2;			//错误
```



==组合关系==

|               | `int i` | `cont int i` |
| :-----------: | :-----: | :----------: |
|   `int &r `   |    ✔    |      ❌       |
| `cont int &r` |    ✔    |      ✔       |



### 4.2 指针和const



|               | `int i` | `cont int i` |
| :-----------: | :-----: | :----------: |
|   `int *p `   |    ✔    |      ❌       |
| `cont int *p` |    ✔    |      ✔       |



#### const指针



```c++
int errNumb = 0;
int *const curErr = &errNumb;	//curErr将一直指向errNumb,不可以改变指向
const double pi = 3.14;
cont double *const pip = &pi;		//pip是一个指向常量对象的常量指针
```

==从右向左读==



> C++ Primer 5th :
>
> <a id="const point">常量指针</a>： 该变量是一个指针，指针本身是一个常量，即它的指向初始化后不可以改变



*另一种说法：*

*指针常量：该变量是一个指针，指针本身是一个常量，即它的指向初始化后不可以改变*

*常量指针：该指针变量指向的是常量，指针的指向可以改变，但是不能通过指针解引用改变所指向的变量的值*



### 4. 3 顶层const

**顶层const** : 表示该变量（对象）本身是常量，不可以改变

**底层const**: 表示指向的变量（对象）是一个常量



```c++
int i = 0;
int *const p1 = &i;		//p1是指针，p1的指向不能改变，顶层
const int ci = 42;		//ci是普通变量，ci的值不能改变，顶层
const int *p2 = &ci;	//p2是一个指针，它必须指向 const int型的数据，但是本身的指向可以改变，底层
const int *const p3 = p2;	//第一个底层，第二个顶层
const int &r = ci;			//用于声明引用的const都是底层
```



==引用类型的变量自带顶层const== 即引用一旦赋值（指向某个变量）就不可以在变化（指向另一个变量）



### 4.4 constexpr和常量表达式

<span style="border:2px solid Red">C++11</span>  用 `constexpr` 关键字声明一个变量，编译器会检查该表达式是否是一个常量表达式。



**constexpr和指针**

```c++
const int *p1 = nullptr;
constexpr int *p2 = nullptr;
int *const p3 = nullptr;
```

> p2 和p3是等价的，`constexpr`修饰指针变量是被定义为顶层const



## 5. 处理类型

为了复杂程序更加易读易写，通常会给类型取别名，或是利用C++提供的特性自动推导复杂类型。



### 5.1 类型别名



#### typedef

传统的方法是使用 `typedef` 关键字定义类型别名

```cpp
typedef double wages;		//wages表示是double类型
typedef wages base, *p;		//base = wages = double, p = double*
//数组的别名
typedef int arrT[10];		//arrT是一个类型别名，他表示的类型是含有10个整数的数组
using arrT = int[10];		//和上面的等价
```



#### using

<span style="border:2px solid Red">C++11</span> 提供了一种新的方式，使用 `using` 

```cpp
using SI = Sales_item;		//Sales_item是一个类类型， SI表示是该类的别名
```

> 这里的 `using` 要和 `using namespace std;` 中的 `using` 区分开。后者是表示引入命名空间，类似于java和python的导包操作



#### 指针、常量和类型别名

```cpp
typedef char* pstring;
const pstring cstr = 0;		//char *const cstr = 0;
const pstring *ps;			//char **const ps;
```

==第二行的定义不能理解成== `const char *cstr = 0;` 



>  `const pstring` 中 `const` 是对 `pstring` 的修饰，而 `pstring` 是一个 `char*` 类型，因此 `const petring` 是指向 char的 [常量指针](#const point) ，而并不是指向常量字符的指针



### 5.2 auto 类型说明符

<span style="border:2px solid Red">C++11</span>  `auto` 类型说明符可以让编译器分析表达式所属的类型。

```cpp
int val1 = 1, val2 = 3;
auto val = val1 + val2;		//编译器可以自动推出val为int类型
auto i = 0, *p = &i;		//正确，编译器通过字面值推出i为int,p为int*
auto sz = 0; pi = 3.14;		//错误，编译器无法推出类型， sz， pi类型不一致无法统一
```



#### 复合类型、常量和auto

- 当使用引用类型推导类型是，`auto`推导的类型是引用指向变量的实际类型

  ```cpp
  int i = 0; &r = i;
  auto a = r;		// r是int型的引用,因此a是int型
  ```

- `auto`会忽略掉顶层const, 同时底层const则会保留下来

  ```cpp
  const int ci = i, &cr = ci;
  auto b = ci;	//int b = ci;
  auto c = cr;	//int c = cr;  cr是ci的别名，ci本身是一个顶层const
  auto d = &i;	//int *d = &i;
  auto e = &ci;	//const int *e = &ci; 对常量对象取地址是一种底层const
  ```

  如果希望推断出的auto类型是一个顶层const，需要明确指出：

  ```cpp
  const auto f = ci;		// const int f = ci;
  ```

  指定引用类型

  ```cpp
  auto &g = ci;		//const int &g = ci;
  auto &h = 42;		//错误，int &h = 42;
  const auto &j = 42; //const int &j = 42;
  ```

  

> auto 使用建议：
>
> 使用auto声明变量一定要做到心里有数，你知道编译器会推断出的什么样的类型
>
> 通常使用auto是对于一些类型名比较复杂的变量，使用auto写起来更方便



### 5.3 decltype 类型指示符

<span style="border:2px solid Red">C++11</span>  `decltype` 可以不执行表达式，编译器自动推断出表达式的返回值类型

```cpp
decltype(f()) sum = x;		//sum的类型和f()的返回类型一样
```

通过 `f()` 推断出返回类型，但是并不会执行 `f()`



#### decltype 和const

`decltype`处理顶层 consth和引用的方式和auto有点不同，如果 decltype使用的表达式是一个变量，则decltype返回该变量的类型（==包括顶层const和引用在内==）

```cpp
const int ci = 0, &cj = ci;
decltype(ci) x = 0;		//const int x = 0
decltype(cj) y = 0;		//const int &y = 0;
decltype(cj) z;			//错误， const int &z;  引用必须初始化
```





#### decltype 和引用

```cpp
int i = 42, *p = &i, &r = i;
decltype(r + 0) b;		//int b;
decltype(*p) c;			//错误， int &c; 引用需要初始化
```

> `r` 是引用  `decltype(r)` 是引用，但是 `r + 0` 是一个int型数据
>
> 解引用指针得到的是指针所指的对象，，因此 `decltype(*p)` 是 `int&`

变量加上 `()` 得到的是引用类型

```cpp
decltype((i)) d;   	//错误， int& d; 引用类型需要初始化
decltype(i) e;		// int e;
```

==`decltype((variable))` 的结果永远是引用==





## 6. 自定义数据结构

这里的自定义数据结构就是指类类型的数据，在C++中定义类的关键字有`class` 和 `struct`

```cpp
class ClassName{
	//属性
	//方法
};

struct ClassName{
	//属性
	//方法
};
```

> `class` 和 `struct` 在功能上是完全一样的，两者唯一的不同是默认的权限不同
>
> `class`默认的权限是私有的(private), 而 `struct` 是公有的(public)



*注意：c语言中的结构体是不能有方法（函数）*



关于类更具体的介绍在后面的章节~~

 
