FROM python:3.4
VOLUME /code
WORKDIR /code
RUN pip install \
    gunicorn \
    flask
CMD gunicorn -w 4 -b 0.0.0.0:8000 myapp:app
