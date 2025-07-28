CREATE database Employee_detail;
USE Employee_detail;
CREATE TABLE employees (id INT PRIMARY KEY,name VARCHAR(100),department VARCHAR(100),salary DECIMAL(10, 2));
INSERT INTO employees (id, name, department, salary) VALUES (1, 'Alice', 'Engineering', 75000), (2, 'Bob', 'Marketing', 65000),(3, 'Charlie', 'Engineering', 80000);
SELECT * from employees;
UPDATE employees SET salary=70000 where name='Bob';
SELECT * FROM employees WHERE department="Engineering";
DELETE  FROM employees WHERE id=3;
ALTER TABLE employees ADD COLUMN appraisal_percentage DECIMAL(10, 2);
