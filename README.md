This is a bidding website which uses Django and Python along with Jquery and HTML. The website has been deployed using openshift. This project was done as part of a group and helped me learn how to work with the Django framework and deployment of applications.

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).

2. Ensure that the executable `pg_config` is available on your machine. You can check this using `which pg_config`. If not, install the dependency with one of the following.
  - macOS: `brew install postgresql` using [Homebrew](https://brew.sh/)
  - Ubuntu: `sudo apt-get install libpq-dev`
  - [Others](https://stackoverflow.com/a/12037133/8122577)

3. Fork this repo and clone your fork:
    
4. Install dependencies:

    `pip install -r requirements.txt`

5. Create a development database:

    `./manage.py migrate`

6. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

7. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.
