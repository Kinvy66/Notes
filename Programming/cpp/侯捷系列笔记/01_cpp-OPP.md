# C++面向对象高级编程



## 1. 简介

* 基于对象 c++ class

  class without pointer mebers

  class with pointer mebers

* 面向对象  class之间的关系

  继承，复合，委托

参考代码 : `complex `   `string`



## 2. 头文件与类的声明

### 2.1  头文件的声明

**示例：** `complex.h`

```c++
//防卫式声明
#ifndef __COMPLEX__
#define __COMPLEX__
//类声明

#endif
```



### 2.2  类的声明



```c++
class Complex
{
public:
    Complex (double r = 0, double i = 0)
        : re(r), im(i)
    { }
    Complex& operator+=(const Complex&);
    double real() const { return re;}
    double imag() const { return im;}

private:
    double re, im;

    friend Complex& __doapl (Complex*, const Complex&);
};


inline double
imag (const Complex& x)
{
    return x.imag();
}
```

* 内联函数

  声明和定义在类内的方法默认是inline函数，外部定义需要加 `inline` 关键字，但是无论在哪里，inline只是给编译器的建议，编译器会根据方法的复杂程度决定是否称为inline函数。

* 成员权限

  对于属性成员和不想外部调用的方法建议设置为==private==





## 3.  构造函数（ctor)

## 3.1  构造函数

```c++
//初始化列表方式
Complex (double r = 0, double i = 0)
    : re(r), im(i)  { }

//赋值方式
Complex (double r = 0, double i = 0)
{ re = r; im = i;}
```

> 构造函数推荐使用初始化列表的方式给属性设定初始值. (C++的初始化和赋值的区别)



*不带指针的class基本不用析构*

## 3.2  构造函数的重载(overloading)

构造函数可以有多个重载，对于重载的成员函数，编译器编译之后是有不同的名称

==注意==：重载函数，在调用时不要出现歧义，这也是判断是否可重载的标准。



* 把构造函数放在 `private` 

  ```c++
  //Singleton 模式
  class A
  {
  public:
      static A& getInstance();
      setup() {....}
  private:
      A();
      A(const A& rhs);
  
      ...
  };
  
  A& A::getInstance()
  {
      static A a;
      return a;
  }
  
  //创建实例
  A::getInstance().setup();
  
  ```

  

### 3.3  常函数和常对象

在函数后面加 `const` , 如 real() 和 imag() 方法



```c++
{
    complex c1(2, 1);
    cout << c1.real();
    cout << c1.imag();
}

//常对象只能调用常函数
{
    const complex c1(2, 1);
    cout << c1.real();
    cout << c1.imag();
}
```

> 在设计一个class时，对于可能被常对象调用的方法，一定要加const关键字





## 4.  参数的传递

参数传递分为值传递和引用传递，==尽量传引用==

对于不想被更改的值，==加const关键字解决==

*以上建议也适用于函数的返回形式*



```c++
class complex
{
public:
    complex(double r = 0, double i = 0)
        : re(r), im(i) {}

    int func(const complex& pragma)
    {
        return pragma.re +pragma.im;
    }
private:
    double re, im;
}

{
    complex c1(2, 1);
    complex c2;
    c2.func(c1);
}
```

> 相同class的各个object互为友元



## 5. 操作符重载

* 成员函数操作符重载

```c++
inline complex&
__doapl(complex* ths, const const complex& r)
{
    ths->re += r.re;
    ths->im += r.im;
    return *ths;
}

inline complex&
complex::operator+=(const complex& r)
{
    return __doapl(this, r);
}
//成员函数的参会有用默认的参数，this参数，谁调用这个方法谁就是这this，但是不能不这个this写上去
inline complex&
complex::operator+=(this, const complex& r)
{
    return __doapl(this, r);
}

//调用
{
    complex c1(2,1);
    complex c2(5);
    
    c2 += c1;   //这里c2就是this参数  operator+=(c2, c1);
}
```



> 传递者无需指导接收者是以引用形式接收，返回引用是为了支持链式编程(`c3 += c2 += c1`)



