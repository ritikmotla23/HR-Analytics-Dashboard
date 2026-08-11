SELECT COUNT(*) AS TotalEmployees
FROM employees;
SELECT
    COUNT(*) AS EmployeesLeft
FROM employees
WHERE Attrition = 'Yes';
SELECT
    ROUND(
        100.0 * SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS AttritionRate
FROM employees;
SELECT
    ROUND(AVG(MonthlySalary), 2) AS AverageSalary
FROM employees;
SELECT
    ROUND(AVG(AttendanceRate), 2) AS AverageAttendance
FROM employees;
SELECT
    ROUND(AVG(PerformanceScore), 2) AS AveragePerformance
FROM employees;
SELECT
    Department,
    COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Department
ORDER BY EmployeeCount DESC;
SELECT
    Department,
    COUNT(*) AS TotalEmployees,

    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS EmployeesLeft,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS AttritionRate

FROM employees

GROUP BY Department
ORDER BY AttritionRate DESC;
SELECT
    Department,
    ROUND(AVG(MonthlySalary), 2) AS AverageSalary
FROM employees
GROUP BY Department
ORDER BY AverageSalary DESC;
SELECT
    PerformanceScore,
    COUNT(*) AS EmployeeCount,
    ROUND(AVG(MonthlySalary), 2) AS AverageSalary,
    ROUND(AVG(AttendanceRate), 2) AS AverageAttendance
FROM employees
GROUP BY PerformanceScore
ORDER BY PerformanceScore;
SELECT
    Overtime,
    COUNT(*) AS TotalEmployees,

    SUM(
        CASE
            WHEN Attrition = 'Yes' THEN 1
            ELSE 0
        END
    ) AS EmployeesLeft,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN Attrition = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS AttritionRate

FROM employees

GROUP BY Overtime;
