DROP TABLE IF EXISTS details;
CREATE TABLE IF NOT EXISTS details(
	cust_name varchar(50),
    cust_city varchar(50),
    cust_country varchar(50),
    cust_grade decimal(10, 0)
);

DROP PROCEDURE IF EXISTS get_details;

DELIMITER &&
CREATE PROCEDURE get_details() 
BEGIN
	DECLARE var_stop INT DEFAULT 0;
    DECLARE c_name, c_city, c_country varchar(50);
    DECLARE c_grade decimal(10, 0);
    
    DECLARE curs CURSOR FOR
    SELECT DISTINCT CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE FROM customer WHERE AGENT_CODE LIKE "A00%";
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET var_stop=1;
    OPEN curs;
    label : LOOP
    FETCH curs INTO c_name, c_city, c_country, c_grade;
    IF var_stop=1 THEN 
    LEAVE label;
    END IF;
    INSERT INTO details VALUES(c_name, c_city, c_country, c_grade);
    END LOOP;
    CLOSE curs;
END &&
DELIMITER ;

CALL get_details();
SELECT *  FROM details;
