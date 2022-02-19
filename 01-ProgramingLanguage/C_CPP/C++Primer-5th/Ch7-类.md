# 第7章 类



## 类的基本概念

本小节的内容对应书中第2章最后一节（2.6 自定义数据结构）

正如标题，**类**就是一种自定义数据结构，这种数据结构把多个变量和函数封装在一起。几个关于类的几个基本概念：

- **成员变量**， 也叫**类的属性** ，就是类中声明定义的变量，可以是基本类型变量或是类类型变量
- **成员函数**，也叫方法，就是类中声明的函数
- **实例对象**，通过类类型创建的变量

在后面的这些名称会混着用

定义类的语句形式：

```cpp
//使用struct关键字
struct ClassName{
  //类属性
  //...  
  
  //方法
  //...
};
//使用class关键字
class ClassName{
  //类属性
  //...  
  
  //方法
  //...
};
```



> 说明：
>
> 1. `struct` 和 `class` 定义类两者基本是等价的，只是默认的访问权限不同，关于权限的问题在7.2节会详细讲解，在这之前我们定义类都使用 `struct`
> 2. 类中的成员变量（属性）定义的位置不影响调用，即可以在类的任意位置，也就是说我们可以在声明定义一个变量之前就可以使用改变量，这个规则只限于类方法和类属性
> 3. 定义类的语法 `{}` 后面有一个 `;` ,不用漏了





## 1. 定义抽象数据类型

本小节是一个具体的实例，设计一个 `Sales_data` 类，这个类在第二章有讲到，我们不用回头看第二章，直接跟着书中的步骤就可以了。



### 1.1 设计 Sales_data 类

我们知道类有属性和方法，设计一个类首先要确定这些（这是根据类的功能确定的）。这个类是表示书的销售，这里直接给出类需要的属性和方法。

类的接口（对外可以使用的函数，部分函数不是类的成员函数）

- 一个 `isbn` 成员函数，用于返回对象的ISBN编号
- 一个 `combine` 成员函数，用于将一个 Sales_data 对象加到拎一个对象上
- 一个 `avg_price`成员函数，用于返回售出数书籍的平均价格
- 一个名为 `add` 的函数，指向两个Sales_data 对象的加法
- 一个 `read` 函数，将数据从 istream 读入到 Sales_data 对象中
- 一个 `print` 函数，将Sales_data 对象的值输出到 ostream

成员变量：

- `bookNo` 表示 ISBN编号，string类型
- `units_sold` 表示某本数的销量， unsigned
- `revenue` 表示这本书的总销售收入

对应类的定义代码

```cpp
//Sales_data.h
struct Sales_data{ 
  	//成员函数
  	std::string isbn() const { return bookNo; }
  	Sales_data& combine(const Sales_data&);
    dobule avg_price() const;
    
    //成员变量
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
  
};
//Sales_data的非成员接口函数
Sales_data add(const Sales_data&, const Sales_data&);
std::ostream &print(std::ostream&, const Sales_data&);
std::istream &read(std::istream&, Sales_data&);
```



#### Sales_data 类的说明

使用下面的语句定义一个 Sales_data 类型的对象

```cpp
Sales_data total;		//total 是一个类对象
```



##### 1. 引入 this

使用total对象对isbn 函数的调用：

```
total.isbn();
```

我们可以看到 `isbn()` 的函数体内容是 `return bookNo;` 我们知道上面的调用语句返回的就是 `total` 对应的 `bookNo` 属性（`total.bookNo)`，但是在 `isbn()` 函数体内并没显式的指明需要返回哪个实例对象的属性，这里其实有一个隐式的参数 `this`.

`this` 是一个==指针==，准确的说是一个常量指针，指向的是当前调用该函数的对象的地址。比如上面的调用语句，this 指向的是 total 的地址，所以上面的调用过程是：

```cpp
//伪代码，用于说明调用成员函数的实际过程
Sales_data::isbn(&total);
```

每个成员函数都会一个隐式的形参`this`，实际 `isbn()` 成员函数为

```cpp
std::string isbn(Sales_data *const this);	//错误代码
```

==上面代码是为了说明成员函数有一个名为this的隐式形参，实际代码不能把这个形参写出来==

虽然不能写出来，但是我们在成员函数体内可以使用`this` 这个形参名，比如 isbn的函数体可以改成

```cppp
return this->bookNo;		//正确，返回当前对象实例的bookNo属性
```



##### 2. 引入const成员函数

```cpp
std::string isbn() const { return bookNo; }
```

`isbn()` 函数还有一个之前没有出现的知识点，我们可以看到在函数的参数列表后面还有一个 `const` 关键字，把这种形式的成员函数叫做 **常量成员函数** （简称 常函数）

