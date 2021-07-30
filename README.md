
### ***Online job portal***

## Author
***Juma Allan.***

## Description

Online Job portal is a Django website application that allows  registered users - for the jobseekers to find available job listings and apply ,and as for the employers to post the vacant positions in their companies for the qualified canditates available.

## Set Up and Installations

### Prerequisites
    - Ubuntu Software
    - Python3.8.10
    - Postgres
    - python virtual environment (virtual:venv).
    - Text editor - preferably Visual Studio Code Editor.

### Clone the  project Repo
Run the following command on the terminal:
`git clone https://github.com/juma-moringa/Online_job_portal.git`
* cd ONLINE_JOB_PORTAL

###  Install and activate virtual environment
Activate virtual environment using python3.8 
1. Install
* python3 -m venv virtual
2. Activate
* source virtual/bin/activate

### Install dependancies
Install  all dependancies that will make the app run/function
* pip install -r requirements.txt

### Create the Database
* psql
* create database onlinejob;

### Make Migrations
* python3 manage.py makemigrations jobsapp
* python3 manage.py migrate

### Run the app
* python3 manage.py runserver
* open your browser with the local host; `127.0.0.1:8000` provided on the terminal

## Testing the application
* python3 manage.py test jobsapp

### Admin dashboard
* The admin dashboard can be accessed from the dropdown menu just below the profile icon.
* Firstly you must be on the homepage to access it.
`Username: Admin`
`Password: Access254`


### Technologies used
    - Python 3.8.10
    - HTML5
    - Django 3.2.5
    - Bootstrap 3
    - Django-Heroku
    - Postgresql
    - GIT
    - Material Design
    - Heroku
### known bugs
* Not responsive on mobile view but the development of the app is still in progress. 

### Enjoy :)


### Live Link

***[View Live Site.](linkupjobs.herokuapp.com/)***

### License

Online job portal is under the ***[MIT](LICENSE)*** license.

@Jaycreations-2021.