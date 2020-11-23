FROM python:3.7.2
WORKDIR /app
ADD . /app
RUN pip install -r install.txt
CMD ["uwsgi","app.ini"]
