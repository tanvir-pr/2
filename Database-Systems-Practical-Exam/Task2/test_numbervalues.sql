-- Testing Task 2: NumberValues Function

SET SERVEROUTPUT ON;

DECLARE
    v_result NUMBER;
BEGIN
    -- Test 1: Non-existent position (should return -1)
    v_result := NumberValues('Nonexistent Position', SYSDATE);
    DBMS_OUTPUT.PUT_LINE('Non-existent position: ' || v_result);

    -- Test 2: Public Accountant with first date
    v_result := NumberValues('Public Accountant', TO_DATE('2005-01-01', 'YYYY-MM-DD'));
    DBMS_OUTPUT.PUT_LINE('Public Accountant (2005-01-01): ' || v_result);

    -- Test 3: Public Accountant with second date
    v_result := NumberValues('Public Accountant', TO_DATE('2010-01-01', 'YYYY-MM-DD'));
    DBMS_OUTPUT.PUT_LINE('Public Accountant (2010-01-01): ' || v_result);
END;
/
