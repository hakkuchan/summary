# 案例：查询员工编号在100到120之间的员工信息
SELECT
	* 
FROM
	employees 
WHERE
	employee_id BETWEEN 100 AND 120;

/* 

包含100和120

注意大小顺序，不可写成 between 120 and 100

*/

