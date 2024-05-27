import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription, LaunchContext
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch_ros.actions import Node


import xacro


def rsp_setup(context: LaunchContext, robot_name, use_sim_time):
    robot_name_str = context.perform_substitution(robot_name)
    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('boxbots'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file, mappings={
        'robot_name': robot_name_str, 
        'use_ros2_control': 'true'
    })
    
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    
    robot_description_topic = "/" + robot_name_str + "/robot_description"
    # Create a robot_state_publisher node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params],
        remappings=[('/robot_description', robot_description_topic)]
    )
    return [node_robot_state_publisher]
 

# Place here the robot name without .xacro extension
def generate_launch_description():
    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true', description='Use sim time if true'),
        DeclareLaunchArgument('robot_name', default_value='axeBot', description='Name of current robot'),
        OpaqueFunction(function=rsp_setup,
                       args=[LaunchConfiguration('robot_name'),
                             LaunchConfiguration('use_sim_time')])
    ])