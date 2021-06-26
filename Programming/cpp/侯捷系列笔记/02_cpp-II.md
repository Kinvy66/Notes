# C++ 面向对象（II） 兼谈对象



## 1. 转换函数

### 1.1

**示例：**

```c++
class Fraction
{
public:
    Fraction(int num, int den = 1)
        : m_numerator(num), m_denominator(den) {}

    operator double() const
    {
        return (double)(m_numerator / m_denominator);
    }

private:
    int m_numerator;   //分子
    int m_denominator; //分母
};

Fraction f(3, 5);
double d = 4 + f; //调用 operator double() 将 f 转为 0.6
```



> `operator double()` 就是转换函数，不用写返回值









### 1. 2non-explicit-one-argument ctor



**示例：**

```c++
//non-explicit-one-argument ctor
class Fraction
{
public:
    Fraction(int num, int den = 1)
        : m_numerator(num), m_denominator(den) {}

    Fraction operator+(const Fraction& f)
    {
        return Fraction(...);
    }

private:
    int m_numerator;   //分子
    int m_denominator; //分母
};

Fraction f(3, 5);
double d = 4 + f; //调用 non-explicit ctor 将 4 转为 Fraction(4,1). 然后调用operator+

```



> 如果1中的转换函数和2的`operator+`同时出现的话，编译出错，二义性



```c++
explict Fraction(int num, int den = 1)
        : m_numerator(num), m_denominator(den) {}
```

> 告诉编译器不要自动调用 `Fraction()` ，它就是一个普通的ctor





## 2. pointer-like classes, 智能指针

