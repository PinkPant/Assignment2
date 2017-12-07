FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install \
        python-pip \
        python-setuptools \
        build-essential
COPY . /project
WORKDIR /project
RUN pip install -r requirements.txt
CMD ["/bin/bash"]
