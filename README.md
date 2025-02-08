# Authentication System
## 1. Project Overview
- This project is an Authentication System developed using Python and Django. It allows users to register, log in, and manage their accounts securely.
## 2. Features
- Secure login with password hashing.
- Password reset functionality.
- User profile management.
- Also implemented the authorization.
- All the modules are built using inbuilt forms and views.
## 3. Technologies Used
- Python
- Django
- HTML/CSS for frontend
- SQLite for the database
## 4. Installation Instructions
- Clone repository
  - ``` bash
    git clone https://github.com/rahulsmrd/AuthenticationSystem.git
    ```
- Change Directory
  - ``` bash
    cd AuthenticationSystem
    ```
- Create and Activate Virtual Environment
  - ``` bash
    python -m venv venv
    ```
  - ``` bash
    venv\Scripts\activate
    ```
- Install requirements
  - ``` bash
    pip install requirements.txt
    ```
- Run Migrations
  - ```bash
    python manage.py makemigrations
    ```
  - ```bash
    python manage.py migrate
    ```
- Create Super User
  - ```bash
    python manage.py createsuperuser
    ```
  - Enter the credentials and add Super User
- Run Server
  - ```bash
    python manage.py runserver
    ```
## 5. User Guide
- Access the registration page at `http://localhost:8000/signup/` to create a new account.
- Log in at `http://localhost:8000/login/` using your credentials.
- To reset your password, navigate to `http://localhost:8000/change-password/` and follow the prompts.
- To view profile, navigate to `http://localhost:8000/profile/`.
## 6. project Structure
- `authentication_system/` - Contains the Django application modules.
- `home/` - Contains templates and static files for the home page.
- `manage.py` - Django's command-line utility for administrative tasks.
