# JavaWeb

## 1. 系统各个层级

DAO层：==对数据库的操作==
DAO层叫数据访问层，全称为data access object，属于一种比较底层，比较基础的操作，具体到对于某个表的增删改查，也就是说某个DAO一定是和数据库的某一张表一一对应的，其中封装了增删改查基本操作，建议DAO只做原子操作，增删改查。

Service层：
Service层叫服务层，被称为服务，粗略的理解就是对一个或多个DAO进行的再次封装，封装成一个服务，所以这里也就不会是一个原子操作了，需要事物控制。

Controler层：==和页面交互==
Controler负责请求转发，接受页面过来的参数，传给Service处理，接到返回值，再传给页面。

POJO层： ==(domain)将表中的字段封装成一个类==
POJO是Plain Ordinary Java Objects的缩写不错，但是它通指没有使用Entity Beans的普通java对象，可以把POJO作为支持业务逻辑的协助类。POJO有一些private的参数作为对象的属性。然后针对每个参数定义了get和set方法作为访问的接口。

Utils基本工具

![image-20211118170009783](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20211118170009783.png)







## 2. HTTP

- HTTP 协议
- Response对象
- ServletContext对象



### 1. HTTP协议

1. 请求消息： 客户端发送给服务端的消息

   数据格式：

   1. 请求行
   2. 请求头
   3. 请求空行
   4. 请求体

2. 响应消息：服务端发给客户端的消息

   数据格式：

   1. 响应行
   2. 响应头
   3. 响应空行
   4. 响应体





## 3. 请求方式

### 1. GET

用来获取（查询数据）查询参数跟在url的后面



> select *  from [table]



### 2. POST

post请求一般是对服务器的数据做改变，常用来数据的提交，新增操作。

特点：

post请求的请求参数都是请求体中

post请求本身HTTP协议也是没有限制大小的，限制它的是服务器的处理能力



> insert into [table] (column1, column2, ..) values (value1, value2...)



### 3.PUT

put请求与post一样都会改变服务器的数据，但是put的侧重点在于对于数据的修改操作，但是post侧重于对于数据的增加



> update [table] set column1 = value1, ..... where [condition]



### 4. DELETE



> delete from [table] where [condition]







## 3 数据库的关系和操作

- 外键在多的一方
- 一对多的关系，有外键关联的情况下，外键表是副表，另一个是主表
- 关联表的操作
  - 增加元素，先增加主表，在增加副表
  - 删除数据先删副表，再删主表



