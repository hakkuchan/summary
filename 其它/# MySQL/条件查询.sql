# 条件查询

/* 
语法：
SELECT 查询列表
FROM 表名
WHERE 筛选条件;
*/ 

# 方式一：按照条件表达式筛选
# 条件运算符: =, <>, >, <, >=, <=, <=>
# <=>:安全等于，可以判断是否等于普通值或NULL，不常用

# 示例1：查询工资大于12000的员工信息
SELECT
	* 
FROM
	employees 
WHERE
	salary > 12000;
	
# 示例2：查询部门编号不等于90号的员工名和部门编号
SELECT
	CONCAT( first_name, last_name ),
	department_id 
FROM
	employees 
WHERE
	department_id <> 90;


# 方式二：按照逻辑表达式筛选
# 逻辑运算符: &&, and, ||, or, !, not
# 作用：连接条件表达式

# 示例：工资在1000-2000之间的员工名，工资，奖金
SELECT
	CONCAT( first_name, last_name ),
	salary,
	commission_pct 
FROM
	employees 
WHERE
	salary >= 10000 AND salary <= 20000;