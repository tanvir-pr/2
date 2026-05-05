-- Testing Task 3: Salarylog Trigger

-- Test 1: Update salary of employee 100
UPDATE employees
SET salary = 30000
WHERE employee_id = 100;

-- Test 2: Update salary of employee 101
UPDATE employees
SET salary = 22000
WHERE employee_id = 101;

-- Test 3: Update salary of employee 102
UPDATE employees
SET salary = 12000
WHERE employee_id = 102;

COMMIT;

-- Verify: Check the logging table
SELECT * FROM logging;
