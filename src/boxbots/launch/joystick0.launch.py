from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

import os
from ament_index_python.packages import get_package_share_directory

#el nombre del robot que se quiere controlar con joystick
bot_namespace = 'donBarredora'

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    joy_node = Node(
            package='joy',
            executable='joy_node',
            namespace=bot_namespace,
            parameters=[{'deadzone': 0.05},
                    {'autorepeat_rate': 20.0}, 
                    {'use_sim_time': use_sim_time},
                    {'device_id': 0}], 
                #en device_id se debe establecer el numero 
                #que el sistema asigno al dispositivo que queremos utilizar
        )

    teleop_node = Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_node',
            namespace=bot_namespace,
            parameters=[{'axis_linear.x': 1},
            {'enable_button': 6},
            {'require_enable_button': False},
            {'enable_turbo_button': 5},
            {'scale_linear.x': 0.3},
            {'scale_linear_turbo.x': 2.0},
            {'axis_angular.yaw': 0},
            {'scale_angular.yaw': 1.0},
            {'scale_angular_turbo.yaw': 2.0},
            {'axis_linear.x': 1},
            {'use_sim_time': use_sim_time}],
            remappings=[('/cmd_vel','/cmd_vel_joy')]
        )           

    # twist_stamper = Node(
    #         package='twist_stamper',
    #         executable='twist_stamper',
    #         parameters=[{'use_sim_time': use_sim_time}],
    #         remappings=[('/cmd_vel_in','/diff_cont/cmd_vel_unstamped'),
    #                     ('/cmd_vel_out','/diff_cont/cmd_vel')]
    #      )


    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        joy_node,
        teleop_node,
        # twist_stamper       
    ])