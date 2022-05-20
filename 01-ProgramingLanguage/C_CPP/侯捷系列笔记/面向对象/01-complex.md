# 一 、Complex

本章节的代码： `complex.h` , `comples-test.cpp`

基于对象&面向对象

<img src="https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220220144438939.png" alt="image-20220220144438939"  />

**Object Based :** 面对的是单一class的设计

**Object Oriented :** 面对的多重classes的设计，classes和classes之间的关系



## 1. 头文件与类的声明

### 1.1 防卫式声明

```cpp
#ifndef __MYCOMPLEX__
#define __MYCOMPLEX__

//...

#endif   //__MYCOMPLEX__
```

在vs中支持下面写法

```cpp
#program once
```



`complex-test.h`

```cpp
#include <iostream>
#include "complex.h"

using namespace std;

ostream&
operator << (ostream& os, const complex& x)
{
  return os << '(' << real (x) << ',' << imag (x) << ')';
}

int main()
{
  complex c1(2, 1);
  complex c2(4, 0);

  cout << c1 << endl;
  cout << c2 << endl;
  
  cout << c1+c2 << endl;
  cout << c1-c2 << endl;
  cout << c1*c2 << endl;
  cout << c1 / 2 << endl;
  
  cout << conj(c1) << endl;
  cout << norm(c1) << endl;
  cout << polar(10,4) << endl;
  
  cout << (c1 += c2) << endl;
  
  cout << (c1 == c2) << endl;
  cout << (c1 != c2) << endl;
  cout << +c2 << endl;
  cout << -c2 << endl;
  
  cout << (c2 - 2) << endl;
  cout << (5 + c2) << endl;
  
  return 0;
}

```



### 1.2 头文件的布局

![image-20220220145953076](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220220145953076.png)

## 2. class 的声明（declaration）

![image-20220220150333698](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220220150333698.png)

## 3. class template（模板）简介

![image-20220220192510867](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220220192510867.png)



## 4. inline（内联）函数

![image-20220220192739926](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220220192739926.png)

内联函数类似于宏，在调用出展开，`inline`  只是给编译器的建议，是否 inline取决于编译器



## 5. access level （访问级别）

![image-20220220192946134](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220220192946134.png)



一般情况下数据是 `private` , 对于外界需要调用的接口使用 `public`



## 6. constuctor（ctor 构造函数）

![image-20220220193328806](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220220193328806.png)

构造函数可以有重载

一种构造放在`private` 区域的用法，单例设计模式

```cpp
//singleton
class {
public:
    static A& getInstance();
    setup() { /*...*/ }
    
private:
    A();
    A(const A& rhs);
    //...
};

A& A::getInstance()
{
    static A a;
    return a;
}

//调用
A::getInstance.setup();

```





## 6. 常量成员函数

![image-20220306104556770](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220306104556770.png)

对于不改变数据内容的函数加上 `const`

代码分析：

左边的，在加了`const` 的情况下调用没有语法错误，即非常量实例对象可以调用常量成员

右边，如果声明成员函数时没有加`const`,那么只能被非常量的实例调用，上面代码中使用常量实例调用非常量成员函数是错误的。

==总结：如果确定成员函数一定不会改变数据，那么最好声明为常函数==





## 7. 参数传递

参数传递的两种方式：1. pass by value（值传递）， 2. pass by reference （引用传递）

![image-20220306105356061](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220306105356061.png)

建议使用引用传参，如果是希望实参不被修改，那么可以传递常量引用



## 8. 参数返回

返回的两种方式：1. pass by value（值传递）， 2. pass by reference （引用传递）

![image-20220306110026132](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220306110026132.png)

==相同class的各个objecs互为友元==





## 8. 操作符重载









