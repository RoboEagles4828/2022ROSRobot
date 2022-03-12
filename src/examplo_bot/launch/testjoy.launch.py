import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

import xacro


def generate_launch_description():

    # Joystick Teleop
    joy = Node(
            package='joy', 
            executable='joy_node', 
            name='joy_node',
            parameters=[{
                'dev': '/dev/input/js0',
                'deadzone': 0.3,
                'autorepeat_rate': 20.0,
            }])

    config_filepath = os.path.join(get_package_share_directory('teleop_twist_joy'), 'config/xbox.config.yaml')
    teleop = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy_node', 
        parameters=[config_filepath],
        remappings={('/cmd_vel', '/diff_drive_base_controller/cmd_vel_unstamped')}
        )


    # Launch!
    return LaunchDescription([
        joy,
        teleop
    ])
