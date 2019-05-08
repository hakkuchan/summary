# 关键字 IS NULL
# 案例1：查询没有奖金的员工名的工资和奖金率
SELECT
	first_name,
	salary,
	commission_pct 
FROM
	employees 
WHERE
	commission_pct IS NULL
	
	
# 关键字 IS NOT NULL
# 案例2：查询有奖金的员工名的工资和奖金率
SELECT
	first_name,
	salary,
	commission_pct 
FROM
	employees 
WHERE
	commission_pct IS NOT NULL