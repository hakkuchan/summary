#五、流程控制函数

#1.if函数： if else 的效果

SELECT IF(10<5,'大','小');

SELECT last_name, commission_pct,
IF ( commission_pct IS NULL, '没奖金，呵呵', '有奖金，嘻嘻' ) 备注 
FROM employees;




#2.case函数的使用一： switch case 的效果

/*
语法：

case 要判断的字段或表达式
when 常量1 then 要显示的值1或语句1;
when 常量2 then 要显示的值2或语句2;
...
else 要显示的值n或语句n;
end
*/

/*案例：查询员工的工资，要求

部门号=30，显示的工资为1.1倍
部门号=40，显示的工资为1.2倍
部门号=50，显示的工资为1.3倍
其他部门，显示的工资为原工资

*/


SELECT
	salary AS 原始工资,
	department_id,
CASE
		department_id 
		WHEN 30 THEN
		salary * 1.1 
		WHEN 40 THEN
		salary * 1.2 
		WHEN 50 THEN
		salary * 1.3 ELSE salary 
	END AS 新工资 
FROM
	employees;



#3.case 函数的使用二：类似于 多重if
/*

语法：

case 
when 条件1 then 要显示的值1或语句1
when 条件2 then 要显示的值2或语句2
……
else 要显示的值n或语句n
end
*/

#案例：查询员工的工资的情况
#如果工资>20000,显示A级别
#如果工资>15000,显示B级别
#如果工资>10000，显示C级别
#否则，显示D级别


SELECT salary,
CASE 
WHEN salary>20000 THEN 'A'
WHEN salary>15000 THEN 'B'
WHEN salary>10000 THEN 'C'
ELSE 'D'
END AS 工资级别
FROM employees;