# CenterAI-api

After clone
1. pip install -r requirements.txt
2. docker pull postgres
3. docker run --name centerai_postgres -e POSTGRES_PASSWORD=centerai -d -p 5432:5432 postgres
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver

