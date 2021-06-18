# Java基础

## 1.  开发环境搭建

1. [JDK](https://www.oracle.com/cn/java/technologies/javase-downloads.html)下载

2. 安装，默认配置，路径可更改

3. 设置环境变量

   ![image-20210618092654482](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210618092701.png)

![image-20210618092718819](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/20210618092718.png)



## 2. HelloWorld

**HelloWorld.java**  (文件名和类名要一样)

```java
//单行注释
public class HelloWorld {
    /*
    多行注释
    */
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
```



编译运行命令

```bash
javac HelloWorld.java	#编译
java HelloWorld		#运行

```





## 3. 标识符、常量、变量和数据类型

### 3.1 标识符

* **命名规则**

  字母和数字，下划线，

  不能以数字开头

  不能是关键字

* **命名规范**

  类名规范：首字母大学，后面每个单词首字母大写（大驼峰）eg:HelloWorld

  变量名规范：首字母小写，后面每个单词首字母大写（小驼峰）

  方法名规范：同变量名



### 3.2  常量



常量：在程序运行期间固定不变的数据

* 分类：字符串常量，整数常量，浮点数常量，字符常量，布尔常量，空常量(null)



### 3.3  变量和数据类型

基本数据和C/C++一致， ==char 是两个字节,bool是一个字节==

引用数据类型：类，数组，接口，Lambda





**注意事项：**

> 1. 字符串不是基本类型，而是引用类型
> 2. 浮点型可能只是一个近似值，并非精确的值，故最后不要比较浮点数的大小
> 3. 数据范围与字节数不一定相等，例如float数据范围比long更加广泛，但是flat是4字节，long是8字节
> 4. java中的默认数据类型：整数类型是 `int` ,浮点型是`double`，要使用long或flota在数据后加L或F



### 3.4  数据类型转换

* 自动转换： 数据范围从小到大
* 强制类型转换:  `(转换类型)变量`



> 强制类型转换不推荐使用，会出现数据进度损失







## 4.  算术运算

* 算术运算符：`+` `-` `*` `/` `%`  `++`  `--`

* 赋值运算符：`=` `+=` `-=`  `*=` `/=` `%=`
* 比较运算符：`<` `>` `==` `<=`  `>=` `!=`
* 逻辑运算符：`&&`  `||`  `!`
* 三目运算符： `? :`



## 5.  方法入门

方法即类中的函数

**示例：**

```java
public class Demo04Method {
    public static void main(String[] args) {
        func();
    }

    public static void func(){
        System.out.println("func()");
    }
}

```



> java的方法不用声明，且可以先调用后定义





## 6.  JShell

类似于Python，可直接调用java的方法，可以一句一句执行



**编译器的优化：**

```java
public class Demo03DataType {
    public static void main(String[] args) {
        short a = 10;
        short b = 20;
        //short + short --> int + int --> int 
        //short c = a + b;  //错误写法, 左侧需要是int类型

        //右侧不用变量，而是采样常量，而且只有两个常量，没有变量
        //编译器会直接计算出结果,这称为编译器的常量优化
        short result = 10 + 1;
        System.out.println(result);


        //short = 10 + a + 1;     //错误，有变量无法实现常量优化
    }
}

```





## 7.  程序流程控制



### 7.1 顺序结构

从上到下的执行方式，根据编写顺序执行



### 7.2  选择结构

* `if`  `if-else`  `if-else if-else if`

  ```java
  if(关系表达式) {
      语句体；
  }
  ```

  > 基本语法和C/C++一致





















