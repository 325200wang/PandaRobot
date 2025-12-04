# 🎯 Panda 机器人控制方法总结

## 📋 总览

你现在有 **3 种主要方式** 来控制 Panda 机器人的关节，每种方式都有不同的优势：

| 方法 | 启动命令 | 优点 | 缺点 | 难度 |
|------|---------|------|------|------|
| **GUI 滑块** | `ros2 launch panda_description view_panda_gui.launch.py` | 直观、实时、交互式 | 需要 X11 显示环境 | ⭐ 简单 |
| **Python 脚本** | `python3 panda_joint_controller.py <cmd>` | 快速、可脚本化、易自动化 | 只有预设位置 | ⭐⭐ 中等 |
| **Jupyter Notebook** | `jupyter notebook panda_control_interactive.ipynb` | 可编程、教育友好、文档齐全 | 需要 Jupyter 环境 | ⭐⭐ 中等 |

---

## 🎮 方法 1：GUI 滑块控制

### 启动

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
ros2 launch panda_description view_panda_gui.launch.py
```

### 效果

同时打开：
- **RViz2 窗口**：显示 3D 机器人模型
- **joint_state_publisher_gui 窗口**：显示所有关节的滑块

### 使用

1. 拖动任意滑块即可控制对应关节
2. 机器人在 RViz2 中实时运动
3. 滑块显示当前角度（度数和弧度）

### 特点

✅ **优点：**
- 直观的图形界面
- 实时视觉反馈
- 无需编写代码
- 适合初学者

❌ **缺点：**
- 需要 X11 显示环境
- 每个关节需要单独调整
- 难以保存复杂的运动序列

---

## 🐍 方法 2：Python 命令行脚本

### 文件位置

```
/media/dubhe/store/sim/panda/PandaRobot/ros2_ws/src/panda_description/scripts/panda_joint_controller.py
```

### 可用命令

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash

# 1. 初始位置（所有关节 0°）
python3 src/panda_description/scripts/panda_joint_controller.py home

# 2. 准备位置（标准姿态）
python3 src/panda_description/scripts/panda_joint_controller.py ready

# 3. 伸展位置（手臂伸开）
python3 src/panda_description/scripts/panda_joint_controller.py stretch

# 4. 打开夹爪（默认宽度 0.04m）
python3 src/panda_description/scripts/panda_joint_controller.py open

# 5. 打开夹爪（自定义宽度）
python3 src/panda_description/scripts/panda_joint_controller.py open 0.08

# 6. 关闭夹爪
python3 src/panda_description/scripts/panda_joint_controller.py close
```

### 编程使用

在你自己的 Python 脚本中导入并使用控制器：

```python
#!/usr/bin/env python3
import rclpy
import math
from src.panda_description.scripts.panda_joint_controller import PandaJointController

rclpy.init()
controller = PandaJointController()

# 示例 1：设置单个关节
controller.publish_joint_state({
    'panda_joint1': math.radians(45),
})

# 示例 2：设置多个关节
controller.publish_joint_state({
    'panda_joint1': math.radians(30),
    'panda_joint2': math.radians(-45),
    'panda_joint3': math.radians(60),
})

# 示例 3：控制夹爪
controller.open_gripper(0.04)
controller.close_gripper()

rclpy.shutdown()
```

### 脚本编写示例

创建 `my_sequence.py`：

```python
#!/usr/bin/env python3
import rclpy
import math
import time
import sys
sys.path.insert(0, 'src/panda_description/scripts')

from panda_joint_controller import PandaJointController

rclpy.init()
controller = PandaJointController()

# 动作序列
print("🤖 执行动作序列...")

print("1️⃣ 回到初始位置...")
controller.set_home()
time.sleep(1)

print("2️⃣ 设置准备位置...")
controller.set_ready()
time.sleep(1)

print("3️⃣ 打开夹爪...")
controller.open_gripper()
time.sleep(1)

print("4️⃣ 关闭夹爪...")
controller.close_gripper()
time.sleep(1)

print("5️⃣ 伸展手臂...")
controller.set_stretch()
time.sleep(1)

print("✅ 序列执行完成！")
rclpy.shutdown()
```

运行：
```bash
python3 my_sequence.py
```

### 特点

✅ **优点：**
- 快速执行
- 易于自动化
- 可编写复杂的动作序列
- 适合脚本和集成

❌ **缺点：**
- 只有几个预设位置
- 需要知道 Python 和 ROS 2 基础
- 不如 GUI 直观

---

## 📓 方法 3：Jupyter 交互式控制

### 文件位置

```
/media/dubhe/store/sim/panda/PandaRobot/ros2_ws/src/panda_description/notebooks/panda_control_interactive.ipynb
```

