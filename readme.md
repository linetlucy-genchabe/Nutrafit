## Nutrafit
# Author
Linetlucy Genchabe

## Description
This is an application where certified nutritionists and fitness coaches can upload meal plans and workouts to help people embrace healthy living.


## User Stories

* Users need to Sign in to the application to start using it

* Users can Set up a profile about them 
* Users Find  different posts about nutrition and fitness.
* Users can click view details of a single post.

* Users can search for a specific post.

*  Users can Find Contact Information for the professionals





## Home 
![Home](./static/images/home.png)

## login
![Home](./static/images/login.png)

## viewPost details
![Home](./static/images/viewpost.png)




## SETUP AND INSTALLATION 
### Prerequisites
* python3.8
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/linetlucy-genchabe/Nutrafit.git
        $ cd Neighbourhood-Trends

## Running the Application
* Install virtual environment using `$ python3.8 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.8 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations watch
        $ python3.8 manage.py migrate 

* To run the application, in your terminal:

        $ python3.8 manage.py runserver


## Technologies Used
- Python3.8
- Django
- HTML
- Bootstrap
- cloudinary 
- Postgres Database


## live link 

https://nutrafit.herokuapp.com/

## License
MIT license


## Author's Info

* linetlucy21@gmail.com  

<p align = "center">
    &copy; 2022 @Linetlucy Genchabe.
</p>