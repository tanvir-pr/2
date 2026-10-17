-- Testing Task 1: Goodwage Procedure

SET SERVEROUTPUT ON;

-- Test 1: Existing department with amount = 1000
EXEC Goodwage('IT', 1000);

-- Test 2: Existing department with different amount = 5000
EXEC Goodwage('IT', 5000);

-- Test 3: Non-existent department
EXEC Goodwage('Nonexistent Dept', 1000);
