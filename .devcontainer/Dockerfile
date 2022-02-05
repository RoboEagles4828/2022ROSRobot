FROM ubuntu:20.04
RUN apt update && apt install -y xterm

COPY /install-scripts /opt/install-scripts
ENV PATH=$PATH:/opt/install-scripts

RUN install-base