# Research Paper Management

A quick and easy way to find and read research papers.

## Features:

- Easy to use
- User Login
- CRUD to maintain database
- Upload and download files

## Installation on Linux

### Clone the repo:

In terminal, enter the following commands

1. git clone https://github.com/prabesh012/crud_app

### Setup Virtual Environment

Inside the repo directory, setup a virtual environment and install required modules

1. python3 -m venv env or virtualenv env
2. source env/bin/activate
3. pip3 install -r requirements.txt

### Export flask app

To export the flask app and integrate db with it

1. export FLASK_APP=application.py
2. export FLASK_ENV=development
3. export FLASK_DEBUG=1
4. sudo apt-get install python3-sqlalchemy
5. python3 -m flask db init (Try to run flask db init, if you get an error, I suggest to install the sqlalchemy using sudo)
6. python3 -m flask db migrate -m "Database Created"
7. python3 -m flask db upgrade

## Installation on Windows

### Clone the repo:

In terminal, enter the following commands

1. git clone https://github.com/prabesh012/crud_app

### Setup Virtual Environment

Inside the repo directory, setup a virtual environment and install required modules

1. python3 -m venv env or virtualenv env
2. source env/Scripts/activate
3. pip3 install -r requirements.txt

### Export flask app

To export the flask app and integrate db with it

1. set FLASK_APP=application.py
2. set FLASK_ENV=development
3. flask db init
4. flask db migrate -m "database Created"
5. flask db upgrade

## Setting up gmail for mail functionality

1. Make a new gmail account
2. Go to Gmail Settings >> See all settings
3. Go to Forwarding & POP/IMAP >> In POP download Select Enable pop for all mail and Save Changes
4. In gmail's setting itself, Go to Account and Import >> Click on Other Google Account settings >> In the top navigation, go to Security >> In Less secure app access, Allow less secure apps

## Update the .env file located in the project folder

MAIL_PASSWORD=password(type the password for the gmail account, no spaces,no quotes)
MAIL_USERNAME=example@example.com(type the password for the gmail account, no spaces,no quotes)

## Features in developement

- Search files from the search bar
- Send files directly to mail as well
- Fully responsive UI
