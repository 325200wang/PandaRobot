# 🚀 快速开始 - 控制 Panda 机器人

本文档介绍如何在最短时间内开始控制 Panda 机器人。

## ⚡ 5 秒快速开始

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
./run_panda.sh
```

然后在另一个终端：

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
python3 src/panda_description/scripts/panda_joint_controller.py ready
```

✅ 完成！机器人会摆动到 "准备" 位置。

---

## 方法 A: GUI 控制（最简单）⭐

如果你想要交互式滑块界面：

```bash
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
source install/setup.bash
ros2 launch panda_description view_panda_gui.launch.py
```

**会打开两个窗口：**
- RViz2：显示机器人
- GUI 窗口：显示所有关节的滑块

**操作：**
1. 拖动任意滑块
2. 实时看到机器人在 RViz2 中运动

---

## 方法 B: 命令行控制（最快）🚀

```bash
# 终端 1：启动机器人
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
./run_panda.sh

# 终端 2：执行命令
source install/setup.bash

# 初始位置（所有关节 0°）
python3 src/panda_description/scripts/panda_joint_controller.py home

# 准备位置（标准姿态）
python3 src/panda_description/scripts/panda_joint_controller.py ready

# 伸展位置（手臂伸开）
python3 src/panda_description/scripts/panda_joint_controller.py stretch

# 打开夹爪
python3 src/panda_description/scripts/panda_joint_controller.py open

# 关闭夹爪
python3 src/panda_description/scripts/panda_joint_controller.py close
```

---

## 方法 C: Jupyter 交互式控制（最好玩）🎮

```bash
# 终端 1：启动机器人
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws
./run_panda.sh

# 终端 2：启动 Jupyter
source install/setup.bash
pip install jupyter ipywidgets
jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb
```

**特点：**
- 实时滑块调整
- 实时角度显示
- 预设位置按钮
- 可编程控制

---

## 常见命令对照表

| 任务 | 命令 |
|------|------|
| 快速启动 | `./run_panda.sh` |
| GUI 控制 | `ros2 launch panda_description view_panda_gui.launch.py` |
| 命令行控制 | `python3 src/panda_description/scripts/panda_joint_controller.py <cmd>` |
| Jupyter 控制 | `jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb` |
| 初始位置 | `python3 ... panda_joint_controller.py home` |
| 准备位置 | `python3 ... panda_joint_controller.py ready` |
| 伸展位置 | `python3 ... panda_joint_controller.py stretch` |
| 打开夹爪 | `python3 ... panda_joint_controller.py open` |
| 关闭夹爪 | `python3 ... panda_joint_controller.py close` |

---

## 💡 我该选择哪种方法？

### 选择 GUI 方式如果你：
- 🎨 喜欢图形界面
- 👀 需要直观的视觉反馈
- 📊 想要精确控制每个关节

### 选择命令行方式如果你：
- ⚡ 需要快速设置
- 📝 喜欢编写脚本
- 🔄 要自动化重复操作

### 选择 Jupyter 方式如果你：
- 🎓 在学习 ROS 2
- 📚 需要文档和代码示例
- 🔬 想要探索式编程

---

## 🔧 常见问题

### Q: 机器人不动？

A: 检查这些步骤：

```bash
# 1. 确保 ROS 2 环境正确初始化
source install/setup.bash

# 2. 检查 joint_states 话题是否有数据
ros2 topic echo /joint_states

# 3. 查看所有正在运行的节点
ros2 node list
```

### Q: 哪个方法最简单？

A: **GUI 方式最简单** - 一个命令启动，拖动滑块即可。

### Q: 我能同时运行多个方法吗？

A: **是的！** 在不同的终端中同时运行多个控制方法。机器人会响应最新的命令。

### Q: 怎样设置自定义位置？

A: 在 Python 代码中直接调用：

```python
from src.panda_description.scripts.panda_joint_controller import PandaJointController
import math

controller = PandaJointController()
controller.publish_joint_state({
    'panda_joint1': math.radians(45),
    'panda_joint2': math.radians(-30),
})
```

---

## 📚 下一步

- 👉 查看 [完整控制指南](CONTROL_GUIDE.md) 了解高级用法
- 👉 阅读 [OVERVIEW.md](OVERVIEW.md) 理解项目结构
- 👉 查看 [BUGFIX_REPORT.md](BUGFIX_REPORT.md) 了解已修复的问题

---

**祝你使用愉快！** 🎉
