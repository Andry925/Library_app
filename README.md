## This is a basic web application for managing the work of library as librarian and user
This is a basic web application for managing library work, serving both librarians and users. The application includes basic functionalities such as user registration with different roles, login for existing users, and redirection to their respective profiles. After registration, my project  provides CRUD and filter functionalities for authors and books.

## Technologies I used for this project
 - PostgreSQL: To store data
 - Django Template Language: To reduce repeated HTML and display data on the frontend
 - Django ORM: To manage models
 - Django Signals: To create user profiles as soon as new users are registered
 - Class-Based Views: To create the backend
 - Python-Decouple: To store sensitive data
 - Unit Tests: To test applications

## How to use my project
 - To download all dependencies by running 'pip install-r requirements.txt'
 - Fill '.env-sample' file with your data
 - Run server with 'python manage.py runserver' and go to register page
 - Run some basic tests to test applications with python manage.py test 'app_name'




