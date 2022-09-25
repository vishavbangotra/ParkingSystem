##DATABASE SCHEMA FOR FLASKAPP

####Customers

| KEY |COLUMN NAME   |TYPE  |
| ------------ | ------------ |
| PRIMARY_KEY | Customer_ID  | VARCHAR(32)  |
|  |  Name  | VARCHAR(32)  |
|  | Age | TINYINT |
| FOREIGN_KEY (Cars) | Car_Reg_Num | VARCHAR(32)
|  | Bill | INT

####Cars

| KEY |COLUMN NAME   |TYPE  |
| ------------ | ------------ |
| PRIMARY_KEY | Car_Reg_Num  | VARCHAR(32)  |
| | Colour | VARCHAR(32)  |
|  |  Model_name  | VARCHAR(32)  |
|  | Manufacturer | TINYINT |
| FOREIGN_KEY (Cars) | Car_reg_num | VARCHAR

####Parking slots

| KEY |COLUMN NAME   |TYPE  |
| ------------ | ------------ |
| PRIMARY_KEY | Serial_num  | VARCHAR(32)  |
| | Occupied | BOOLEAN  |
| FOREIGN_KEY (Cars) |  Car_details  | VARCHAR(32)  |
|  | Entry_time | TINYINT |