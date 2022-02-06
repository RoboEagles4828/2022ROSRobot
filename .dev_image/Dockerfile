FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
COPY /.dev_image/install-scripts /opt/install-scripts
ENV PATH=$PATH:/opt/install-scripts

RUN install-base
RUN TZ=Etc/UTC apt -y install tzdata
RUN apt -y install keyboard-configuration
RUN install-ros2
RUN install-gazebo