# DailyCode
RESTFul service with Django for maintaining competetive atmosphere by tracking and creating ranking by rating and streak submissions on LeetCode platform.
## Features:
<li>Login/Register</li>
<li>Link LeetCode account with username</li>
<li>Create personal to-do list problems</li>
<li>Rating based on solved problems and streak submissions</li>
<li>Update profiles requesting LeetCode API with given time interval</li>

## Installation

```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv) pip install -r requirements.txt
    (venv) cd projects
    (venv) python manage.py makemigrations
    (venv) python manage.py migrate
    (venv) python manage.py createsuperuser
    (venv) python manage.py runserver
```
