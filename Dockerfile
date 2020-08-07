FROM python:3.6

ADD . /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN echo yes | python manage.py collectstatic

EXPOSE 8000

CMD exec gunicorn docflow.wsgi:application --bind 0.0.0.0:8000 --workers 3