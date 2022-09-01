DROP PROCEDURE IF EXISTS cust_city;

DELIMITER &&
CREATE PROCEDURE cust_city (IN city varchar(35))
BEGIN
	SELECT CUST_NAME FROM customer WHERE WORKING_AREA = city;
END &&
DELIMITER ;

CALL cust_city("Bangalore");
