-- Task 2: Stored Function NumberValues
-- Takes a position name (job_title) and a date as input.
-- Returns -1 if the position does not exist in the jobs table.
-- Otherwise returns the count of employees currently in that position
-- who also worked in other positions before the specified date.

CREATE OR REPLACE FUNCTION NumberValues(
    p_job_title IN jobs.job_title%TYPE,
    p_date IN DATE
) RETURN NUMBER IS
    v_job_id jobs.job_id%TYPE;
    v_count NUMBER;
BEGIN
    BEGIN
        SELECT job_id INTO v_job_id
        FROM jobs
        WHERE job_title = p_job_title;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RETURN -1;
    END;

    SELECT COUNT(*) INTO v_count
    FROM employees e
    WHERE e.job_id = v_job_id
      AND EXISTS (
          SELECT 1
          FROM job_history jh
          WHERE jh.employee_id = e.employee_id
            AND jh.job_id != v_job_id
            AND jh.start_date < p_date
      );

    RETURN v_count;
END;
/
