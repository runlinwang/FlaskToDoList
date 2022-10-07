## RunLin's Flask To-Do App

Code based off of tutorial at https://github.com/onurtacc/flask-todo-app

Github repository at 

## Features

This todo app contains the basic functionality of being able to add and check off / uncheck tasks (by clicking the "Update" button for the task that you want to change the completion status of). Additionally, there is the added feature of deleting tasks that was in the tutorial. I have also personally implemented the counter feature, which continually tells the user how many items are still on the todo list overall, and how many still need to be completed. Most of the comments I make are in the `app.py` file, and there are also a few comments in the `index.html` file.

## Reflection

Flask is the first tool that allows us to integrate Python into our front-end code. The flexibility, ease of testing, and easy to understand nature of programming using Flask is tremendously helpful for beginners. However, we must also note that Flask has a single source that can only handle one request at a time, which can present scalability issues. Additionally, the usage of external third party modules increases security risks in case a malicious module is involved.

Note: I read up on some of the technical details about Flask at this source! https://dev.to/detimo/python-flask-pros-and-cons-1mlo

## Running the App

This app can be run locally; please download the repository and navigate to the folder. Then, follow these instructions:

<hr>

- Run `python3 -m venv venv` to create a virtual environment and activate it.
- Run `pip3 install -r requirements.txt` to ensure that the correct packages / dependencies are installed.
- Run `python3 app.py` to start the local server, and navigate to the provded local address to see the interface!

<hr>



