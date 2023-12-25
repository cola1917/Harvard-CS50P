# FakeBTC
### Video Demo:  [FakeBTC](<https://youtu.be/AITy2HabTQ0>)
#### Description: This is a fake BTC trading platform based on the command line, You can view the overview as well as buy btc, all the data is persistent, stored in the database, and there are two ways to export the data, a csv file for analysis and a pdf file for printing with a Christmas CS50 duck as a background

#### Author Info

+ `name` : jiangtao wang
+ `id`: cola1917 (edx github)
+ `country`: China
+ `city`: BeiJing

#### Tech stack used:

- `python`

#### How to use

+ Use the command to start: `python project.py`,  The app will then print the welcome message along with today's BTC price, And you can see the four options of the main menu, `Overview`, `Transactions`, `Data Export`, `Exit`. type number `1-4`  to choose one option.
	+ `1`, `Overview` This feature will output all your assets, such as how much BTC you have, and how much they are worth
	+ `2`, `Transactions` This feature can be used to purchase BTC, you can buy one or more, or even 0.5 of them
	+ `3`, `Data Export` This function can export all order data, and in order to facilitate data analysis or printing, it provides two export methods: CSV file and PDF file
	+ `4`, `Exit` Exit the program

#### Project Structure Description

+ `CS50P-DUCK.png` The background image of the PDF file when it is exported
+ `fakebtc.db` A database where all transactions are stored. Use `sqlite3` as the database, only have one table `record` in this database, There are four fields :
	+ `id`, The `primary key` field is `self-incrementing` and `non-empty`
	+ `time`, The time field `text` type is `not empty`
	+ `price`,  The price field `REAL` type is `not empty`
	+ `amount`, The amount field `REAL` type is `not empty`
+ `project.py`
	+ `transactionHistorys` This is the main list of data, which is initialized when the project is running and maintained when new transactions are added
	+ `main` The entry function of the project
	+ `run` The most important functions of the project, control the running logic of the project, output menus at various levels, print prompts, etc
	+ `show_hello` Use the `Figlet` library to personalize the output greeting message,
	+ `get_btc_price` Use the Requests library to send a `request` to the target API and process the data to return today's `BTC` price
	+ `purchase` Purchase interfaces, respond to different amounts of demand, and write to the database
	+ `parser` Format the required data before performing database and data list operations
	+ `overview` The interface of the overview function returns the account holding information, how much BTC was purchased before the cost, and the current price
	+ `data_to_csv` In the Export Data API, export all data to a `CSV` file, and the file name is named after operation time + `data`
	+ `data_to_pdf` In the Export Data API, export all data to a `PDF` file, and the file name is named after operation time + `data`
	+ `write_to_db` Database write functions, format `SQL` statements, and write directly to the database
	+ `formal_to_record` At the beginning of the project, all the information found in the database is formatted into the data structure used by the project
+ `requirements.txt` Dependency information for the project, Only the dependency names are listed here. View the specific version file
	+ `fonttools`
	+ `fpdf2`
	+ `pyfiglet`
	+ `requests`
	+ `pytest`
+ `test_project.py`, The test file of the project, which tests some functions in the project, including:
	+ `purchase`
	+ `parser`
	+ `overview`
+ `util.py`, The project's tool file contains two utility classes: `SQL` and `PDF`
