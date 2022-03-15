# [Clean City API](https://github.com/decadevs/clean_city.git)

API Service backing client interfaces for the Clean City Mobile Application.

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment

## Description


## Getting Started

Getting started with this project is very simple, all you need is to have Git installed on your machine. Then open up your terminal and run this command `git clone https://github.com/decadevs/clean_city.git` to clone the project repository.

Change directory into the project folder `cd clean_city`.
Open up another terminal and run this command `python manage.py makemigrations` for creating new migrations based on the models defined and also run `python manage.py migrate` to apply migrations.

In summary, run these commands in the following order, to start up the project.

```docker
1. git clone https://github.com/decadevs/clean_city.git
2. cd clean_city
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver
```

## Running Tests

Run the tests with the following command. Make sure that your api service is up and running.
 
```
python manage.py test
```

## License

The MIT License - Copyright (c) 2021 - Present, Decagon Institute. https://decagonhq.com/
