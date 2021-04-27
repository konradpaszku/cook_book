# cook_book
This is not a big project, It is only homework for interview to check my skills with Django Rest Framework and JWT Authentication.
I had to make cook book app with endpoints which show all the recipes and ingredients, and show all details of them.

# Manual to run the app
Create a virtualenv and install the project requirements, which are listed in requirements.txt. The easiest way to do this is with pip install -r requirements.txt while your virtualenv is activated.

In order to initialize the database for the project, go into the cookbook directory. Then run the following command python manage.py makemigrations then type python manage.py migrate. This will run all of the migrations for the project and initialize the database.

To run the project type in python manage.py runserver

To check the JWT authentication and endpoints you have to make admin account, type to terminal 'python manage.py createsuperuser' and follow the instructions.

To get JWT you have to do these steps:
Go to http://127.0.0.1:8000/api/token/ and log in as admin and then browser will show you access and refresh token.
Now you can go to the home page http://127.0.0.1:8000/ and turn on postman app.
In postman app put the token in authorization as bearer token.
You have only 1 min then you will lose you permission and you will have to make authorization once again.<br />
I added sqlite to github page for some examples, and log in as superuser : login: 'user' password :'admin'. <br />
URLs to check endpoints:

http://127.0.0.1:8000/api/ <- browser show all recipes in database<br />
http://127.0.0.1:8000/api/id <- browser show you one specific recipe<br />
http://127.0.0.1:8000/api/ingredients/ <- browser show all ingredients in database<br />
http://127.0.0.1:8000/api/ingredients/id <- browser show you one specific ingredient<br />
The id must be the integer.


