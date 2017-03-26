FROM python:2.7-wheezy
MAINTAINER "ntoofu"
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /work
WORKDIR /work
CMD /bin/bash