常量成员函数的本质实际上是对 `this` 指针的限制，前面说到 `this` 是一个常量指针，类型是 `Sales_dat *const` ，这是只有顶层const，而常量成员函数又加上了底层const，`this`指针变成了 `const Sales_data *const` 类型（关于顶层const和底层const在第二章有详细的讲解）。`isbn` 函数真正的原型为

```cpp
std::string isbn(const Sales_data *const this) { return bookNo; }		
```

==再次说明，this是一个隐式形参，实际代码不能把这个形参写出来==



常量成员函数和普通的成员函数有什么区别呢？它们是不是一组重载函数？

```cpp
std::string isbn() const { return bookNo; }		//1
std::string isbn() { return bookNo; }			//2
```

==它们是重载函数== ，我们把这两个函数的真实的形式写出来，以同样的方式和条件调用，看下是否只有唯一一个匹配的函数。==再再次说明，实际代码不能把this形参显式写出来==

```cpp
//isbn() 的真实形式，实际代码不能把this写出来
std::string isbn(Sales_data *const this);			//普通成员函数
std::string isbn(const Sales_data *const this);		//常量成员函数	

//定义两个 Sales_data 类型变量
Sales_data total;
const Sales_data c_total;
total.isbn();		//1
c_total.isbn();		//2

//对应的伪代码，用于说明调用成员函数的实际过程
Sales_data::isbn(&total);		//调用 std::string isbn(Sales_data *const this);	
Sales_data::isbn(&c_total);		//调用std::string isbn(const Sales_data *const this);
```

传参的规则实际和变量初始化的规则一样（第二章中的内容），我们观察下面的几个变量初始化

```cpp
Sales_data total;
const Sales_data c_total;

Sales_data *const this = &total;			//正确，用一个非常量对象初始化一个顶层const
Sales_data *const this = &c_total;			//错误，&c_total包含一个底层const

const Sales_data *const this = &total;		//错误	
const Sales_data *const this = &c_total;	//正确
```



> 总结：常函数只能调用被常对象调用，非常量对象既可以调用常量函数，也可以吃调用普通函数



以上内容比较抽象，建议结合2.4节内容理解，关于常函数还有部分的知识点，后面的章节再讲



#### 类作用域和成员函数

在 `isbn()` 函数中使用了 `bookNo` 成员变量，而这个变量的声明式在函数的后面。按照之前关于作用域的知识，变量使用前必须声明，这里和编译器的处理方式有关。编译器对类的处理分两步：首先编译成员的声明，然后才轮到成员函数。因此，成员函数体可以随意使用类中的其他成员而无须在意这些成员出现的次序。



#### 在类的外部定义成员函数

`Sales_data` 类的成员函数只有 `isbn()`有定义，其他的成员函数都是只有声明。关于成员函数，它是支持类内声明，类外定义的。类外定义函数需要包含所属的类名，具体形式如下

```cpp
//avg_price() 的类外定义
double Sales_data::avg_price() const {
    if(units_sold)
        return revenue / units_sold;
    else
        return 0;
}
```

成员函数类外定义和普通函数的定义没有什么区别，只是成员函数需要在函数名的前面加上对应的类名。

==类内定义的成员函数默认是inline函数，定义在类外的要成为内联函数，需要显显式的指定，在函数定义的前面加 inline关键字==



#### 定义一个返回this对象的函数

函数 `combine` 的设计初衷类似于复合赋值运算符 `+=` , 调用该函数传入的是一个 Sales_data对象，返回的还是该对象本身，这里我们可以使用 `this` 指针实现

```cpp
Sales_data& Sales_data::combine(const Sales_data &rhs)
{
    units_sold += rhs.units_sold;
    revenue += rhs.revenue;
    return *this;		//this 是调用该函数的对象的指针，对其解引用得到的就是该对象
}
```

==再再再次说明，this 是一个隐式形参，不能写出来，但是可以再函数体中使用==



### 1.3 定义类的非成员函数

`add` ，`read`，`print` 不是类的成员函数，但是它们出和该类相关的接口函数，所以把它们和类定义在同一个文件中，以下是这三个函数的定义

```cpp
istream &read(istream &is, Sales_data &item)
{
    double price = 0;
    is >> item.bookNo >> item.units_sold >> price;
    item.revenue = price * item.units_sold;
    return is;
}
ostream &print(ostream &os, const Sales_data &item)
{
    os << item.isbn() << " " << item.units_sold << " "
        << item.revenue << " " << item.avg_price();
    return os;
}
Sales_data add(const Sales_data &lhs, const Sales_data &rhs)
{
    Sales_data sum = lhs;
    sum.combine(rhs);
    return sum;
}
```



各个函数功能不作过多的说明



### 1.4 构造函数

<span style="border:2px solid Red">C++11</span>  新标准允许在类属性定义时初始化，比如`Sales_data` 类中`units_sold ` 和 `revenue ` 都被初始化为0.但是并不是所有的属性都需要在类内初始化的，有些可能需要类的使用者自定义的初始化。这个时候我们就需要要到类的 **构造函数** ，构造函数的形式：类名就是函数名，没有返回值

