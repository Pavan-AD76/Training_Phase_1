CREATE database hr;
USE hr;
CREATE TABLE employees (id INT PRIMARY KEY,name VARCHAR(100),department VARCHAR(100),salary DECIMAL(10, 2));
INSERT INTO employees (id, name, department, salary) VALUES(1, 'Alice', 'Engineering', 75000),(2, 'Bob', 'Marketing', 65000),(3, 'Charlie', 'Engineering', 80000),(4, 'Diana', 'HR', 60000),(5, 'Evan', NULL, 55000),(6, 'Fiona', 'Sales', 50000),(7, 'George', 'Sales', 48000);
SELECT * from employees;
SELECT department, AVG(salary) AS avg_salary FROM employees WHERE department = 'Engineering'GROUP BY department;
SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department HAVING AVG(salary) > 60000;
