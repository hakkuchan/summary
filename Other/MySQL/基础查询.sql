# 基础查询

/* 
语法：
SELECT
	内容 
FROM
	表名;
*/

# 查询表中单个字段
SELECT
	last_name 
FROM
	employees;

# 查询表中多个字段
SELECT
	first_name,
	salary,
	email 
FROM
	employees;

# 查询表中所有字段
SELECT
	* 
FROM
	employees;

# 查询常量值
SELECT
	100;
SELECT
	'john';

# 查询表达式
SELECT
	100 % 98;

# 查询函数
SELECT
	VERSION( );

# 字段起别名
/*
目的：
(1) 便于理解
(2) 使用别名区分重名字段
*/

SELECT
	last_name AS 姓,
	first_name AS 名 
FROM
	employees;
	
# 也可以省略 AS
SELECT
	last_name 姓,
	first_name 名 
FROM
	employees;

# 别名中存在关键字时，用双引号把别名引出
SELECT
	salary AS "out put" 
FROM
	employees;

# 去重
SELECT DISTINCT
	department_id 
FROM
	employees;

# 拼接
SELECT
	CONCAT( first_name, last_name ) AS 姓名 
FROM
	employees;
	
# 在拼接中增加字符
SELECT
	concat( first_name, ', ', last_name ) AS 'out_put' 
FROM
	employees;