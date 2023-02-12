# Engineering-Challenge
brief:
this project is a solution for FlexPwe EngineeringChallenge ( github.com/FlexPwr/EngineeringChallenge#Submission-Instructions )
it is built using python 3 and Django framework and has 3 main functionalities:
* calculates total buy volume for flex power
* calculates total buy volume
* calculates total profit and loss

# Used technologies
* Language: python 3
* frameworks : django / djangorest
* database: builtin SQLite
* unit testing: Django.test

# Docker image:
to get the docker image for this application run the below command
## >> docker pull lbustanji/engineering-challenge

# Code structure:
## there are two classes (models) used in this project :
* Trade: represents trade record in the database
* PnlData: represents the response as required by the challenge

and they are both in the file named models.py (Engineering-Challenge/trade/models.py)

## the methods that perform the required calculations can be found in the views.py file (Engineering-Challenge/trade/views.py)
* compute_pnl
* compute_total_buy_volume
* compute_total_sell_volume

## Unit-Test
Engineering-Challenge/trade/test.py
contains 3 testing methods for the 3 functions

# using the exposed API
## running the application
* run the below commands
## >> env\Scripts\activate 
## >> python manage.py runserver
*open a browser and go to the URL:http://127.0.0.1:8000/pnl/strategy_id
and replace strategy_id with the desired strategy id
