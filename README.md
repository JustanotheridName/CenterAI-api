# CenterAI-api

After clone

1. docker pull postgres
2. docker run --name centerai_postgres -e POSTGRES_PASSWORD=centerai -d -p 5432:5432 postgres
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver

