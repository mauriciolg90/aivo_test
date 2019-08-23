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

## Create a virtual environment

Creating a virtual environment will isolate the libraries for one project from another and is very useful when you have multiple Python applications running on a single server.

To create a virtual environment, perform the following:

```
# Create a new folder for your files:
$ mkdir ~/aivo

# Make sure you are in the above directory:
$ cd ~/aivo

# Install and create the virtual environment (on mac/linux):
$ sudo apt-get install python3-venv
$ python3 -m venv flask_env

# Activate the virtualenv created recently:
$ source flask_env/bin/activate

# NOTE: when you are done with virtualenv, you can run:
$ deactivate
```