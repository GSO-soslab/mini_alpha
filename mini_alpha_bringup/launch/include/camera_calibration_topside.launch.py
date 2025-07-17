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

    calibration_camera_topside_params_path = os.path.join(robot_param_path, 'config', 'camera_calibration_topside.yaml')

    explore_camera_remote_node = Node(
        package='dwe_camera_driver',
        executable='remote_node',
        name='explore_camera_remote_node',
        namespace=robot_name,
        output='screen',
        parameters=[calibration_camera_topside_params_path],
        remappings=[
            ('image_raw', 'exploreHD/image_raw')
        ]
    )

    # Node for camera calibration, converted from the ros2 run command
    camera_calibrator_node = Node(
        package='camera_calibration',
        executable='cameracalibrator',
        name='cameracalibrator',
        namespace=robot_name,
        output='screen',
        prefix='gnome-terminal --',
        arguments=[
            '--size', '6x8',
            '--square', '0.028',
            '--fisheye-k-coefficients=4',
            '--fisheye-fix-skew',
            '--fisheye-recompute-extrinsics',
            '--fisheye-check-conditions',
            '--max-chessboard-speed=0.5',
            '--no-service-check'
        ],
        remappings=[
            ('image', 'exploreHD/image_raw'),
            ('camera', 'dwe_camera')
        ]
    )

    return LaunchDescription([
        explore_camera_remote_node,
        camera_calibrator_node
    ])