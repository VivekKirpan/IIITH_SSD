DROP PROCEDURE IF EXISTS addition;
DELIMITER //
CREATE PROCEDURE addition (IN num1 INT, num2 INT, OUT sum INT)
BEGIN
SELECT (num1 + num2) INTO sum;
END //
DELIMITER ;

CALL addition(3, 5, @sum);
SELECT @sum;