# MySQL 基础



## 0.  MySQL安装

用压缩包的方式安装

[mysql下载](https://dev.mysql.com/downloads/mysql/)

将下载的安装包解压，例如： `C:\Env`

在解压的mysql文件夹下创建 `my.ini`文件，文件内容

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
default-character-set=utf8
```

添加环境变量



依次执行以下命令

```bash
mysqld --initialize-insecure
mysqld --defaults-file=C:\Env\mysql-8.0.25-winx64\my.ini --initialize –console
mysqld install
mysqld --initialize-insecure --user=mysql	
mysqladmin -u root -p password		#设置root用户密码，初始密码为空
mysql -u root -p					#登录测试
```







## MySQL的登录和退出

1. 登录和退出
> mysql 【-h主机名 -P端口号】-u用户名 -p密码

> exit  #

## MySQL的常见命令

```sql
show databases;     --显示所有的数据库
use test;           --打开test数据库
show tables;        --显示数据库的表
show tables from  mysql; --查看mysql库的表
select databases(); --查看当前所在的数据量
create table  tablename(id int, name varchar(20)); --创建表
desc tablename;     --显示表
select * from tablename; --查看表的数据
insert into tablename (id,name) values(1,'tom');    --插入数据
select version();   --查看数据库版本
```


## MySQL语法规范

1. 不区分大小写，但建议关键字大写，表名、列名小写
2. 每条命令最后用分号结尾
3. 每条命令根据需要，可以进行缩进或换行
4. 注释
    * 单行注释： #注释文字   --单行注释
    * 多行注释： /* 多行注释 */


## DQL 语言

## DML语言

## DDL语言

## TCL语言
