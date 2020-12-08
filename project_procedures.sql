USE `project`;
DROP procedure IF EXISTS `color_price`;

DELIMITER $$
USE `project`$$
CREATE PROCEDURE `color_price` (IN color varchar(50))
BEGIN
Select Color_price from Color Where Color_id = color;
END$$

DELIMITER ;

USE `project`;
DROP procedure IF EXISTS `car_choose_price`;

DELIMITER $$
USE `project`$$
CREATE PROCEDURE `car_choose_price` (IN mid varchar(6))
BEGIN
Select Price from Make Where Make_id = mid;

END$$

DELIMITER ;


USE `project`;
DROP procedure IF EXISTS `full_report`;

DELIMITER $$
USE `project`$$


CREATE PROCEDURE `full_report` ( IN bid int,
  OUT report_out varchar(500))
BEGIN
Declare cid, pri int default 0;
Declare modelname varchar(30);
Declare brandname varchar(10);
Select Cart_id into cid
From Buyer Join Cart 
Where Buyer.Cart_id = Cart.Cart_id and Buyer.Customer_id = bid;

Select Price into pri 
From Buyer Join Cart
Where Buyer.Cart_id = Cart.Cart_id and Buyer.Customer_id = bid;

Select Brand_name into brandname
From Buyer Natural join Cart Natural join Make natural join Vehicle_Brand
Where Buyer.Customer_id = bid;

Select Model_Shape into modelname
From Buyer natural join Cart natural join Make
Where Buyer.Customer_id = bid;

Set report_out = CONCAT("Buyer id: " + str(bid) + " Cart id: " + str(cid) + " Price: $" + str(pri) + " Brand: " + brandname + " Model: " + modelname);
END$$