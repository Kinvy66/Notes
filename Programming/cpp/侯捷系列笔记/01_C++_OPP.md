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
    complex(double r = -, double i = 0)
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

