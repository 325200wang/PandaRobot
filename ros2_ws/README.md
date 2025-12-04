# Franka Emika Panda Robot - ROS 2 Humble

完整的 Franka Emika Panda 机器人 ROS 2 工作区，支持可视化和仿真。

## 📋 要求

- **操作系统**: Ubuntu 22.04 LTS
- **ROS 2**: Humble 版本
- **Python**: 3.10+
- **构建工具**: colcon

## 📦 安装依赖

```bash
sudo apt update
sudo apt install -y \
    ros-humble-desktop \
    python3-colcon-common-extensions \
    python3-rosdep
```

## 🏗️ 项目结构

```
ros2_ws/
├── src/
│   └── panda_description/
│       ├── CMakeLists.txt
│       ├── package.xml
│       ├── launch/
│       │   └── view_panda.launch.py       # ROS 2 launch 文件
│       ├── urdf/
│       │   └── panda.urdf                 # URDF 机器人模型
│       └── meshes/
│           ├── collision/                 # 碰撞网格（OBJ 格式）
│           └── visual/                    # 可视化网格（DAE 格式）
├── install/                               # 安装目录
├── build/                                 # 构建目录
├── log/                                   # 日志目录
└── run_panda.sh                           # 快速启动脚本
```

## 🔨 构建

```bash
# 进入工作区
cd ros2_ws

# 构建所有包
colcon build

# 或只构建 panda_description 包
colcon build --packages-select panda_description
```

## 🚀 运行

### 方法 1：使用启动脚本（推荐）

```bash
cd ros2_ws
./run_panda.sh
```

### 方法 2：手动启动

```bash
cd ros2_ws
source install/setup.bash
ros2 launch panda_description view_panda.launch.py
```

### 方法 3：单独启动各个节点

```bash
# 终端 1：启动 robot_state_publisher
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description="$(cat src/panda_description/urdf/panda.urdf)"

# 终端 2：启动 joint_state_publisher
source install/setup.bash
ros2 run joint_state_publisher joint_state_publisher

# 终端 3：启动 RViz2
source install/setup.bash
ros2 run rviz2 rviz2
```

## 📊 可视化

启动后，RViz2 会自动打开显示机器人模型。你可以：

- **查看机器人**：机器人会在 RViz2 窗口中显示
- **发布关节状态**：joint_state_publisher 会发布随机关节值
- **监控 TF 树**：robot_state_publisher 发布所有变换

### 在 RViz2 中添加 RobotModel 显示（如果未自动加载）

1. 点击左下角的 `Add`
2. 选择 `RobotModel`
3. 在参数中设置 `Topic` 为 `/tf` 或 `Fixed Frame` 为 `panda_link0`

## 🎮 控制机器人

有三种主要的方式来控制 Panda 机器人的关节：

### 1. **GUI 方式（推荐）** 🎨

使用图形界面滑块控制所有关节：

```bash
source install/setup.bash
ros2 launch panda_description view_panda_gui.launch.py
```

### 2. **Python 脚本方式** 🐍

运行命令行脚本来设置预定义的位置：

```bash
source install/setup.bash
python3 src/panda_description/scripts/panda_joint_controller.py home    # 初始位置
python3 src/panda_description/scripts/panda_joint_controller.py ready   # 准备位置
python3 src/panda_description/scripts/panda_joint_controller.py stretch # 伸展位置
python3 src/panda_description/scripts/panda_joint_controller.py open    # 打开夹爪
python3 src/panda_description/scripts/panda_joint_controller.py close   # 关闭夹爪
```

### 3. **Jupyter Notebook 方式** 📓

交互式 notebook 与实时滑块控制：

```bash
source install/setup.bash
jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb
```

**详见 [完整控制指南](CONTROL_GUIDE.md)** 📖

### 发布关节状态（高级）

```bash
source install/setup.bash
ros2 topic pub -1 /joint_states sensor_msgs/msg/JointState \
    "{header: {stamp: {sec: 0, nanosec: 0}, frame_id: ''}, \
    name: ['panda_joint1', 'panda_joint2'], \
    position: [0.5, -0.5], \
    velocity: [], \
    effort: []}"
```

### 查看可用的话题

```bash
ros2 topic list
```

### 查看 TF 树

```bash
ros2 run tf2_tools view_frames
```

## 📝 配置

### 修改 URDF 模型

URDF 文件位于 `src/panda_description/urdf/panda.urdf`。修改后重新构建：

```bash
colcon build --packages-select panda_description
source install/setup.bash
```

### 修改网格文件

网格文件位于 `src/panda_description/meshes/`：
- `collision/` - 碰撞检测用的低多边形网格（OBJ 格式）
- `visual/` - 可视化显示用的高质量网格（DAE 格式）

## 🐛 故障排除

### RViz2 不显示机器人

1. 检查 `/robot_description` 话题是否有数据：
   ```bash
   ros2 topic echo /robot_description | head -20
   ```

2. 检查 `/joint_states` 话题是否有数据：
   ```bash
   ros2 topic echo /joint_states
   ```

3. 检查 TF 广播：
   ```bash
   ros2 topic echo /tf
   ```

### 找不到网格文件

确保网格文件存在：
```bash
ls -la src/panda_description/meshes/visual/
```

如果缺少文件，重新复制：
```bash
cp -r ../deps/Panda/meshes/* src/panda_description/meshes/
```

## 📚 相关资源

- [ROS 2 官方文档](https://docs.ros.org/en/humble/)
- [URDF 教程](http://wiki.ros.org/urdf/Tutorials)
- [RViz2 使用指南](https://github.com/ros2/rviz/wiki/User-Guide)

## 📄 许可证

Apache License 2.0 - 详见 LICENSE.md

## 👨‍💻 开发指南

### 添加新的 ROS 2 节点

1. 在 `src/` 中创建新包：
   ```bash
   cd src
   ros2 pkg create --build-type ament_cmake my_package
   ```

2. 在 `launch/` 文件中添加节点

3. 重新构建：
   ```bash
   cd ..
   colcon build
   ```

### 调试技巧

```bash
# 详细输出
colcon build --packages-select panda_description --cmake-args -DCMAKE_BUILD_TYPE=Debug

# 查看日志
colcon build --packages-select panda_description --event-handlers console_direct+

# 清除构建
colcon clean packages --select panda_description
```

## 🤝 贡献

欢迎提交问题和拉取请求！

---

**最后更新**: 2025-12-04