* 非成员函数操作符重载

  ```c++
  //提供三种实现方式
  inline complex
  operator+(const complex& x, const complex& y)
  { 
      return complex (real(x) + real(y),
                      imag(x) + imag(y));
  }
  
  inline complex
  operator+(const complex& x, double y)
  {
      return complex (real(x) + y, imag(x));
  }
  
  inline complex
  operator+(double x, const complex& y)
  {
      return complex (x + real(y), imag(x))
  }
  
  //三种实现方式对应的调用
  
  {
      complex c1(2, 1);
      complex c2;
  
      c2 = c1 +c2;
      c2 = c1 + 5;
      c2 = 7 + c1;
  }
  ```
  
  

> 非成员函数无this，以上函数返回的不是引用，因为热门返回的必定的是个local object
>
> 临时对象： typename();





## 6.  三大函数--构造函数，构造拷贝，析构函数

以`string.c` 为例，class with pointer mebers



### 6.1  拷贝构造函数

没有写拷贝构造函数，编译器会给默认的拷贝构造函数，但是编译器给的是==浅拷贝==

> 类中带有指针一定不能使用编译给的默认拷贝构造



**示例：**

```c++
class String
{
public:
    String(const char* cstr = 0);
    String(const String& str);
    String& operator=(const String& str);
    ~String();
    char* get_c_str() const { return m_data; };
private:
    char* m_data;
};

inline 
String::String(const char* cstr= 0)
{
    if(cstr) {
        m_data = new char[strlen(cstr)+1];
        strcpy(m_data, cstr);
    }
    else {  //未指定初值
        m_data = new char[1];
        *m_data = '\0';
    }
}

inline
String::~String()
{
    delete[] m_data;
}
```



使用默认的拷贝构造和拷贝赋值会出现一些情况

![image-20210611171157486](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210611171204.png)

### 6.2 拷贝赋值函数

```c++
inline
String& String::operator=(const String& str)
{
    if(this == &str) {	//检测自我赋值
        return *this;
    }

    delete[] m_data;							//1
    m_data = new char[ strlen(str.m_data) + 1];	//2
    strcpy(m_data, str.m_data);					//3
    return *this;
}
```

>监测自我赋值的这段代码，不只是效率高低的问题
>
>如若没有检测自我赋值，当出现 `a=a` 时，代码执行步骤
>
>* 代码1，释放传入的a
>* 代码2，申请传入和a大小相同的内存，这里在1中已经释放了，所以执行到这里就出错了



==重载 = 一定要检测自我赋值==





## 7. 堆、栈与内存管理（参考黑马教程）

* 栈用于调用函数时，存放接收的参数，以及返回的地址。由系统管理
* 堆，通过 `new` 关键字申请的内存空间位于堆区，申请和释放都是有程序员手动管理





* `new` ： 先分配内存，再调用拷贝构造

  ```c++
  Complex* pc = new Complex(1,2);
  //上面代码，编译器会有一下操作
  Complex *pc;
  
  void* mem = operator new(sizeof(Complex))   //1. 分配内存， 调用 malloc(n)
  pc = static_cast<Complex*>(mem);            //2. 转换类型
  pc->Complex::Complex(1,2);                  //3. 构造函数, Complex::Complex(pc,1,2);
  ```





* `delet`: 先调用析构函数，再释放内存

  ```c++
  String* ps = new String("Hello");
  //...
  delete ps;
  //编译器转化为
  String::~String(ps);    //1. 析构函数
  operator delete(ps);    //2. 释放内存, 内部调用 free(ps);
  
  ```

  



## 8.  类和类之间的关系

类和类之间的关系

* 继承
* 复合
* 委托



### 8.1  复合  (has-a)

复合,即类中的成员是类的这种关系。

复合关系下的构造和析构：

构造由内而外，析构由外而内。



### 8.2  委托(Delegation)

委托的关系，类中成员有其他类实例指针， Compositon by reference



```c++

//file String.hpp
class StringRep;
class String
{
public:
    String(const char* cstr = 0);
    String(const String& str);
    String& operator=(const String& str);
    ~String();
//.....  
private:
    StringRep* rep;     //pimp1
};

//file String.cpp
#include "String.hpp"
namespace
{ 
    class StringRep 
    {
        friend class String;
        StringRep(const char* s);
        ~StringRep();

        int count;
        char* rep;
    };

}

String::String() { ... }
```





### 8.3  继承  is-a

*参考黑马教程笔记*





## 9.  虚函数和多态





 







