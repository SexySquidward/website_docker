FROM python:3.7.2-stretch
WORKDIR /app
ADD . /app
RUN pip install -r requirments.txt
CMD["uwsgi",'app.ini']