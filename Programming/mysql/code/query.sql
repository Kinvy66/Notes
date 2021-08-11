# 基础查询
/*
语法：
selec 查询列表 from 表名;

特点：
1. 查询列表可以使： 表中的字段、常量值，表达式
2. 查询的结果是一个虚拟的表发
*/

use scott;

# 1. 查询表中的单字段

select last_name from employees;

#2. 查询表中的多个字段
select last_name,salary,email from employees;

#3. 查询表中的所有字段
select * from employees;

#4. 查询常量值
select 100;


#5. 起别名
# 方式1
select 100%98 as 结果;
select last_name as 姓, first_name as 名 from employees;

# 方式2
#select last_name  姓, first_name  名 from employees;

#案例  查询salary，显示结果为 out put
#select salary as 'out put'  from employees;


# 6. 去重

# 案例
select DISTINCT department_id from employees;
 

 #7. + 号的作用, mysql的+只有一个功能：运算符
/*
select 100+90;  两个操作数都为数值型，则做加法运算
select '123'+90;    只有其中一方为字符型，识图将字符型数值转换成数值型
                    如果转换成功，则继续做加法运算
                    如果转换失败，则将字符型数值转换成0

select null+10;  只要其中一方为null,则结果肯定为null
*/

 #案例 ： 查询员工名和姓连接成一个字段，并显示为 姓名

 select concat('a','b','c') as 结果;   # 将a,b,c连接起来
 select concat('last_name','first_name') as 姓名  from employees;




#显示表的结构
desc departments;
select * from departments; 





 
