# 🎮 Panda Robot 关节控制指南

## 概述

本指南介绍如何通过多种方式控制 Panda 机器人的关节，并在 RViz2 中实时查看效果。

有三种主要的控制方法：

1. **GUI 方式（推荐）**：使用 joint_state_publisher_gui
2. **命令行方式**：使用 Python 脚本
3. **交互式方式**：使用 Jupyter Notebook

---

## 方法 1️⃣：GUI 方式（最简单）

### 启动 GUI 控制界面

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
ros2 launch panda_description view_panda_gui.launch.py
```

### 效果

启动后会同时打开：
- ✅ **RViz2**：显示 3D 机器人模型
- ✅ **GUI 窗口**：显示所有关节的滑块

### 使用方法

1. **拖动滑块**：改变关节角度
   - 左键按住滑块并拖动
   - 实时看到机器人在 RViz2 中运动

2. **查看角度值**：
   - 滑块下方显示当前角度（度数和弧度）

3. **快速复位**：
   - 点击滑块两端快速设置为最小/最大值
   - 点击中间快速回到 0°

### 关节范围

| 关节 | 最小值 | 最大值 | 说明 |
|------|--------|--------|------|
| panda_joint1 | -165° | +165° | 底部旋转关节 |
| panda_joint2 | -101° | +101° | 肩关节 |
| panda_joint3 | -165° | +165° | 上臂关节 |
| panda_joint4 | -176° | -4° | 肘关节 |
| panda_joint5 | -165° | +165° | 前臂关节 |
| panda_joint6 | -1° | +215° | 腕关节 1 |
| panda_joint7 | -165° | +165° | 腕关节 2 |
| panda_hand_joint | 0° | 2.3° | 手部关节 |
| leftfinger_joint | 0° | 0.04 m | 左夹爪 |
| rightfinger_joint | 0° | 0.04 m | 右夹爪 |

---

## 方法 2️⃣：命令行方式（通过 Python 脚本）

### 启动机器人

首先在一个终端中启动机器人（不带 GUI）：

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
ros2 launch panda_description view_panda.launch.py
```

### 在另一个终端中运行控制脚本

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
python3 src/panda_description/scripts/panda_joint_controller.py <command>
```

### 可用命令

#### 1. 回到初始位置

```bash
python3 src/panda_description/scripts/panda_joint_controller.py home
```

所有关节都设置为 0°

#### 2. 设置准备位置

```bash
python3 src/panda_description/scripts/panda_joint_controller.py ready
```

这是一个标准的机器人准备姿态

#### 3. 设置伸展位置

```bash
python3 src/panda_description/scripts/panda_joint_controller.py stretch
```

机器人手臂伸展开来

#### 4. 打开夹爪

```bash
# 默认宽度 0.04 m
python3 src/panda_description/scripts/panda_joint_controller.py open

# 自定义宽度（米）
python3 src/panda_description/scripts/panda_joint_controller.py open 0.08
```

#### 5. 关闭夹爪

```bash
python3 src/panda_description/scripts/panda_joint_controller.py close
```

### 在 Python 代码中使用

创建 `my_control.py` 文件：

```python
#!/usr/bin/env python3
import rclpy
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src/panda_description/scripts'))

from panda_joint_controller import PandaJointController
import math

rclpy.init()
controller = PandaJointController()

# 例子 1：设置单个关节
controller.publish_joint_state({
    'panda_joint1': math.radians(45),    # 关节1 设置为 45°
})

# 例子 2：设置多个关节
controller.publish_joint_state({
    'panda_joint1': math.radians(30),
    'panda_joint2': math.radians(-45),
    'panda_joint3': math.radians(0),
    'panda_joint4': math.radians(-90),
})

# 例子 3：打开夹爪
controller.open_gripper(0.04)

# 例子 4：关闭夹爪
controller.close_gripper()

rclpy.shutdown()
```

运行：

```bash
python3 my_control.py
```

---

## 方法 3️⃣：交互式方式（Jupyter Notebook）

### 前置条件

```bash
pip install jupyter ipywidgets
```

### 启动 Notebook

```bash
# 首先启动机器人（在第一个终端）
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
ros2 launch panda_description view_panda.launch.py

