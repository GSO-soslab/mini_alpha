import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """
    Launch file to run two instances of the dwe_camera_node for two cameras,
    with remappings to ensure topics are unique.
    """
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'
    
    # The package name is 'dwe_camera' as defined in setup.py
    robot_param_path = get_package_share_directory(robot_bringup)

    calibration_camera_vehicle_params_path = os.path.join(robot_param_path, 'config', 'camera_calibration_vehicle.yaml')

    explore_camera_node = Node(
        package='dwe_camera_driver',
        executable='camera_node',
        name='explore_camera_node',
        namespace=robot_name,
        output='screen',
        parameters=[calibration_camera_vehicle_params_path],
        remappings=[
            ('image/compressed', 'exploreHD/image/compressed'),
            ('image_lowbw/compressed', 'exploreHD/image_lowbw/compressed'),
            ('camera_settings', 'exploreHD/camera_settings'),
        ]
    )

    return LaunchDescription([
        explore_camera_node
    ])