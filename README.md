Django-todolist
===============
# What is it?

Simple todo list application using python webservices .


## Development Environment Dependencies

* Python 2.5 or higher
* Django , Djando piston {light weight webservices framework for Django}
* Git


## Build DataBase

Step 1: In settings.py modify DATABASES tag
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'path to the database file', # Or path to database file if using sqlite3.

    }
}
```
Step2: run command python manage.py syncdb


CSRF Token : Needed for authentication , as every api call is to be done by an authenticated user in django

```
default token : X-CSRFToken: bFzhzpKhsasg1vRiwjVa3ZyXHGDmeS1U
 ```

