# Full-Stack Django/VueJS demo

... in progress

## 🚀 Quick start

```
$ make setup
$ make setup-data

```

you can run the tests with the command:

```
$ make test
```
Note: you need previously run `make setup`

## Manual mode

In case you don't have docker installed, you can run the project manually

### Requirements
    - PostgreSQL intalled
    - Pipenv installed (https://pipenv.pypa.io/)
    - nodejs / npm

$ git clone https://github.com/erikriver/fullstack-django-vuejs-demo.git
$ cd fullstack-django-vuejs-demo/backend
$ pipenv install
$ pipenv shell

$ python manage.py migrate
$ python manage.py loaddata project/fixtures/users.json
$ python manage.py get_places
$ python manage.py runserver

## ToDo
    * Authentication
    * Authorization
    * More tests