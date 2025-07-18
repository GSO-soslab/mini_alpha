import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """
    Launch file to run the camera driver and the camera calibrator node.
    """
    robot_name = 'mini_alpha'
    robot_bringup = robot_name + '_bringup'
    
    robot_param_path = get_package_share_directory(robot_bringup)

    apriltag_detection_topside_params_path = os.path.join(robot_param_path, 'config', 'camera_calibration_tag_detection_topside.yaml')

    explore_camera_remote_node = Node(
        package='dwe_camera_driver',
        executable='remote_node',
        name='explore_camera_remote_node',
        namespace=robot_name,
        output='screen',
        parameters=[apriltag_detection_topside_params_path],
        remappings=[
            ('image_calibrated/compressed', 'exploreHD/image_calibrated/compressed'),
            ('apriltag_detection/compressed', 'exploreHD/apriltag_detection/image/compressed')
        ]
    )

    return LaunchDescription([
        explore_camera_remote_node,
    ])
