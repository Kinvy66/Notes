# Mysql 重置root用户密码

环境： ubuntu18，mysql-8， 忘记root用户的密码情况下进入mysql重置root用户





## 修改root用户密码



### 1. 更改配置文件

```shell
$ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

打开这个文件后，在最后添加

```shell
skip-grant-tables　
```



### 2. 重启mysql

```shell
$ sudo service mysql restart
```



### 3. 连接mysql修改数据库的root用户密码

```shell
$ mysql
```

mysql操作

```sql
use mysql;		#进入名为mysql的数据库
select User, Host, authentication_string from user;  # 查看一下user表的内容
update user set authentication_string=password("你的新密码") where User='root';
flush privileges;  # 刷新权限，修改完成之后，需要使用该语句，重新加载权限表
exit;    #退出mysql
```

执行上面的sql语句退出后，记得把`/etc/mysql/mysql.conf.d/mysqld.cnf`  配置文件添加的内容删除



### 5. 重启mysql

```shell
$ service mysql restart
```

输入新密码正常登陆即可

```shell
$  mysql -u root -p
```



## 重新创建root用户

重新创建是指没有root用户，如果有需要先删除

同样需要修改mysql的配置文件，进入到mysql执行下面的sql语句

```sql
use mysql;		#进入名为mysql的数据库
select User, Host, authentication_string from user;  # 查看一下user表的内容
CREATE USER 'root'@'%' IDENTIFIED BY 'password';  #password 换成自定义的密码 
GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION; # 给root用户权限
```









 