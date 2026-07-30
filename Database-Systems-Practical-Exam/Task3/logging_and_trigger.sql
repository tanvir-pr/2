-- Task 3: Logging Table and Salarylog Trigger

-- Step 1: Create the logging table
CREATE TABLE logging (
    employee_id   NUMBER,
    last_name     VARCHAR2(50),
    change_date   DATE,
    new_salary    NUMBER
);

-- Step 2: Create the trigger
CREATE OR REPLACE TRIGGER salarylog
AFTER UPDATE OF salary ON employees
FOR EACH ROW
BEGIN
    INSERT INTO logging (employee_id, last_name, change_date, new_salary)
    VALUES (
        :NEW.employee_id,
        :NEW.last_name,
        SYSDATE,
        :NEW.salary
    );
END;
/
