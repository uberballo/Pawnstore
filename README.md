# Pawnstore  
Pawnstore project. User can lend and borrow items. You may browse items available, but to borrow, you need to make your own account. After making your account, you may add items and borrow items. When you're done using the borrowed item, Admins need to check the items quality, then may return the item to circulation or to remove the item from the list. 

[User stories](https://github.com/uberballo/Pawnstore/blob/master/documentation/userStories.md)  
[Database chart and CREATE TABLE-statements](https://github.com/uberballo/Pawnstore/blob/master/documentation/databaseChartsAndCreateTableStatements.md) 

## How to install
* Make sure to have the latest verison of Python 3, python3-venv, SQLite 3 and pip. 
* Unzip the program folder if needed and make it your current working directory.
* Make virtual environment with  
`python3 -m venv venv`  
* Add the new environment as your source with  
`source venv/bin/activate`  
* Install required libraries with the command  
`pip install -r requirements.txt`  
* Run the application with  
`python3 run.py`  
* Now the application should be running at  
`localhost:5000`  

## How to install on Heroku  
* First install the program locally, following the "How to install" part.
* Go to the folder where you've installed the program  
`cd FOLDER\WHERE_INSTALLED`
* Make a new app on Heroku. You may name it as whatever you want, as long as it is all **lowercase**
`heroku create NAME_HERE`
* Now if you want to use PostgreSQL, which allows the program to store data, use  
`heroku config:set HEROKU=1`  
`heroku addons:add heroku-postgresql:hobby-dev` 


## How to use
At first you should make a account, so you can fully utilize the application
* From the sidebar choose `Create a user` and fill the form. This will instantly create your account.
Now you may add items or borrow them. As the items owner, you may delete them.
* To add items, choose `Add a item` and fill the form. Fill the items name, what category it belongs to and if it is available. It will instantly show on the list
* To browse items, choose `Items`. Here you can browse the items, borrow and delete them. If the item is available, you may borrow it. If you're the items owner, you may delete it.
* To return borrowed item, you need to let the admins to check the borrowed item, then they will accept the item back. This is to ensure that items borrowed stay in good shape.
* Admins may choose new admins, thus allowing more volunteers to accept items back.


## Test accounts
Admin account credentials are:  
        
        Username: admin
        Password: admin

If you download the code and install it locally, you have to either manually insert admin accounts or for testing purposes, disable comments from the insert_admin()-function found in \_init\_ file, located in application folder.
