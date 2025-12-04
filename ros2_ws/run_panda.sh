#!/bin/bash
# Franka Emika Panda Robot ROS 2 Visualization Launch Script

# 获取脚本所在的目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 进入工作区
cd "${SCRIPT_DIR}"

# Source ROS 2 setup（使用 Humble 环境）
source /opt/ros/humble/setup.bash
source install/setup.bash

# 启动 Panda 机器人可视化
echo "=========================================="
echo "Franka Emika Panda Robot ROS 2 Visualization"
echo "=========================================="
echo ""
echo "启动组件:"
echo "  - Robot State Publisher (发布机器人状态)"
echo "  - Joint State Publisher (发布关节状态)"
echo "  - RViz2 (可视化显示)"
echo ""
echo "按 Ctrl+C 停止"
echo "=========================================="
echo ""

ros2 launch panda_description view_panda.launch.py
