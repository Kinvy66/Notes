use myemployees;
#1. 显示出表employees的全部列，各个列之间用逗号连接，列头显示成OUT_PUT

select ifnull(commission_pct,0) as 奖金率,
        commission_pct
from
    employees;

# -------------------------------
select 
    concat('first_name',',','last_name',',','job_id',',',ifnull(commission_pct,0)) as out_put
from
    employees;



#-------------------------------------------------------------------

#2. 条件查询
/*
语法：
    select 
            查询列表
    from
            表名
    where
            筛选条件；
分类：
    一、 按条件表达式筛选
    条件运算符：> < = !=  <>  >=  <=
    二、 按逻辑表达式筛选
        &&   ||  ！

    三、 模糊查询
        like
        between  and
        in 
        is null
*/
# 一、按条件表达式筛选
#案例1： 查询工资 > 12000的员工信息
select 
        *
from
        employees
where 
        salary>12000;

#案例2： 查询部门编号不等于90号的员工名和部门编号
select
        last_name,
        department_id
from
        employees
where
        department_id <> 90;

# 二、 按逻辑表达式筛选
#案例1： 查询工资在10000到20000之间的员工名，工资以及奖金，
select
        last_name,
        salary,
        commission_pct
from
        employees
where
        salary >= 10000 and salary <= 20000;

# 案例2： 查询部门编号不是在90 到110之间，或者工资高于1500的员工信息
select
        *
from
        employees
where
        not(department_id>=90 and department_id <= 110) or salary > 15000;

#三、 模糊查询
/*
1. like
特点：
* 一般和通配符搭配使用
    通配符：
    % 任意多个字符，包含0个字符

        between  and
        in 
        is null
*/
#1. like
#案例1： 查询员工中包含字符a的员工信息
select
        *
from 
        employees
where
        last_name like '%a%';   #%表示通配符

#案例2：查询员工中第三个字符为e,第五个字符为a的员工名和工资
select 
        last_name,
        salary
from 
        employees
where
        last_name like '__n_1%';  #_  为通配符

#案例3：查询员工名中第二个字符为_的员工名
SELECT
        last_name
FROM
        employees
WHERE
        last_name LIKE  '_\_%';   



SELECT
        last_name
FROM
        employees
WHERE
        last_name LIKE  '_$_%' ESCAPE '$';   


#2. between and  
/*
包含临界值
临界值不要调换位置 (>= and <=)
*/
#案例1： 查询员工编号在100到120之间的员工信息
select

        *
from
        employees
where
        employee_id between 100 and 120;  

#3. in
/*
判断某字段的值是否属于in列表中的某一项
in列表的值类型必须一致或兼容


*/
#案例：查询员工的工种编号是 IT_PROG、AD_VP、AD_PRES中的一个员工名和工种编号
select
        last_name,
        job_id
from
        employees
where
        job_id in('IT_PROG','AD_VP','AD_PRES');

#4. is null
/*
*/
#案例1： 查询没有奖金的员工名和奖金率
select
        last_name,
        commission_pct
from
        employees
where
        commission_pct is null;  # is not null  表示有奖金的


#安全等于   <=>
#案例1： 查询没有奖金的员工名和奖金率
select
        last_name,
        commission_pct
from
        employees
where
        commission_pct <=> null;

#案例2： 查询工资为12000的员工信息
select
        last_name,
        salary     
from
        employees
where
        salary <=> 12000 ;