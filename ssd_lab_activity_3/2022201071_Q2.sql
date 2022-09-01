SELECT EMPLOYEE.Fname, EMPLOYEE.Minit, EMPLOYEE.Lname, EMPLOYEE.Ssn, EMPLOYEE.Dno, subquery.Num FROM 
EMPLOYEE INNER JOIN (SELECT Super_ssn, COUNT(*) AS Num FROM EMPLOYEE GROUP BY Super_ssn) subquery 
ON EMPLOYEE.Ssn=subquery.Super_ssn ORDER BY subquery.Num;