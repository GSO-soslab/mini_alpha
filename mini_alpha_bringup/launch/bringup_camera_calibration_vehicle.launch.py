import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    arg_robot_name = 'mini_alpha'
    robot_bringup = arg_robot_name + '_bringup'

    camera = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(robot_bringup), 
                'launch','include','camera_calibration_vehicle.launch.py')), 
    )

    return LaunchDescription([
        camera
    ])