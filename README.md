# DailyCode
RESTFul service with Django for maintaining competetive atmosphere by tracking and creating ranking by rating and streak submissions on LeetCode platform.

## Built With

- [Python](https://www.python.org/) 3.6.x
- [Django Rest Framework](http://www.django-rest-framework.org/) 3.8.x
- [Celery](https://api.jquery.com/) 5.x


## Features:
<li>Login/Register</li>
<li>Link LeetCode account with username</li>
<li>Create personal to-do list problems</li>
<li>Rating based on solved problems and streak submissions</li>
<li>Update profiles requesting LeetCode API with given time interval</li>

## Installation

Create new directory:

```shell
$ mkdir DailyCode && cd DailyCode
```

Create new virtual environment:

```shell
$ python -m venv venv
```

Activate virtual environment:

```shell
$ source venv/bin/activate  (For Linux)
$ venv/Scripts/activate  (For Windows)
```

Clone this repository:

```shell
$ git clone git@github.com:cdoos/DailyCode.git && cd DailyCode/project
```

Install requirements:

```shell
$ pip install -r requirements.txt
```

Check for any project errors:

```shell
$ python manage.py check
```

Run Django migrations to create database tables:

```shell
$ python manage.py migrate
```

Run the development server:

```shell
$ python manage.py runserver
```
