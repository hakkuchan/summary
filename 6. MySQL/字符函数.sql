#一、字符函数

#1.length 获取参数值的字节个数
SELECT LENGTH('john');
SELECT LENGTH('张三丰hahaha');

#2.concat 拼接字符串

SELECT CONCAT(last_name,'_',first_name) 姓名 FROM employees;

#3.upper、lower
SELECT UPPER('john');
SELECT LOWER('joHn');
#示例：将姓变大写，名变小写，然后拼接
SELECT CONCAT(UPPER(last_name),' ',LOWER(first_name))  姓名 FROM employees;

#4.substr、substring
注意：索引从1开始
#截取从指定索引处后面所有字符
SELECT SUBSTR('李莫愁爱上了陆展元',7) AS out_put; # SQL语言索引从1开始
#截取从指定索引处指定字符长度的字符
SELECT SUBSTR('李莫愁爱上了陆展元',1,3) AS out_put;
#案例：姓名中首字符大写，其他字符小写然后用_拼接，显示出来
SELECT
	CONCAT( UPPER( SUBSTR( last_name, 1, 1 ) ), LOWER( SUBSTR( last_name, 2 ) ) ) AS out_put 
FROM
	employees;

#5.instr 返回子串第一次出现的索引，如果找不到返回0
SELECT INSTR('杨不殷六侠悔爱上了殷六侠','殷六侠') AS out_put;

#6.trim
SELECT TRIM('a' FROM 'aaaaaaaaa张aaa翠山aaa')  AS out_put;

#7.lpad 用指定的字符实现左填充指定长度
SELECT LPAD('殷素素',10,'*') AS out_put;

#8.rpad 用指定的字符实现右填充指定长度
SELECT RPAD('殷素素',12,'a') AS out_put;

#9.replace 替换
SELECT REPLACE('张无忌爱上了周芷若','周芷若','赵敏') AS out_put;  