FROM python:3.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    && apt-get -y install git procps lsb-release \
    && apt-get autoremove -y \
    && apt-get clean -y

COPY . /comp0010

RUN chmod u+x /comp0010/sh
RUN chmod u+x /comp0010/tools/test
RUN chmod u+x /comp0010/tools/coverage
RUN chmod u+x /comp0010/tools/analysis

RUN cd /comp0010 && python -m pip install -r requirements.txt

RUN echo "hello" > smth.txt
RUN echo "hello" > smth1.txt
RUN echo "hello" > smth2.txt
RUN echo "hello" > smth3.txt


ENV DEBIAN_FRONTEND=

EXPOSE 8000

