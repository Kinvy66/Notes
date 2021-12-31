# Mysql 数据库

## 1. 原理定义概念

### 1.1 安装

#### **下载** 

 [Mysql](https://dev.mysql.com/downloads/mysql/)

![image-20210808171411499](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808171411499.png)

#### **将压缩包解压**

![image-20210808174534880](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808174534880.png)

#### **添加环境变量**

![image-20210808174724993](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808174724993.png)

#### **添加配置文件**  

`my.ini`

![image-20210808175832389](https://kinvy-images.oss-cn-beijing.aliyuncs.com/Images/image-20210808175832389.png)

my.ini 内容

```ini
[mysqld] 
# 设置 3306 端口 
port=3306 
# 设置 mysql 的安装目录 
basedir=C:\\Env\\mysql-8.0.25-winx64
# 设置 mysql 数据库的数据的存放目录
datadir=C:\\Env\\mysql-8.0.25-winx64\\data 
# 允许最大连接数 
max_connections=200 
# 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统 
max_connect_errors=10 
# 服务端使用的字符集默认为 UTF8 
character-set-server=utf8 
# 创建新表时将使用的默认存储引擎 
default-storage-engine=INNODB 
# 默认使用“mysql_native_password”插件认证 
default_authentication_plugin=mysql_native_password 
[mysql] 
# 设置 mysql 客户端默认字符集 
default-character-set=utf8 
[client] 
# 设置 mysql 客户端连接服务端时默认使用的端口 
port=3306 
default-character-set
```



#### **安装**

以管理员运行cmd

初始化

```powershell
mysqld –initialize –console  #记住密码
```

安装

```powershell
mysqld –install
net start mysql		#启动
```

登录

```powershell
mysql -u root -p   # 输入密码 123456
```

修改初始化

```powershell
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';
```

若要删除mysql，可执行命令

```powershell
mysqld --remove mysql
```



> 安装文件安装参考：https://www.bilibili.com/video/BV1V5411g7EK?p=3&spm_id_from=pageDriver

### 1.2 基本概念

 分类：

* DDL   ---   数据库定义语言
* DML   ---   数据库操作语言  增删改（CRUD）
* DQL   ---    数据库查询语言
* DCL   ---     数据 库控制语言

## 2. SQL-DQL语句

* 格式
  * select 列名*N from 表名 where 查询条件1  and/or 查询条件2  group by 列 Having 分组条件 Order by 排序

* 规则
  * sql在书写的时候除了查询条件之外，大小写都可以
    * select * from user where uname='xd';
    * SELECT * FROM USER WHERE UNAME='xd';
  * `--`属于SQL语句的注释
  * 所有的查询条件为字符串是，需要用`"` 进行修饰，否则就会被当做列名处理

* select查询列和别名
  ```sql
  -- 查询所有员工信息（*通配符，默认所有的列）
  SELECT * FROM emp;
  -- 查询员工姓名
  SELECT ename FROM emp;
  --查询员工的薪资
  SELECT sal FROM emp;
  --查询员工的姓名和薪资
  SELECT ename, sal FROM emp;
  SELECT ename sal FROM emp;
  SELECT ename sal comm FROM emp;
  --查询员工的姓名和薪资，推荐使用单引号
  SELECT ename '员工姓名', sal '薪资' FROM emp;
  --查询到的数据可以直接进行运算
  SELECT ename ,sal ,sal * 12 FROM emp;
  SELECT ename ,sal, comm ,(sal+comm) * 12 FROM emp;
  ```




## 3. SQL-DML









## 4. SQL-DDL