### 启动

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws

# 确保已安装 Jupyter 和 ipywidgets
pip install jupyter ipywidgets

# 启动 Notebook
source install/setup.bash
jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb
```

### 功能

1. **ROS 2 初始化**：自动初始化 ROS 2 环境
2. **控制器创建**：创建 PandaController 实例
3. **交互式滑块**：为每个关节创建滑块
4. **实时显示**：显示当前角度（度数和弧度）
5. **预设位置**：快速按钮设置常用姿态
6. **夹爪控制**：打开/关闭夹爪按钮
7. **自定义代码**：在专用单元格编写自己的控制代码

### Notebook 工作流程

1. **第 1 单元格**：导入库和初始化 ROS 2
2. **第 2 单元格**：创建控制器类
3. **第 3 单元格**：创建交互式滑块
4. **第 4 单元格**：绑定滑块事件处理器
5. **第 5 单元格**：显示预设位置按钮
6. **第 6+ 单元格**：自定义代码区域

### 在 Notebook 中编写代码示例

在最后的测试单元格中尝试：

```python
# 移动单个关节
controller.publish_joint_state({
    'panda_joint1': math.radians(45)
})

# 循环运动
import time
for angle in [0, 30, 60, 30, 0]:
    controller.publish_joint_state({
        'panda_joint1': math.radians(angle)
    })
    time.sleep(0.5)

# 复杂动作
controller.set_ready()
time.sleep(1)
controller.open_gripper(0.04)
time.sleep(1)
controller.close_gripper()
```

### 特点

✅ **优点：**
- 交互式实验环境
- 文档和代码在一起
- 易于学习和理解
- 实时反馈
- 可重复使用和修改

❌ **缺点：**
- 需要 Jupyter 环境
- 需要在浏览器中操作
- 稍微复杂的启动流程

---

## 🔄 多方法组合使用

你可以同时运行多个控制方法！例如：

**终端 1**：启动机器人
```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
./run_panda.sh
```

**终端 2**：GUI 控制
```bash
source install/setup.bash
ros2 launch panda_description view_panda_gui.launch.py
```

**终端 3**：命令行脚本
```bash
source install/setup.bash
python3 src/panda_description/scripts/panda_joint_controller.py ready
```

**终端 4**：Jupyter Notebook
```bash
source install/setup.bash
jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb
```

所有方法都会控制同一个机器人！机器人会响应最新的命令。

---

## 📊 选择指南

### 我该选择哪一个？

#### 选择 **GUI 滑块** 如果你：
- 🎨 喜欢图形界面，不想写代码
- 👀 需要直观的视觉反馈
- 📚 是初学者或不熟悉 Python
- 🔍 需要精确调整每个关节
- ✨ 想要最快上手

#### 选择 **Python 脚本** 如果你：
- ⚡ 需要快速执行预设动作
- 📝 想要编写自动化脚本
- 🔄 需要重复执行相同的动作
- 🤖 要集成到更大的应用中
- 🚀 追求最高效率

#### 选择 **Jupyter Notebook** 如果你：
- 🎓 在学习 ROS 2 和机器人编程
- 📚 需要文档和代码在一起
- 🔬 想要探索式编程和实验
- 📊 需要可视化结果和分析
- 🧮 想要计算和可视化支持

---

## 🔧 常见任务速查表

### 设置特定的关节角度

**GUI 方式**：拖动对应的滑块

**Python 方式**：
```python
import math
controller.publish_joint_state({
    'panda_joint1': math.radians(45),
})
```

**Jupyter 方式**：拖动对应滑块或在代码单元格中运行

### 执行运动序列

**Python 脚本**：
```python
for angle in [0, 30, 60, 30, 0]:
    controller.publish_joint_state({'panda_joint1': math.radians(angle)})
    time.sleep(1)
```

**Jupyter**：在单元格中运行相同代码

### 保存和重复动作

**推荐使用 Python 脚本**，保存为 `.py` 文件后可重复运行

---

## 📚 相关文档

- 📖 [完整控制指南](CONTROL_GUIDE.md) - 详细的教程和高级用法
- 🚀 [快速开始](QUICK_CONTROL_START.md) - 5 分钟快速入门
- 📋 [README](README.md) - 项目概览
- 🔍 [OVERVIEW](OVERVIEW.md) - 项目结构和文件说明

---

## 💡 提示

1. **先用 GUI 探索**：使用 GUI 了解机器人的运动方式
2. **再用脚本自动化**：找到喜欢的姿态后，用脚本保存和重复
3. **最后用 Notebook 优化**：使用 Notebook 进行详细的参数调整

---

**祝你使用愉快！** 🎉

有任何问题，请查看故障排除部分或参考完整文档。
