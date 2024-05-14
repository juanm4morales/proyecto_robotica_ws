import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():
    world_folder = 'Race_World'
    world_index = 'Race.xml'
    package_name='boxbots'
    package_path = get_package_share_directory(package_name)

    # Start simulation
    sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(package_path, 'launch', 'launch_sim.launch.py')
        ]), launch_arguments={
            'world': os.path.join(package_path, 'worlds', world_folder, world_index)
        }.items()
    )

    # Start slam
    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory("slam_toolbox"), 'launch', 'online_async_launch.py')
        ]), launch_arguments={
            'slam_params_file': os.path.join(package_path, 'config', 'mapper_params_online_async.yaml'),
            'use_sim_time': 'true'
        }.items()
    )

    # Start navigation node
    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory("nav2_bringup"), 'launch', 'navigation_launch.py')
        ]), launch_arguments={ 'use_sim_time': 'true' }.items()
    )

    # Launch them all!
    return LaunchDescription([
        sim,
        slam,
        navigation
    ])