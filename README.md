# Flask Application on CRUD operations on MongoDB

## This application is totally built using Python Flask and uses MongoDB to store the data . It can also perform operations like Inserting new data , Deleting data,Updating previously entered data and fetching data from the mongoDB database.

# Table of Contents
  - main.py
  - Dockerfile
  - requirements.txt
  - myenv
# Brief of the Contents
  - **main.py** 
    - This is the main file of the project.
    - This is made entirely using Python.
    - The modules used in creating the project are 
      - flask : used in creating the python application
      - flask_pymongo and pymongo: used in connecting mongoDB to the flask application.
      - json and bson : used in working with json objects
    - The mongoDB database named myDB and a collection named user_list was created initially.
    - The routes used in this app are
      -  /get_all_users : fetches all the users from the collection. The user's data is stored in the database as documents which are json objects.
      -  /get_user_with/id : fetch the particular user with given id.
      -  /add_user : a json object is passed with the object and it is stored in the collection.
      -  /update_user_with_id/id: updates information of the user with given id
      -  /delete_user/id: deletes user with given id
  - **requirements.txt**
    - This file contains all the modules required to run this project along with the required versions.
  - **myenv**
    - This is a virtual environment used in running applications . Using this environment we can run the python application by activating it and installing the modules using pip.
# Requirements
  - python:3.10.2
  - pip
  - postman
  - VSCode
  - venv
  - NOSQL booster for MONGODB
# Installation
  - Clone the project in your local directory
  - Ensure that myenv is installed
  - Open the terminal in VS Code and activate enviroment by myenv/Scripts/activate.ps1
  - Ensure that all the requirements of the modules are satisfied
  - Run the main.py file and check it's output through postman.

     
           

