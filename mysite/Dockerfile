FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install django-environ
RUN pip install psycopg2
RUN pip install Pillow
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8999

CMD ["python", "manage.py", "runserver", "0.0.0.0:8999"]