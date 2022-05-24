# log_in
An app that requires a user to log in and uses cookies to allow them to stay logged in until the cookie expires.

# Running this app

## Virtual environments
When running projects like this it is good practice to use a <a href='https://www.geeksforgeeks.org/python-virtual-environment/'>virtual environment</a>. To create a virtual environment (assuming Python is already installed on your machine), create a new directory for it or choose an existing one. In that directory, run this command from the command line: 

`python3 -m venv /path/to/new/virtual/environment`

The path argument can simply be the name of your virtual environment if you just want it to be created in the current directory. In the main directory of your virtual environment, copy over your Python installation. After that, run the Django PIP installation in your virtual environement to install Django into your Python installation: 

`pip install Django==4.0.4`

You can run `python -m django --version` to check your Django version.

That's all you need to add to the virtual environment. To activate the virtual environment, run `C:/path/to/virtual/environment> activate`

## Starting the project and app structure

To start a Django project, run this command in any directory you want:

`django-admin startproject projectname`

A Django project can contain multiple apps. When you create the project, there will be another directory inside of it with the same name as the project. You will also have a manage.py file in the main directory. This file will be used to manage most actions concerning your project and associated apps. To create your first app, run this command in the project directory:

`python manage.py startapp appname`

You can just name the app "login." 

You will need to create two new Python files (forms.py and urls.py) for the app, all of the needed stylesheets, and some new directories. This is the app directory structure:

```
login
  templates
    login
      home.html
      login.html
      sign_up.html
  static
    login
      home_style.css
      login_style.css
      sign_up_style.css
    urls.py
    views.py
    forms.py
    models.py
```

From your project directory, go to the directory with the same name your project. In there, you will find the settings.py file. In the settings.py file, go to the Installed Apps setting, and add your app's name to the list like:

```
...
'random.stuff.middleware',
'random.stuff.middleware',
'login'
]
```

You should also add this new setting to the bottom of the settings.py file: `SESSION_COOKIE_HTTPONLY = True`

There is a urls.py file for the *project*, and a urls.py for the *app*. You need to make a change to the urls.py file for the *project*. Add this to the url patterns:

```
path('admin/', admin.site.urls),
path('login/', include('login.urls'))
```

## Running the app
  
From this point everything is set up. Copy all of the code from the repository into the corresponding files. Once you're done with that, run  these two commands:

```
python manage.py makemigrations login

python manage.py migrate
```

This creates the database tables specified in the models.py file. After that run `python manage.py runserver` to start the local Django server. Paste the url snippet provided in the command line (http://127.0.0.1:8000/) into your web broswer and you're good to navigate to any page of the project. Keep in mind that the URL of each page will be prefaced with "login/" in this app. Therefore, to get to the home page the URL would be "http://127.0.0.1:8000/login/home." The urls for all pages can be found in the urls.py file.

### Thank you for checking out my repository


