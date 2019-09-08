# TRANSPORT

###### Truck/Cab Management Website. It can be used by businesses which have large fleets of trucks or cabs to keep the record of expenses and trips(profits/sale). This can come in very handy especially in the case if the business has several branches in different cities which have to report to a central authority. This acts as a unified ledger. 

## Technology Stack:
### Backend
* #### Django(Python3)
###### Django is used here because of it's powerful underlying code that makes it very convenient to use and focus on logic rather than boilerplate code and also because of Python's ease of use.

### Frontend
* #### HTML/CSS
* #### JavaScript

### Database
* #### SQLite
  ###### It is used(which comes bundled with Django). This is only used for development purpose and a more powerful datatbase should be used in production.


## How to Use?
* Create a python3 virtual environment, navigate to project directory on terminal and install django using the command
  `pip install django` <br>
  RUN `python manage.py makemigrations` and `python manage.py migrate` <br>to create tables in database. <br>
  Entries can be made using the admin panel and superuser for admin panel can be created using the command<br>
  `python manage.py createsuperuser`<br>
  To run server, use command `python manage.py runserver`
  
 * Open a browser and navigate to <b>localhost:8000</b> to use the website.
