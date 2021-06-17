# MySQL 基础

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
