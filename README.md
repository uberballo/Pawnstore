# Pawnstore  
Pawnstore project. User can lend and borrow items. At the beginning any cash transactions aren't required.

[Pawnstore heroku link](https://pawnstore.herokuapp.com/)  
[User stories](https://github.com/uberballo/Pawnstore/blob/master/documentation/userStories.md)  
[Database chart](https://github.com/uberballo/Pawnstore/blob/master/documentation/databaseChart.png) 

## How to install
* Make sure to have the latest verison of Python 3, SQLite 3 and pip.
* Unzip the program folder if needed and make it your current working directory.
* Make virtual environment with `python3 -m venv venv`
* Add the new environment as your source with `source venv/bin/activate`
* Install required libraries with the command `python3 -m install -r requirements.txt`
* Run the application with `python3 run.py`
* Now the application should be running at `localhost:5000`

## How to use
At first you should make a account, so you can fully utilize the application
* From the sidebar choose `create a user` and fill the form. This will instantly create your account.
Now you may add items or borrow them. As the items owner, you may delete them.
* To add items, choose `Add a item` and fill the form. Fill the items name, what category it belongs to and if it is available. It will instantly show on the list
* To browse items, choose `Items`. Here you can browse the items, borrow and delete them. If the item is available, you may borrow it. If you're the items owner, you may delete it.
