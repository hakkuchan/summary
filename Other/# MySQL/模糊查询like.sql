# 模糊查询
# 关键字：like, between and, in, is null, is not null

/* 
关键字 like 
通常与3个关键符号：% _ \
配合使用
*/

# 示例1：查询员工姓中包含字符a的员工信息
# 通配符 % ：表示0-任意多的字符
SELECT
	* 
FROM
	employees 
WHERE
	last_name LIKE '%a%';
	
# 示例2：查询员工姓中第3个字符为n,第5个字符为l的员工信息
# 通配符 _ ：任意单个字符
SELECT
	* 
FROM
	employees 
WHERE
	last_name LIKE '__n_l%';
	
# 示例3：查询员工姓中包含 _ 的员工信息
# \ 转义符：任意单个字符
SELECT
	* 
FROM
	employees 
WHERE
	last_name LIKE '%\_%';
	
# 另一种写法：
SELECT
	* 
FROM
	employees 
WHERE
	last_name LIKE '%$_%' ESCAPE '$'; 
# 其中，$ 可以用其它字符代替

