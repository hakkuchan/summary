#二、分组函数

#1、简单 的使用
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;
SELECT COUNT(salary) FROM employees; # salary is not full 的个数

SELECT
	SUM( salary ) 和,
	AVG( salary ) 平均,
	MAX( salary ) 最高,
	MIN( salary ) 最低,
	COUNT( salary ) 个数 
FROM
	employees;
	
SELECT
	SUM( salary ) 和,
	ROUND( AVG( salary ), 2 ) 平均,
	MAX( salary ) 最高,
	MIN( salary ) 最低,
	COUNT( salary ) 个数 
FROM
	employees;

#2、参数支持哪些类型
SELECT SUM(last_name) ,AVG(last_name) FROM employees;
SELECT SUM(hiredate) ,AVG(hiredate) FROM employees;
SELECT MAX(last_name),MIN(last_name) FROM employees;
SELECT MAX(hiredate),MIN(hiredate) FROM employees;
SELECT COUNT(commission_pct) FROM employees;
SELECT COUNT(last_name) FROM employees;

#3、是否忽略null（答案：不参与）
SELECT
	SUM( commission_pct ),
	AVG( commission_pct ),
	SUM( commission_pct ) / 35,
	SUM( commission_pct ) / 107 
FROM
	employees;

SELECT MAX(commission_pct) ,MIN(commission_pct) FROM employees;
SELECT COUNT(commission_pct) FROM employees;
SELECT commission_pct FROM employees;


#4、和distinct搭配
SELECT SUM(DISTINCT salary),SUM(salary) FROM employees;
SELECT COUNT(DISTINCT salary),COUNT(salary) FROM employees;



#5、count函数的详细介绍
SELECT COUNT(salary) FROM employees;
SELECT COUNT(*) FROM employees;

#6、和分组函数一同查询的字段有限制
SELECT AVG(salary),employee_id  FROM employees; #avg是一个值，employee_id是一列表
