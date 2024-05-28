import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled

    package_name = 'boxbots'
    package_path = get_package_share_directory(package_name)

    #WORLD
    world = LaunchConfiguration('world')
    world_path = os.path.join(package_path, 'worlds', 'Race_World','Race.xml')
    world_arg= DeclareLaunchArgument(name='world', default_value=world_path, description='Full path to the world model file to load')

    # Start robot
       
    rsp1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(package_path,'launch','rsp1.launch.py')]),
        launch_arguments={'use_sim_time': 'true',
                          'robot_name': 'donBarredora',
                          'robot_description_topic': "donBarredora/robot_description"
                         }.items()
    )

    rsp2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(package_path,'launch','rsp2.launch.py')]),
        launch_arguments={'use_sim_time': 'true',
                          'robot_name': 'axeBot',
                          'robot_description_topic': "axeBot/robot_description"
                          }.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': world}.items()
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity1 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        namespace="donBarredora",
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'donBarredora',
            '-x', '1.0',  # Coordenada X
            '-y', '0.0',  # Coordenada Y
            '-z', '1.0',  # Coordenada Z
            '-R', '0.0',  # Rotación en el eje X (roll)
            '-P', '0.0',  # Rotación en el eje Y (pitch)
            '-Y', '-1.57'  # Rotación en el eje Z (yaw)
        ],
        output='screen'
    )

    spawn_entity2 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        namespace="axeBot",
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'axeBot',
            '-x', '-1.0',  # Coordenada X
            '-y', '0.0',  # Coordenada Y
            '-z', '1.0',  # Coordenada Z
            '-R', '0.0',  # Rotación en el eje X (roll)
            '-P', '0.0',  # Rotación en el eje Y (pitch)
            '-Y', '-1.57'  # Rotación en el eje Z (yaw)
        ],
        output='screen'
    )

    # Launch them all!
    return LaunchDescription([
        world_arg,
        rsp1,
        rsp2,
        gazebo,
        spawn_entity1,
        spawn_entity2
    ])