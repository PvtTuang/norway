FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install Pillow
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8056

CMD ["python", "manage.py", "runserver", "0.0.0.0:8999"]