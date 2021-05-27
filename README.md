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
1. virtualenv env
2. source env/bin/activate
3. pip3 install -r requirements.txt

### Export flask app
To export the flask app and integrate db with it
1. export FLASK_APP=application.py
2. export FLASK_ENV=development
3. flask db init
4. flask db migrate -m "database Created"
5. flask db upgrade

## Installation on Windows

### Clone the repo:

In terminal, enter the following commands
1. git clone https://github.com/prabesh012/crud_app
### Setup Virtual Environment

Inside the repo directory, setup a virtual environment and install required modules
1. virtualenv env
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
You can use your own gmail account but it is recommended to use not used gmail account for security purpose

1. Make a gmail account >> Setting >> See all settings
-Forwarding & pop/mp >> Enable pop for all mail
- Account and Import >> other google account Setting >> Security >> Turn on Less Secure

## Update the .env file

MAIL_PASSWORD=password
MAIL_USERNAME=example@example.com

## Features in developement
- Search files from the search bar
- Send files directly to mail as well
- Fully responsive UI