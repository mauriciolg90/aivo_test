# API REST for Aivo

This web application is used to filter countries according to indexs provided by the user. It can be extended easily by adding new routes on controllers module at app folder.

## Project hierarchy

app/  
|-> controllers.py  
|-> models.py  
test/  
|-> unit/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-> pytest.ini  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-> test_countries.py  
util/  
|-> input_file.csv  
|-> script.sql  
db_setup.py  
main.py  
requirements.txt  

## Install principal packages

We need Git tools to clone the project, PIP to install Python packages, a SQL server to make queries and a virtual environment for Python:

```
$ sudo apt install git
$ sudo apt install python3-pip
$ sudo apt install mysql-server
$ sudo apt-get install python3-venv
```

## Create a MySQL user

A new user account will allow us to bring data from a CSV file:

```
# Write the root password after run the following:
$ sudo mysql -u root -p

# In this example, 'mauri' is the new user and '280490mg' is its password:
mysql> CREATE USER 'mauri'@'localhost' IDENTIFIED BY '280490mg';
Query OK, 0 rows affected (0.00 sec)

# Finally, we need to give it permissions to create a database later:
mysql> GRANT ALL PRIVILEGES ON *.* TO 'mauri'@'localhost' WITH GRANT OPTION;
Query OK, 0 rows affected (0.00 sec)
```

## Clone the project

To clone the repository to your local machine, perform the following:

```
# Create a new folder for your files:
$ mkdir ~/aivo

# Make sure you are in the above directory:
$ cd ~/aivo

# Clone the repository:
$ git clone https://github.com/mauriciolg90/aivo_test.git
```

## Read the CSV file

A simple way to query the data is to load the CSV into a SQL table:

```
# Make sure the SQL script is on the below directory (downloaded previously):
mysql -u mauri -p < ~/aivo/aivo_test/util/script.sql
```

The previous command requires to insert the password, and if we didn't receive any error messages, then all were ok.

## Create a virtual environment

Creating a virtual environment will isolate the libraries for one project from another and is very useful when you have multiple Python applications running on a single server.

To create a virtual environment, perform the following:

```
# Make sure you are in the work directory:
$ cd ~/aivo

# Create the virtual environment (on mac/linux):
$ python3 -m venv flask_env
```

## Configure bash environment

For making your environment variables accessible to the application, you will need to modify your virtualenv activation file:

```
# Open the file using any text editor, for example:
$ nano flask_env/bin/activate

# Add the following lines according to the SQL parameters configured previously:

export DB_HOST='localhost'
export DB_PORT='3306'
export DB_NAME='flask_test'
export DB_USER='mauri'
export DB_PASS='280490mg'

# Save and exit
```

NOTE: by default, host and port are 'localhost' and '3306' respectively.

## Init the virtual environment

Finally, we can start to use the virtual environment doing:

```
# Activate the virtualenv created:
$ source flask_env/bin/activate

# Install flask and other dependencies:
$ pip3 install -r aivo_test/requirements.txt

# NOTE: when you are done with virtualenv, you can run:
$ deactivate
```