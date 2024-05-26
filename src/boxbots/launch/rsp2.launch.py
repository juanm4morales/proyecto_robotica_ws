import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro

# Place here the robot name without .xacro extension
def generate_launch_description():

    # Check if we're told to use sim time
    use_sim_time = LaunchConfiguration('use_sim_time')
    #TODO: Hacer que este argumento se pase como string
    #robot_name = LaunchConfiguration('robot_name')
    robot_name = "axeBot"
    robot_description_topic = LaunchConfiguration('robot_description_topic')

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('boxbots'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file, mappings={
        'robot_name': robot_name,  # Resuelve el LaunchConfiguration a su valor
    })

    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        namespace= robot_name,
        executable='robot_state_publisher',
        output='screen',
        parameters=[params],
        remappings=[('/robot_description', robot_description_topic)]
    )

    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false', description='Use sim time if true'),
        DeclareLaunchArgument('robot_name', default_value='robot', description='Name of current robot'),
        DeclareLaunchArgument('robot_description_topic', default_value='/robot_description', description='Topic name for the robot description'),
        node_robot_state_publisher
    ])