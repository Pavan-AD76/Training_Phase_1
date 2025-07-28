CREATE database hr_database;
USE hr_database;
CREATE TABLE employees (id INT PRIMARY KEY,name VARCHAR(100),department VARCHAR(100),salary DECIMAL(10, 2));
INSERT INTO employees (id, name, department, salary) VALUES(1, 'Alice', 'Engineering', 75000),(2, 'Bob', 'Marketing', 65000),(3, 'Charlie', 'Engineering', 80000),(4, 'Diana', 'HR', 60000),(5, 'Evan', NULL, 55000);
SELECT * from employees;

CREATE TABLE departments (department_id INT PRIMARY KEY,department_name VARCHAR(100));
INSERT INTO departments (department_id, department_name) VALUES(1, 'Engineering'),(2, 'HR'),(3, 'Sales');
SELECT * FROM departments;

# inner join
SELECT e.id,e.name,e.department,e.salary,d.department_name from employees as e inner join departments as d on e.department=d.department_name;

# Left join
SELECT e.id,e.name,e.department,e.salary,d.department_name from employees as e left join departments as d on e.department=d.department_name;

# Right Join
SELECT e.id,e.name,e.department,e.salary,d.department_name from employees as e right join departments as d on e.department=d.department_name;

# Full Outer Join
SELECT e.id, e.name, e.department, e.salary, d.department_name FROM employees e LEFT JOIN departments d ON e.department = d.department_name
UNION
SELECT e.id, e.name, e.department, e.salary, d.department_name FROM employees e RIGHT JOIN departments d ON e.department = d.department_name;


