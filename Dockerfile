FROM  osrf/ros:humble-desktop-full

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

USER root
SHELL [ "/bin/bash" , "-c" ]

RUN apt-get update
RUN apt-get install -y git \
    python3-pip

RUN sudo apt-get update \
    && sudo apt-get install -y python3-colcon-common-extensions \
    ros-humble-xacro \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-joint-state-publisher-gui \
    ros-humble-gazebo-plugins \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-joint-state-publisher \
    ros-humble-gazebo-ros \
    ros-humble-twist-mux \
    ros-humble-slam-toolbox \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-gazebo-ros2-control 


COPY . /root/proyecto_robotica_ws
 
RUN source /opt/ros/humble/setup.bash \
    && cd /root/proyecto_robotica_ws \
    && colcon build


RUN echo "cat /root/proyecto_robotica_ws/scripts/initial_bashrc" >> ~/.bashrc
RUN echo "source /root/proyecto_robotica_ws/install/setup.bash" >> ~/.bashrc


RUN echo "DONE!"

