# 🚀 快速开始指南 - Franka Emika Panda Robot ROS 2 可视化

## ⚡ 最快的启动方式（3 步）

### 第 1 步：打开终端

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
```

### 第 2 步：运行启动脚本

```bash
./run_panda.sh
```

### 第 3 步：等待 RViz2 打开

你应该看到：
- ✅ RViz2 窗口打开
- ✅ Panda 机器人模型显示
- ✅ 机器人的所有关节和链接可见

---

## 📚 详细使用说明

### 方式 A：使用启动脚本（推荐 ⭐）

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
./run_panda.sh
```

**优点**：
- 一键启动所有组件
- 自动配置环境
- 显示清晰的启动消息

---

### 方式 B：手动启动

```bash
# 进入工作区
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws

# Source ROS 2 和本地环境
source /opt/ros/humble/setup.bash
source install/setup.bash

# 启动 ROS 2 launch 文件
ros2 launch panda_description view_panda.launch.py
```

---

### 方式 C：启动单个节点（高级）

如果你想单独启动各个组件，可以在不同的终端中运行：

**终端 1 - 启动 Robot State Publisher**：
```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run robot_state_publisher robot_state_publisher --ros-args \
  -p robot_description="$(cat src/panda_description/urdf/panda.urdf)"
```

**终端 2 - 启动 Joint State Publisher**：
```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run joint_state_publisher joint_state_publisher
```

**终端 3 - 启动 RViz2**：
```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run rviz2 rviz2
```

---

## 🎯 主要功能

| 功能 | 描述 |
|------|------|
| **Robot State Publisher** | 读取 URDF 并发布机器人状态，提供 TF 变换 |
| **Joint State Publisher** | 发布关节状态（位置、速度、力矩） |
| **RViz2** | 3D 可视化工具，显示机器人模型和坐标系 |

---

## 🔧 常见操作

### 查看机器人的所有关节

```bash
source install/setup.bash
ros2 topic echo /joint_states
```

输出示例：
```
header:
  stamp:
    sec: 123456
    nanosec: 789012
  frame_id: ''
name:
- panda_joint1
- panda_joint2
- panda_joint3
- panda_joint4
- panda_joint5
- panda_joint6
- panda_joint7
- panda_hand_joint
position: [0.123, -0.456, 0.789, ...]
velocity: []
effort: []
```

### 查看 TF 树（坐标变换关系）

```bash
source install/setup.bash
ros2 run tf2_tools view_frames
file panda_frames.pdf  # 查看生成的 PDF
```

### 发布自定义关节状态

```bash
source install/setup.bash
ros2 topic pub -1 /joint_states sensor_msgs/msg/JointState \
  "{header: {stamp: {sec: 0, nanosec: 0}, frame_id: ''}, \
    name: ['panda_joint1'], \
    position: [1.57], \
    velocity: [], \
    effort: []}"
```

### 列出所有可用的 ROS 2 话题

```bash
source install/setup.bash
ros2 topic list
```

---

## 🐛 问题排除

### ❌ RViz2 启动后立即关闭

**原因**：通常是因为 GUI 环境问题

**解决方案**：
```bash
# 检查 DISPLAY 环境变量
echo $DISPLAY

# 如果为空，设置 DISPLAY
export DISPLAY=:1
./run_panda.sh
```

### ❌ 看不到机器人模型

**原因**：可能是网格文件未正确加载

**解决方案**：
1. 检查网格文件是否存在：
   ```bash
   ls -la src/panda_description/meshes/visual/
   ```

2. 在 RViz2 中手动添加 RobotModel：
   - 点击 `Add` 按钮
   - 选择 `RobotModel`
   - 设置 `Topic` 为 `/tf`

### ❌ 找不到 `panda_description` 包

**原因**：环境未正确 source

**解决方案**：
```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch panda_description view_panda.launch.py
```

---

## 📊 文件结构说明

```
ros2_ws/
├── src/panda_description/
│   ├── CMakeLists.txt          ← ROS 2 构建配置
│   ├── package.xml             ← 包元数据
│   ├── launch/
│   │   └── view_panda.launch.py   ← 启动文件（定义启动流程）
│   ├── urdf/
│   │   └── panda.urdf          ← 机器人模型定义
│   └── meshes/
│       ├── collision/          ← 碰撞检测网格
│       └── visual/             ← 显示用网格（已修复为 DAE 格式）
├── build/                       ← 构建输出（自动生成）
├── install/                     ← 安装文件（自动生成）
├── run_panda.sh                ← 启动脚本 ⭐
└── README.md                   ← 详细文档
```

---

## 💡 进阶使用

### 重新构建包

如果你修改了 URDF 或网格文件：

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
colcon build --packages-select panda_description
source install/setup.bash
./run_panda.sh
```

### 查看构建日志

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
colcon build --packages-select panda_description --event-handlers console_direct+
```

### 清除构建缓存

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
colcon clean packages --select panda_description
colcon build --packages-select panda_description
```

---

## 🎨 RViz2 可视化配置

### ✨ 新特性：自动加载机器人模型

从最新版本开始，启动 RViz2 时会**自动加载并显示 Panda 机器人**，无需手动配置！

**自动配置包括**：
- ✅ RobotModel 显示已启用
- ✅ Fixed Frame 设置为 `panda_link0`
- ✅ 所有 12 个 link 已配置
- ✅ 网格显示已启用
- ✅ 最优视角预设

### 如果需要自定义配置

配置文件位于：`src/panda_description/launch/panda.rviz`

你可以：
1. 在 RViz2 中进行调整
2. 通过 `File → Save Config As` 保存更改
3. 或直接编辑 `panda.rviz` 文件

---

## 📞 获取帮助

- 查看完整文档：`README.md`
- ROS 2 官方文档：https://docs.ros.org/en/humble/
- URDF 教程：http://wiki.ros.org/urdf/Tutorials

---

**祝你使用愉快！** 🤖✨
