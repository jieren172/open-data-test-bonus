FROM ubuntu:18.04

########################################
#                                      #
#        Container preparation         #
#                                      #
########################################

WORKDIR /tmp
RUN apt-get update && \
    apt-get install -y build-essential software-properties-common

RUN apt-get update && \
    apt-get install -y python3 \
                       python3-pip \
                       python3-gdal \
                       gdal-bin \
                       libgdal-dev \
                       libsm6 \
                       libxext6 \
                       libxrender-dev


########################################
#                                      #
#       Preparing for execution        #
#                                      #
########################################


# Copying executable files
COPY data                 /usr/local/bin/test/data
COPY src                  /usr/local/bin/test/src
COPY requirements.txt     /usr/local/bin/test/requirements.txt


# Install python requirements
RUN pip3 install -r /usr/local/bin/test/requirements.txt


CMD python3 /usr/local/bin/test/src/main.py
