FROM debian:jessie

MAINTAINER HSR Geometalab <geometalab@hsr.ch>

# also see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/ for best practices
RUN apt-get clean && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    osmctools \
    parallel \
    wget \
    python3 \
    python3-dev \
    python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/pbf-provisioner

ADD ./requirements.txt /home/pbf-provisioner/requirements.txt

RUN pip3 install -r requirements.txt


