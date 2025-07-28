use hr_database;
CREATE TABLE department_stats (department VARCHAR(100) PRIMARY KEY,avg_salary DECIMAL(10, 2));
DELIMITER //

CREATE PROCEDURE CalculateAvgSalary(IN dept_name VARCHAR(100))
BEGIN
    DECLARE avg_sal DECIMAL(10,2);

    SELECT AVG(salary)
    INTO avg_sal
    FROM employees
    WHERE department = dept_name;

    INSERT INTO department_stats (department, avg_salary)
    VALUES (dept_name, avg_sal)
    ON DUPLICATE KEY UPDATE avg_salary = avg_sal;

END //

DELIMITER ;
CALL CalculateAvgSalary('Engineering');
SELECT * FROM department_stats;
