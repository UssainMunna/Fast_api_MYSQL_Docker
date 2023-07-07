Create Database bse_table;
use bse_table;

CREATE TABLE IF NOT EXISTS `bse_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deal_date` timestamp NULL DEFAULT NULL,
  `security_code` varchar(45) DEFAULT NULL,
  `security_name` varchar(45) DEFAULT NULL,
  `client_name` varchar(45) DEFAULT NULL,
  `deal_type` varchar(10) DEFAULT NULL,
  `quantity` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

LOCK TABLES `bse_info` WRITE;
INSERT INTO `bse_info` (id,security_code,security_name,client_name,deal_type,quantity,price) VALUES (1,'542580','AARTECH','VEENA RAJESH SHAH','s','132,000','111.30');
UNLOCK TABLES;