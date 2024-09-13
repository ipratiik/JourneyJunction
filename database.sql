-- Create database train
CREATE DATABASE train;

-- Use database train
Use train;

-- Create table passenger_details
CREATE TABLE `passenger_detail` (
  `name` varchar(40) NOT NULL,
  `age` int NOT NULL,
  `CNIC` bigint NOT NULL,
  `date` date NOT NULL,
  `booking_class` varchar(40) NOT NULL,
  `departure` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `destination` varchar(40) NOT NULL,
  `ticket_id` int NOT NULL AUTO_INCREMENT,
  `timing` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `fare` int NOT NULL,
  PRIMARY KEY (`ticket_id`)
);

-- Create table accounts
CREATE TABLE `accounts` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `First_Name` char(10) NOT NULL,
  `Last_Name` char(10) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Password` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`)
)