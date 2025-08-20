# ~/ros2_ws/src/skoltech/launch/display.launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
import os

def generate_launch_description():
    # дефолтный URDF файл (можешь изменить)
    default_urdf = os.path.join(
        os.getenv('HOME'), 'ros2_ws/src/skoltech/urdf/UR3_with_gripper.urdf'
    )

    # дефолтный rviz конфиг (локальный файл в src)
    default_rviz = os.path.join(
        os.getenv('HOME'), 'ros2_ws/src/skoltech/rviz/urdf.rviz'
    )

    declare_urdf = DeclareLaunchArgument(
        'urdf_file',
        default_value=default_urdf,
        description='Absolute path to robot urdf file'
    )

    declare_rviz = DeclareLaunchArgument(
        'rviz_config',
        default_value=default_rviz,
        description='Absolute path to rviz config file (optional)'
    )

    urdf_file = LaunchConfiguration('urdf_file')
    rviz_config = LaunchConfiguration('rviz_config')

    # читаем содержимое URDF через Command (будет выполнено в runtime)
    robot_description_cmd = Command(['cat ', urdf_file])

    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': ParameterValue(robot_description_cmd, value_type=str)
        }]
    )

    jsp_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # rviz: если rviz_config путь пустой или не существует, rviz запустится с пустым конфигом
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    return LaunchDescription([
        declare_urdf,
        declare_rviz,
        rsp_node,
        jsp_node,
        rviz_node,
    ])
