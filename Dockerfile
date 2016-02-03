#FROM python:2-onbuild
FROM django:onbuild

RUN python manage.py makemigrations srepo; python manage.py migrate