# 在第二个终端启动 Jupyter
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb
```

### 功能

- 🎨 **可视化滑块**：用交互式滑块控制每个关节
- ⚡ **实时反馈**：显示当前角度（度数和弧度）
- 🎯 **预设位置**：快速按钮设置常用位置
- 🤲 **夹爪控制**：打开/关闭夹爪按钮
- 📊 **高级编程**：在单元格中编写 Python 代码

### Notebook 使用流程

1. 运行第一个单元格初始化 ROS 2
2. 运行第二个单元格创建控制器
3. 运行后续单元格使用不同的控制方式
4. 拖动滑块或点击按钮控制机器人

---

## 📊 ROS 2 话题方式（高级）

如果你想用自己的节点发布关节状态，可以直接发布到 `/joint_states` 话题：

### 命令行发布（快速测试）

```bash
ros2 topic pub -1 /joint_states sensor_msgs/msg/JointState \
  "{header: {stamp: {sec: 0, nanosec: 0}, frame_id: ''}, \
    name: ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7', 'panda_hand_joint', 'panda_leftfinger_joint', 'panda_rightfinger_joint'], \
    position: [0.5, -0.7, 0.3, -1.5, 0.2, 1.5, 0.0, 0.0, 0.0, 0.0], \
    velocity: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    effort: []}"
```

### Python 节点示例

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import math

class MyController(Node):
    def __init__(self):
        super().__init__('my_panda_controller')
        self.publisher = self.create_publisher(JointState, '/joint_states', 10)
    
    def publish(self):
        msg = JointState()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [
            'panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4',
            'panda_joint5', 'panda_joint6', 'panda_joint7', 'panda_hand_joint',
            'panda_leftfinger_joint', 'panda_rightfinger_joint'
        ]
        msg.position = [
            0.5,    # joint1
            -0.7,   # joint2
            0.3,    # joint3
            -1.5,   # joint4
            0.2,    # joint5
            1.5,    # joint6
            0.0,    # joint7
            0.0,    # hand
            0.0,    # left finger
            0.0,    # right finger
        ]
        msg.velocity = [0.0] * 10
        msg.effort = []
        
        self.publisher.publish(msg)

if __name__ == '__main__':
    rclpy.init()
    controller = MyController()
    controller.publish()
    rclpy.shutdown()
```

---

## 🔧 故障排除

### Q: GUI 窗口不显示？
A: 确保有 X11 显示环境：
```bash
echo $DISPLAY
# 如果为空，设置
export DISPLAY=:1
```

### Q: 关节不动？
A: 检查话题是否正确发布：
```bash
# 监听 joint_states 话题
ros2 topic echo /joint_states

# 检查 robot_state_publisher 是否运行
ros2 node list
```

### Q: 角度超出范围？
A: GUI 和脚本都会自动限制在有效范围内，无需手动调整

### Q: Jupyter Notebook 报错？
A: 确保已源代码环境：
```bash
source install/setup.bash
pip install jupyter ipywidgets
```

---

## 📚 关节信息参考

### 关节类型

- **旋转关节**（Revolute）：panda_joint1-7, panda_hand_joint
- **棱柱关节**（Prismatic）：panda_leftfinger_joint, panda_rightfinger_joint

### 坐标系

- **X 轴**：向前
- **Y 轴**：向左
- **Z 轴**：向上

### 角度单位

- 脚本和 ROS 使用**弧度**（radians）
- GUI 显示**度数**（degrees）
- 转换公式：`degrees = radians * 180 / π`

---

## 🎯 常用控制模式

### 模式 1：逐步调整（Fine Tuning）

```python
# 小幅度调整关节
import math
controller.publish_joint_state({
    'panda_joint1': math.radians(5),   # 5° 偏移
})
```

### 模式 2：同时多关节运动

```python
# 多个关节同时运动
controller.publish_joint_state({
    'panda_joint1': math.radians(30),
    'panda_joint2': math.radians(-45),
    'panda_joint3': math.radians(60),
    'panda_joint4': math.radians(-90),
    'panda_joint5': math.radians(30),
    'panda_joint6': math.radians(45),
    'panda_joint7': math.radians(0),
})
```

### 模式 3：动画序列

```python
# 循环执行多个位置
import time

positions = [
    {'panda_joint1': 0.0},
    {'panda_joint1': math.radians(45)},
    {'panda_joint1': math.radians(90)},
    {'panda_joint1': 0.0},
]

for pos in positions:
    controller.publish_joint_state(pos)
    time.sleep(1)  # 每个位置停留 1 秒
```

---

## 💡 提示和技巧

1. **保存配置**：在 Jupyter 中找到喜欢的位置后，记录下滑块的值

2. **组合命令**：使用 shell 脚本自动运行多个命令
   ```bash
   #!/bin/bash
   python3 panda_joint_controller.py ready
   sleep 2
   python3 panda_joint_controller.py open
   sleep 1
   python3 panda_joint_controller.py close
   ```

3. **监控运动**：在 RViz2 中添加"Joint State Publisher"显示来查看实时更新

4. **安全操作**：始终确保没有物理障碍物阻挡机器人的运动路径

---

**祝你使用愉快！** 🚀
