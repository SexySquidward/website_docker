FROM python:3.7.2-stretch
WORKDIR /app
ADD . /app
RUN pip install -r requriments.txt
CMD ["uwsgi",'app.ini']