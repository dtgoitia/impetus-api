# FROM python:alpine3.7
FROM python:3.7-slim

WORKDIR /impetus_api

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
COPY . /impetus_api/

RUN pipenv install --system

# CMD ["pipenv", "run", "python", "manage.py", "runserver"]
CMD ["python", "manage.py", "runserver"]
