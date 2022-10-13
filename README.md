
# Banking Application
##  Aravind kumar

## OVER VIEW 

DATABASE :
I have created three tables in total, they are :
 -registration table - contains username,ph number ,adhar number ,address and password .
 -user cards table - has username ,card type ,card name ,card pin ,card CVV and card balance 
 - beneficiary table - has username and the beneficiary names .

CODE :
I have divided my code into different files to easily understand the code they are: 
1.home.py - which is the file we run to execute our entire code 
2.registration.py - which is used to register and these details are stored in database .
3.login.py - after registration is done we can login , that code is in this file 
4.carddetails.py - this file is used to enter card details and stores in database .
5.base.py - this stands as a back bone to the entire code , all various functions are here .
6.rough.py - I have used it as a playground to construct this banking application .


I have designed an application for a banking system 

- Major sections of my project
- Login 
- Registration
## Features

- Registration  - to register new users and store their data into registered table
- User Cards    - to save all the card details for a user 
- Account Information - to get all the account information 
- List Benificiary  - to list out all the benificaries for a user 
- List of cards  - to list out all the cards for a user 
- Add Benificiary  - to add benificiary 
- Register New Credit Card - to register a new credit card for a user
- Change Pin  - to change card pin 
- Update Information - to update information 
- Transfer Funds - to transfer funds from one user to another 
OVERVIEW : 
1.Once we register then we can login using the details given while registering
2.After entering the details then we can see various options available to us 
3.We can transfer funds , add new card details etc ..

## DESCRIPTION
- Step 1 : I have created users and added their info into registered table.
- Step 2 : I have created another table to store all data related to cards of users .
- Step 3 : After creating and adding card details , we can get info of a required user .
- Step 4 : We can see all the benificiaries and cards a specific user has .
- Step 5 : We can add new benificiaries and new card details for a user .
- Step 6 : We can change card pin for a req user ,card type ,card name .
- Step 7 : We can update  the user info.
- Step 8 : We can transfer funds from one account to another and changes are reflected .

## VALIDATION CHECKS 
- Username     - Has a validation check , spaces cannot be there 
- Adhar number - Should be of length 12 digits , only integer numbers ,and no spaces or special charecters .
- Phone number - Should be of length 10 digits , only integer numbers , and no spaces or special charecters.
- Card-pin     - Should be of length 10 digits , only integer numbers , and no spaces or special charecters.
- Card-cvv     - Should be of length 10 digits , only integer numbers , and no spaces or special charecters.
- Password     - Should match with the one given while registering .
## Functions
> For each different feature i have used different function calls 
- Register
- Usercards
- Getinfo
- Beni
- Cards
- Add
- New
- Change
- Update
- Transfer

## Tech

Tech stacks used for this project 

- [PYTHON] 
- [SQL] 




## Modules

These are varioue modules which i have imported
| Plugin | Import from  |
| ------ | ------ |
| Connection | multiprocessing |
| registered | xml.dom.domreg|
| a | mysql.connector |
| pd| pandas |


