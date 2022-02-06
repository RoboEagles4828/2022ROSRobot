FROM ubuntu:20.04

COPY /.dev_image/install-scripts /opt/install-scripts
ENV PATH=$PATH:/opt/install-scripts

RUN install-base
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN DEBIAN_FRONTEND=noninteractive apt-get install keyboard-configuration
RUN install-ros2
RUN install-gazebo