import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled

    package_name = 'boxbots'
    package_path = get_package_share_directory(package_name)

    # Start robot
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            package_path,'launch','rsp1.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    rsp2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            package_path,'launch','rsp2.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )


    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ])
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        namespace='donBarredora',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'donBarredora'
        ],
        output='screen'
    )

    spawn_entity2 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        namespace='axeBot',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'axeBot'
        ],
        output='screen'
    )



    # Launch them all!
    return LaunchDescription([
        rsp,
        rsp2,
        gazebo,
        spawn_entity,
        spawn_entity2,
    ])