```cpp
struct Entity{
    double x, y;
    //构造函数
    Entity()
    {
       x = 0;
       y = 0;
    }
    
    void print()
    {
        cout << x << "," << y << endl;
    }
}

int main()
{
    Entity e;	//等价   Entity e;   e.Entity(); 两个语句
    e.print();
    
    return 0;
}
```

构造函数不需要显示的调用，在创建对象实例时，会自动调用构造函数



#### 构造函数可以重载

关于构造函数

- 在没有写构造函数的情况下，编译器会提供一个**默认构造函数**，该函数是没有参数的，并且不执行任何操作，对于没有参数的构造函数也叫称作**无参构造**
- 构造函数可以重载，重载的有形参的构造函数也叫做**有参构造**
- 只要写了任何一种构造函数（有参构造或无参构造），编译器就不再提供默认的构造函数

对于 `Sales_data` 的实例，设计了以下构造函数

```cpp
struct Sales_data {
    //新增的构造函数
    Sales_data() {  }		//无参构造
    Sales_data(const std::string &s) : bookNo(s) { }		//有参构造1
    Sales_data(const std::string &s, unsigned n, double p):
    			bookNo(s), units_sold(n), revenue(p*n) {}   //有参构造2
    Sales_data(std::istream &);		//有参构造3
    
};
```

有参构造1和2使用了**初始化列表**的方式初始化成员属性 ，即形参列表后面和函数体`{}` 之间的语句

```cpp
//有参构造1的等价形式
Sales_data(const std::string &s) { bookNo = s; }
//有参构造2的等价形式
Sales_data(const std::string &s, unsigned n, double p)
{
    bookNo = s;
    units_sold = n;
    revenue = p*n; 
}
```

使用 `=` 赋值运算符和使用初始化列表初始化成员属性效果是一样的。但是初始化列表的方式而且更高效，==强烈建议使用初始化列表初始化成员属性==

构造函数的类外定义

```cpp
//其他的构造已经在类内定义了
inline Sales_data::Sales_data(std::istream &is)
{
    read(is， *this);
}
```

==定义在类内的函数，自动成为内联函数==， 在类外定义成员函数，如果需要成为内联函数，需要手动添加 `inline` 关键字



#### 构造函数的调用

构造函数不需要我们手动的调用，也没有提供给我调用的语法，构造函数的调用是编译器根据我们初始化实例对象的方式调用不同的构造函数

```cpp
//1.调用无参构造
Sales_data total;	
//使用括号调用无参构造
Sales_data();	//会创建一个临时的对象，如果需要使用这个对象就要变量接收
Sales_data total = Sales_data();	//用total接收临时变量
Sales_data total();		//错误，这不不调用无参构造创建实例对象，而是声明一个返回类型为Sales_data的函数

//2. 调用有参构造
Sales_data total("654323");		//调用 Sales_data(const std::string &s)构造函数创建实例
```

构造函数：

1. 构造函数，没有返回值也不写void
2. 函数名称与类名相同
3. 构造函数可以有参数，因此可以发生重载
4. 程序在调用对象时候会自动调用构造，无须手动调用,而且只会调用一次





### 1.5 拷贝、赋值和析构

c++编译器至少给一个类添加4个函数

1. 默认构造函数（无参，函数体为空）
2. 默认析构函数（无参，函数体为空）
3. 默认拷贝构造函数，对属性进行值拷贝
4. 赋值运算符 `operator=`，对属性进行值拷贝



#### 析构函数

默认构造函数前面已经提过了，**析构函数** 也是由编译器调用的，它的调用时机是在对象销毁的时候被调用，析构函数的作用一般是用来释放内存空间（主要是堆上的内存空间），它语法形式如下

```cpp
//Sales_data的析构函数
struct Sales_data {
    //..
    
    //析构函数
    ~Sales_data()
    {
        //...
    }
};
```

析构函数语法 ：`~类名() {}`

1. 析构函数，没有返回值也不写void
2. 函数名称与类名相同,在名称前加上符号 ~
3. 析构函数不可以有参数，因此不可以发生重载
4. 程序在对象销毁前会自动调用析构，无须手动调用,而且只会调用一次



#### 拷贝构造函数

下面的语句会调用拷贝构造函数

```cpp
//trans 是一个已经定义的 Sales_data 对象
Sales_data total(trans);	//1
Sales_data total = trans;	//2
//下面的语句不是调用拷贝构造
Sales_data total;
total = trans;		//调用的是赋值操作
```

默认拷贝构造函数的操作等价于把属性进行值拷贝，等价的语句

