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
    nano \
    python3-pip

###########################################
# para manejo de usuarios es la siguiente seccion

# Create a non-root user
# ARG USERNAME=ros
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

# RUN groupadd --gid $USER_GID $USERNAME \
#     && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
#     && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config

# Set up sudo
# RUN apt-get update \
#     && apt-get install -y sudo \
#     && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
#     && chmod 0440 /etc/sudoers.d/$USERNAME \
#     && rm -rf /var/lib/apt/lists/*

# RUN source /opt/ros/humble/setup.bash \
# cd ~/ \
# mv /root/proyecto_robotica_ws .
###########################################

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
    ros-humble-slam-toolbox


COPY . /root/proyecto_robotica_ws
# USER ros
 
RUN source /opt/ros/humble/setup.bash \
    && cd /root/proyecto_robotica_ws \
    && colcon build

# WORKDIR ~/ 

RUN echo "source /root/proyecto_robotica_ws/install/setup.bash" >> ~/.bashrc
RUN pip install opencv-contrib-python==4.6.0.66


RUN echo "DONE!"

