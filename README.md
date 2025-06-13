# Django Internship Project

A simple Django REST API project with:

- Public & Protected APIs (JWT Authentication)
- User Login page (Django)
- Celery Task for Email sending
- Telegram Bot Integration to collect Telegram usernames
- .env configuration for production

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Task Queue:** Celery + Redis
- **Telegram Bot:** python-telegram-bot
- **Database:** SQLite (can be changed to PostgreSQL/MySQL)
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Environment Variables:** Python-dotenv
- **Version Control:** Git + GitHub

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/deshna0620/django_internship_project.git
cd django_internship_project


### 2. Create Virtual Environment
python -m venv telegram_venv
telegram_venv\Scripts\activate # For Windows


### 3. Install Requirements
pip install -r requirements.txt


### 4. Configure `.env`
Create a `.env` file in the root directory using `.env.example` as a reference:

SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password

REDIS_URL=redis://localhost:6379

TELEGRAM_BOT_TOKEN=your-telegram-bot-token


### 5. Apply Migrations
python manage.py migrate

### 6. Run Django Server
python manage.py runserver

### 7. Start Celery Worker (New Terminal)
celery -A internship_project worker --pool=solo --loglevel=info

### 8. Run Telegram Bot (New Terminal)
python mainapp/telegram_bot.py


## API Documentation

### 1. Public API (No Auth Required)
- **URL:** `/api/public/`
- **Method:** GET
- **Response:**
{
"message": "This is a public endpoint accessible to everyone."
}


### 2. Protected API (JWT Auth Required)
- **URL:** `/api/protected/`
- **Method:** GET
- **Header:**
Authorization: Bearer <your_token>
- **Response:**
{
"message": "This is a protected endpoint accessible only to authenticated users."
}


### 3. Token Authentication (JWT)
- **URL:** `/api/token/`
- **Method:** POST
- **Body:**
{
"username": "your-username",
"password": "your-password"
}
- **Response:**
{
"refresh": "your-refresh-token",
"access": "your-access-token"
}


## Telegram Bot

- **Run:** `python mainapp/telegram_bot.py`
- **Commands Supported:**
  - `/start` — Registers your Telegram username into Django DB.
  - `/help` — Shows help info.

## Celery Task

A Celery task runs in the background to send an email after user registration (configured in `mainapp/tasks.py`).

## Environment Variables Used

| Variable            | Purpose                                |
|--------------------|----------------------------------------|
| SECRET_KEY         | Django Secret Key                       |
| DEBUG              | Debug Mode (set False in production)    |
| ALLOWED_HOSTS      | Allowed Hosts                           |
| DB_*               | Database configuration                 |
| EMAIL_*            | Email backend for sending emails       |
| REDIS_URL          | Redis broker URL for Celery             |
| TELEGRAM_BOT_TOKEN | Telegram Bot Token                      |

## Run Locally Summary
git clone https://github.com/deshna0620/django_internship_project.git
cd django_internship_project

python -m venv telegram_venv
telegram_venv\Scripts\activate # For Windows

pip install -r requirements.txt

cp .env.example .env # Or create manually

python manage.py migrate

python manage.py runserver

celery -A internship_project worker --pool=solo --loglevel=info

python mainapp/telegram_bot.py


## Notes

- This project is for backend demonstration only.
- Deployment is not required as per internship instructions.
- Ensure your `.env` file is **NOT** pushed to GitHub.
