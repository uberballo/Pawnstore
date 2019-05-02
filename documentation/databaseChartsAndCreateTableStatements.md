## Database chart 
<img src="https://github.com/uberballo/Pawnstore/blob/master/documentation/databaseChart.png">  

## CREATE TABLE- statements
### User
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

### Item
CREATE TABLE item (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	available BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	borrowed BOOLEAN, 
	borrowed_by_id INTEGER, 
	PRIMARY KEY (id), 
	CHECK (available IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(category_id) REFERENCES category (id), 
	CHECK (borrowed IN (0, 1))
);

### Category
CREATE TABLE category (
	id INTEGER NOT NULL, 
	category_type VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
