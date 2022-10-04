USE flaskapp;

CREATE TABLE Vehicles (
	Reg_Num varchar(32) NOT NULL, 
    Owner_ID INT NOT NULL, 
    Model_name varchar(32),
    Color varchar(32), 
    V_Type varchar(32) CHECK (V_Type in ('LMV', 'MCWG', 'HMV')),
    Entry_time DATETIME NOT NULL,
    PRIMARY KEY (Reg_Num) 
);

CREATE TABLE Customers (
	Name varchar(32) NOT NULL,
    Customer_ID INT NOT NULL,
    Age TINYINT NOT NULL,
    Bill_Amount INT,
    PRIMARY KEY (Customer_ID)
);

ALTER TABLE Vehicles
ADD FOREIGN KEY (Owner_ID) REFERENCES Customers(Customer_ID);



