FROM ubuntu:latest
MAINTAINER Rajani Saini "rajani.saini@student.ufv.ca"
RUN mkdir /app
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . /app
ADD run.py /app
WORKDIR /app
RUN pip install -r install.txt
EXPOSE 8080
CMD /app/run.py