```cpp
//1 和 2等价的语句
total.bookNO = trans.bookNo;
total.units_sold = trans.units_sold;
total.revenue = trans.revenue;
```



#### 赋值

赋值操作是通过重载赋值运算符来实现的,  `operator=`

```cpp
Sales_data total;
total = trans;		//调用的是赋值操作
```

编译器提供的默认赋值运算和默认拷贝构造操作是一样的，就是对属性值进行值拷贝。





> 拷贝构造函数和赋值操作也可以自定义，如何自定义以及相关的使用在后面章节有详细的讲解，这里只是一个简单的介绍





## 2. 访问控制与封装

到目前为至我们定义类都是使用 `struct` 关键字，前面有提过 `class` 以及两者的区别。这小节是讲访问控制与封装。

首先，回顾一下面向对象编程的三大特点之一，封装。像之前那样把属性（变量）和方法（函数）集中到一个类中，这就是封装。但是真正意义的封装还需要加上访问控制，所谓访问控制就是对于类中的某些方法和属性在外部是无法访问的。举个例子，比如前面定义的`Sales_data` 类，我们使用的是`struct` ,这种定义方式我们可以随意的修改类内的属性值，甚至多不许要调用方法

```cpp
Sales_data total;			//声明一个 Sales_data 的实例对象 total
total.units_sold = 10;		//通过类实例对象直接修改属性值
```

上面这种操作通常是不被允许的，如果类的设计者和使用这都是我们自己的话，我们明白（但代码量多到一定程度也不一定）不能直接这样修改类属性，特别是对于某些有限定范围的属性。所以这种类就不具有封装性，真正意义的封装除了代码的集合，还有属性和方法的对外可见性。

比如下面的示例

```cpp
struct Person
{
    int age;
    std::string;
    
    void print()
    {
        std::cout << "age = " << this.age << std::endl
    }
};

//类使用
int main()
{
    Person A, B;
    A.age = -10;		//人的年龄不可能是负数，但是代码并没有错误
    A.age = 1000;		//人的年龄不可能这么大
    A.print();
    B.print();
    
    return 0;
}
```

对于某些不能是负数的属性我们虽然可以通过类型限定，但是像年龄这样的属性（值在一定的范围内）只用类型限定就不太现实了。这是我们引入访问控制，使类的使用者不能够直接给属性设置值（可以通过调用方法给属性设定值）。

在C++中，我们使用访问说明符实现类的可见性的封装：

- 定义在`public` 说明符之后的成员在整个程序可被访问（以类示例对象的方式访问），一般 `public` 成员定义类的接口。
- 定义在 `private` 说明符之后的成员可以被类的成员函数访问，但是不能被使用该类的代码（通常是指类的实例对象）访问。

* 定义在 `protected` 说明符之后的成员可以被类的成员函数访问，但是不能被使用该类的代码（通常是指类的实例对象）访问，在类的继承中还会继续讲到 `protected`

我们使用访问说明符重新定义 `Sales_data` 类

```cpp
class Sales_data {
public:
    Sales_data() {  }		
    Sales_data(const std::string &s) : bookNo(s) { }		
    Sales_data(const std::string &s, unsigned n, double p):
    			bookNo(s), units_sold(n), revenue(p*n) {} 
    Sales_data(std::istream &);	
    std::string isbn() const { return bookNo; }
  	Sales_data& combine(const Sales_data&);
    
private:
    dobule avg_price() const;
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
    
};
```



> 说明：
>
> 1. 从访问说明符开始一直到下一个访问说明符，访问权限是不变的，例如`public` 后（直到下一个访问说明符）都是属于 `public` 的作用域
> 2. 在一个类中不同的访问说明符是没有顺序和数量的限制。
> 3. `struct` 和 `class` 基本是一样的，只是默认的访问权限不同，前者默认的是 `public` ,后者是 `private` . 如果手动的添加了访问说明符完全可以两者相互替换。



### 2.1 友元

除了 `Sales_data` 的成员函数，我们还定义了三个类外的成员，它们也是对该类的操作，所以一般会把它们放到同一个文件中。这三个函数需要操作类中的属性，但是属性已经是 `private` 成员，外部是无法访问的，这里我们可以使用 **友元**。将某个类或函数声明为另一个类的友元，那么它们就可以访问另一个类中的私有成员。

具体语法 `friend 类或函数`  

```cpp
class Sales_data
{
friend Sales_data add(const Sales_data&, const Sales_data&);
friend std::ostream &print(std::ostream&, const Sales_data&);
friend std::istream &read(std::istream&, Sales_data&);
    //后面的成员定义同上
};
```

说明

> 在类内声明了友元函数，不能看做函数的声明，这个只是声明友元，==在类外还是需要声明函数的原型== 。
>
> 友元的声明位置没有限制可以在类内的任何位置，一般建议集中声明在类的开始或是结束。







## 3. 类的其他特性

































