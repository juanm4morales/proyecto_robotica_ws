import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled

    package_name='boxbots'

    rsp_bot1 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp_bot1.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    rsp_bot2 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp_bot2.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    rsp_bot3 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp_bot3.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    joystick_bot1 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick_bot1.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    joystick_bot2 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick_bot2.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    joystick_bot3 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick_bot3.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )


    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity_bot1 = Node(package='gazebo_ros', executable='spawn_entity.py',
                        namespace='bot_1',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')

    spawn_entity_bot2 = Node(package='gazebo_ros', executable='spawn_entity.py',
                        namespace = 'bot_2',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot2'],
                        output='screen')
    
    spawn_entity_bot3 = Node(package='gazebo_ros', executable='spawn_entity.py',
                        namespace = 'bot_3',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot3'],
                        output='screen')


    # Launch them all!
    return LaunchDescription([
        rsp_bot1,
        rsp_bot2,
        rsp_bot3,
        gazebo,
        spawn_entity_bot1,
        spawn_entity_bot2,
        spawn_entity_bot3,
        joystick_bot1,
        joystick_bot2,
        joystick_bot3  
    ])