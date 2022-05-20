# C++

## typedef typename 的作用

**P584** 的一段代码

```cpp
typedef typename std::vector<T>::size_type size_type;
```

将typedef和typename关键字联用。

vector的源码

```cpp
template <class T,class Alloc=alloc>
class vector{
public:
//...
typedef size_t size_type;
//...
};
```

从vector的类定义可以看出，`vector::size_type`是`vector`嵌套类型定义，其实际等价于 `size_t`类型。

```cpp
vector<int>::size_type ssize;
//等价于
size_t ssize;
```

为什么要在typedef后面加上typename关键字？

原因：

实际上，模板类型在实例化之前，编译器并不知道`vector<T>::size_type`是什么东西，事实上一共有三种可能：

> 静态数据成员
> 静态成员函数
> 嵌套类型

那么此时`typename`的作用就在此时体现出来了——定义就不再模棱两可。

`typedef`创建了存在类型的别名，而`typename`告诉编译器`std::vector<T>::size_type`是一个类型而不是一个成员。



在 **P593** 也有相关的解释

 

## using 的用法

### 1. 引入命名空间

C++ Primer 5th （3.1.5 P74）

```cpp
using namespace std;  //将整个命名空间引入到当前作用域
using std::cout;      //将某个某个成员引入到当前作用域
```

在局部作用域中使用 `using`，C++ Primer-5th（13.3， P459)

```cpp
void swap(Foo &lhs, Foo &rhs)
{
    using std::swap;
    swap(lhs.h, rhs.h);  // lhs.h, rhs.h 是 HasPtr 类型
}
```

这里 `swap(lhs.h, rhs.h);` 并没有调用标准库中的 `swap`，而是调用了自定义的 `void swap(HasPtr& &lhs, HasPtr &rhs)` 。 引入标准库中的 `swap` 没有隐藏自定义的 `swap` ，而是和自定义的构成了重载关系。



### 2. 类型别名

C++ Primer 5th （2.5.1 P60）

C++11 新标准可以使用 `using` 关键字声明类型别名，和 `#define` 、`typedef` 功能类似，但更加直观

```cpp
#include <iostream>
using namespace std;

#define DString std::string    //! 不建议使用！

typedef std::string TString;   //! 使用typedef的方式
using Ustring = std::string;   //！使用  using typeName_self = stdtypename;

//更直观
typedef void (tFunc*)(void);
using uFunc = void(*)(void);

int main(int argc, char *argv[])
{

    TString ts("String!");
    Ustring us("Ustring!");    
    string s("sdfdfsd");
    
    cout<<ts<<endl;
    cout<<us<<endl;
    cout<<s<<endl;
    
    return 0;
}
```



### 3. 在继承中，改变父类成员的访问权限

C++ Primer 5th （15.5 P542）

在继承中访问权限遵循下面图示中的原则

![img](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/clip_image002.png)

以公有继承为例，在继承类中可以使用 `using` 关键字改变基类的访问权限

```cpp
class Base
{
public:
    void pub_mem();
protected:
    int prot_mem;
private:
    char priv_mem;
};

class Derved : public Base
{
 public:
    using Base:: prot_mem;   // 基类 prot_mem 成员访问权限变为 public 
 private:
    using Base::pub_mem;      // 基类 pub_mem 成员访问权限变为 private 
};

int main()
{
    Base base;
    Derved der;
    
    base.pub_mem();		// 使用基类对象访问成员的权限不会变
    
    der.pub_mem();		// 错误 继承类中改变了基类成员的访问权限，private
    der.prot_mem = 42;  // 正确 继承类中改变了基类成员的访问权限, public
	
    return 0;
}

```

使用 `using` 声明语句将父类的成员声明在继承类中，其访问权限由该声明语句之前的访问说明符决定的。

> 所以一个类如果是可以被继承的（没有使用 `final` 防止继承），那么可以使用子类对象访问基类中所有的成员（包括私有和保护成员）















