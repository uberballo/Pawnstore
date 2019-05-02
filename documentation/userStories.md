## user stories
|as a... | I want | so that
|-|-|-
|user | add a item | I can lend it
|user | remove a item | I don't have to borrow it anymore
|user | borrow a item | I can use the item
|moderator | Give admin privilege | Make more admins, thus easier to monitor items
|moderador | Check in item | We can ensure the returned item is in acceptable condition  
## SQL queries
### Inserting a new user
	INSERT INTO account (date_created, date_modified, name, username, password, role) 
	       VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

### Changing user role
	UPDATE account SET date_modified=CURRENT_TIMESTAMP, role=? WHERE account.id = ?;

### Inserting a new item
	INSERT INTO item (date_created, date_modified, name, available, account_id, category_id, borrowed, borrowed_by_id) 
		VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)

### Updating items availability
	UPDATE item SET date_modified=CURRENT_TIMESTAMP, available=?, borrowed=?, borrowed_by_id=? WHERE item.id = ?;

### Deleting a item
	DELETE FROM item WHERE item.id = ?;

### Counting items in category
	SELECT COUNT(Item.id), Category.category_type
	       FROM Item
	       LEFT JOIN Category ON Item.category_id = Category.id
	       GROUP BY Category.category_type
	       ORDER BY COUNT(Item.id) DESC;
### Removing user
	DELETE FROM Item WHERE Item.account_id = ?;
	DELETE FROM Account WHERE account.id = ?;
