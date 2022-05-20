# Redis

参考 [黑马程序员Redis入门到精通，深入剖析Redis缓存技术，Java企业级解决方案必看的redis教程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1CJ411m7Gc?p=1)



## 1. 安装



## 2. 基本操作

### 2.1 信息添加

命令

```shell
$ set key value
# eg
$ set name kk  
```



### 2.2 信息查询

命令

```shell
$ get key 
# eg
$ get name
```

根据 key 查询对应的 value，如果不存在，返回空（nil）



### 2.3 退出客户端

```shell
$ quit
$ exit
```





## 3. Redis数据类型

Redis数据类型（5中常用）

- string       String
- hash         HashMap
- list             LinkedList
- set             HashSet
- sorted_set    TreeSet



### 3.1 string

- redis 自身是一个 Map，其中所有的数据都是采用 key : value 的形式存储

- 数据类型指的是存储的数据的类型，也就是 value 部分的类型，key 部分永远都是字符串

  ![image-20220308123008117](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220308123008117.png)



**string类型**

- 存储的数据：单个数据，最简单的数据存储类型，也是最常用的数据存储类型

- 存储数据的格式：一个存储空间保存一个数据

- 存储内容：通常使用字符串，如果字符串以整数的形式展示，可以作为数字操作使用

  ![image-20220308123111893](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220308123111893.png)

#### 1. string类型数据的基本操作

- 修改/添加数据

  ```shell
  $ set key value
  ```

- 获取数据

  ```shell
  $ get key
  ```

- 删除数据

  ```shell
  $ del key
  ```



- 添加/修改多个数据

  ```shell
  $ mset key1 value1 key2 value2 ... 
  ```

- 获取多个数据

  ```shell
  $ mget key1 key2 ...
  ```

- 获取数据字符个数（字符串长度）

  ```shell
  $ strlen key
  ```

- 追加信息到原始信息后部（如果原始信息存在就追加，否则新建）

  ```shell
  $ append key value
  ```



#### 2. string类型数据的扩展操作

- 设置数值数据增加指定范围的值

  ```shell
  $ incr key
  $ incrby key increment   #增加指定的值increment， 可以为负值
  $ incrbyfloat key increment  #增加小数值
  ```

- 设置数值数据减少指定范围的值

  ```shell
  $ decr key
  $ decrby key increment
  ```



**string 作为数值操作**

- string在redis内部存储默认就是一个字符串，当遇到增减类操作incr，decr时会转成数值型进行计算。
- redis所有的操作都是原子性的，采用单线程处理所有业务，命令是一个一个执行的，因此无需考虑并发带来的数据影响。
- 注意：==按数值进行操作的数据，如果原始数据不能转成数值，或超越了redis 数值上限范围，将报错。== 9223372036854775807（java中long型数据最大值，Long.MAX_VALUE）



#### 3. string类型数据操作的注意事项

- 数据操作不成功的反馈与数据正常操作之间的差

  **表示运行结果是否成功**

  - (integer) 0 → false 失败
  - (integer) 1 → true 成功

  **表示运行结果值**

  - (integer) 3 → 3   3个
  - (integer) 1 → 1    1个

- 数据未获取到 

   （nil）等同于null

- 数据最大存储量 512MB
- 数值计算最大范围（java中的long的最大值） 9223372036854775807



#### 4. key的设置约定

数据库中的热点数据key命名惯例

![image-20220308124626457](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20220308124626457.png)



