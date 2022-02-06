FROM ubuntu:20.04
LABEL org.opencontainers.image.source https://github.com/RoboEagles4828/2022ROSRobot

ARG DEBIAN_FRONTEND=noninteractive
COPY /.dev_image/install-scripts /opt/install-scripts
ENV PATH=$PATH:/opt/install-scripts

RUN install-base
RUN TZ=Etc/UTC apt -y install tzdata
RUN apt -y install keyboard-configuration
RUN install-ros2
RUN install-gazebo