## DATABASE SCHEMA FOR FLASKAPP

#### CUSTOMERS                      
| KEY              | COLUMN NAME         | TYPE         |                     
| :------------    | :-------------------| :----------- |
| PRIMARY_KEY      | Customer_ID         | VARCHAR(32)  |
|                  | Name                | VARCHAR(32)  |
|                  | Age                 | TINYINT      |
|FOREIGN_KEY(Cars) | Car_Reg_Num         | VARCHAR(32)  |
|                  | Bill                | INT          |

#### CARS
| KEY                   | COLUMN NAME         | TYPE         |
|:------------          |:--------------------|:------------ |
| PRIMARY_KEY           | Car_Reg_num         | VARCHAR(32)  |
|                       | Color               | VARCHAR(32)  |
|                       | Manufacturer        | TINYINT      |
|FOREIGN_KEY (Customers) | Owner               | VARCHAR(32)  |
|                       | Model_name          | VARCHAR(32)  |

#### PARKING_SLOTS
| KEY                 |COLUMN NAME       | TYPE         |
|:--------------------|:-----------------|:-------------|
| PRIMARY_KEY         | Serial_num       | VARCHAR(32)  |
|                     | Occupied         | BOOLEAN      |
| FOREIGN_KEY (Cars)  | Car_reg_num      | VARCHAR      |
|                     | Parking_date_time| DATETIME     |