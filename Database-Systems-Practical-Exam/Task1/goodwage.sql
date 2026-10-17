-- Task 1: Stored Procedure Goodwage
-- Receives a department name and a number as input parameters.
-- Displays 'Non exist department!' if department doesn't exist.
-- Otherwise displays surname, phone number and salary of employees
-- whose salary differs from their job's max_salary by at most the specified number.

CREATE OR REPLACE PROCEDURE Goodwage(
    p_department_name IN departments.department_name%TYPE,
    p_number IN NUMBER
) IS
    v_dept_id departments.department_id%TYPE;
    v_exists NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_exists
    FROM departments
    WHERE department_name = p_department_name;

    IF v_exists = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Non exist department!');
        RETURN;
    END IF;

    SELECT department_id INTO v_dept_id
    FROM departments
    WHERE department_name = p_department_name;

    FOR rec IN (
        SELECT e.last_name, e.phone_number, e.salary
        FROM employees e
        JOIN jobs j ON e.job_id = j.job_id
        WHERE e.department_id = v_dept_id
          AND (j.max_salary - e.salary) <= p_number
    ) LOOP
        DBMS_OUTPUT.PUT_LINE(
            rec.last_name || ' | ' ||
            rec.phone_number || ' | ' ||
            rec.salary
        );
    END LOOP;
END;
/
