# 排序查询
/* 语法：
SELECT 内容
FROM 表
【WHERE 筛选条件】
ORDER BY 排序列表 【ASC|DESC】
*/

# 示例1：查询员工信息，要求工资从高到低排序
SELECT
	* 
FROM
	employees 
ORDER BY
	salary DESC;


# 示例2：查询部门编号大于等于90的员工信息，按入职时间先后排序
SELECT
	* 
FROM
	employees 
WHERE
	department_id >= 90 
ORDER BY
	hiredate;


# 示例3：按年薪高低显示员工信息和年薪
SELECT
	first_name,
	salary * 12 * ( 1+IFNULL ( commission_pct, 0 ) ) 
FROM
	employees 
ORDER BY
	salary * 12 * ( 1+IFNULL ( commission_pct, 0 ) ) DESC;
	
	
# 案例4：按年薪高低显示员工信息和年薪（别名）
SELECT
	first_name,
	salary * 12 * ( 1+IFNULL ( commission_pct, 0 ) ) AS 年薪 
FROM
	employees 
ORDER BY
	年薪 DESC;

# 案例5：按照姓名长度显示姓名和工资【按函数排序】
SELECT
	LENGTH( last_name ) AS 字节长度,
	last_name,
	salary 
FROM
	employees 
ORDER BY
	LENGTH( last_name ) DESC;

# 示例6：查询员工信息，先按工资排序，再按员工编号排序
SELECT
	* 
FROM
	employees 
ORDER BY
	salary ASC,
	employee_id DESC;