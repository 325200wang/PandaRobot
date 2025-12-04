import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # 获取 panda_description 包的路径
    panda_description_dir = get_package_share_directory('panda_description')
    urdf_path = os.path.join(panda_description_dir, 'urdf', 'panda.urdf')
    rviz_config_path = os.path.join(panda_description_dir, 'launch', 'panda.rviz')

    # 读取 URDF 文件内容
    with open(urdf_path, 'r') as f:
        robot_description = f.read()

    # 创建 launch 描述
    return LaunchDescription([
        # 发布 robot_description 参数
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': False,
            }],
        ),
        
        # 启动 joint_state_publisher_gui（GUI 版本 - 带关节滑块）
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen',
        ),
        
        # 启动 RViz2 进行可视化（使用预配置的 rviz 配置文件）
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen',
        ),
    ])
