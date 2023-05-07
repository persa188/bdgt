FROM python:3

WORKDIR /bdgt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
WORKDIR /bdgt/bdgt

CMD [ "python", "manage.py", "collectstatic", "--noinput"]
CMD [ "python", "manage.py", "makemigrations", "bdgt" ]
CMD [ "python", "manage.py", "migrate", "" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]