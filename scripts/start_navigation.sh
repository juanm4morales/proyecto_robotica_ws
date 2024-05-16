#!/bin/bash

gnome-terminal -- bash -c "ros2 run rviz2 rviz2 -d src/boxbots/config/rviz_slam_with_navigation.rviz; exec bash"
ros2 launch boxbots navigation_launch.launch.py; exec bash
