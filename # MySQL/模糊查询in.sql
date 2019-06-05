# 案例：查询员工的工种编号是 IT_PROG 或 AD_VP 或 AD_PRES 中的员工信息
SELECT
	* 
FROM
	employees 
WHERE
	job_id IN ( 'IT_PROG', 'AD_VP', 'AD_PRES' )