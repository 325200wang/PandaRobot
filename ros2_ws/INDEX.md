# 📚 Panda 机器人文档索引

欢迎使用 Franka Emika Panda 机器人 ROS 2 工作区！

本文件帮助你快速找到所需的文档和工具。

---

## 🎯 快速导航

### 🚀 我想快速开始

👉 **阅读**: [QUICK_CONTROL_START.md](QUICK_CONTROL_START.md) (5 分钟)

包含：
- ⚡ 最快启动方式
- 🎮 三种控制方法对比
- 📋 常见命令速查表

---

### 🎮 我想学习不同的控制方法

👉 **阅读**: [CONTROL_METHODS.md](CONTROL_METHODS.md) (10 分钟)

包含：
- 📊 三种方法详细对比表
- 🔄 每种方法的优缺点
- 💡 如何选择合适的方法
- 🔧 常见任务速查表

---

### 📖 我想详细学习所有功能

👉 **阅读**: [CONTROL_GUIDE.md](CONTROL_GUIDE.md) (20 分钟)

包含：
- 🎨 GUI 滑块详细教程
- 🐍 Python 脚本完整指南
- 📓 Jupyter Notebook 使用方法
- 📚 高级编程示例
- 🔧 故障排除

---

### 📋 我想了解项目结构

👉 **阅读**: [README.md](README.md) (10 分钟)

包含：
- 🏗️ 项目结构
- 🔨 构建和运行方式
- 📊 可视化设置
- 🐛 故障排除
- 👨‍💻 开发指南

---

### 🔍 我想了解项目详情

👉 **阅读**: [OVERVIEW.md](OVERVIEW.md) (15 分钟)

包含：
- 📦 工作区结构详解
- 📄 所有文件说明
- 🔗 文件之间的关系
- 🎯 每个文件的用途

---

### 🐛 我遇到了问题

👉 **阅读**: [BUGFIX_REPORT.md](BUGFIX_REPORT.md) (10 分钟)

包含：
- ❌ 已知问题和解决方案
- 🔧 常见错误信息
- 💡 故障排除步骤
- ✅ 验证修复的方法

---

### 📝 我想了解最近的更新

👉 **阅读**: [CHANGELOG.md](CHANGELOG.md) (5 分钟)

包含：
- 📅 版本历史
- ✨ 新增功能
- 🐛 修复的问题
- 🔄 改进内容

---

## 🎮 控制工具位置

### GUI 滑块控制

**启动**：
```bash
cd ros2_ws
source install/setup.bash
ros2 launch panda_description view_panda_gui.launch.py
```

**文件**：
```
src/panda_description/launch/view_panda_gui.launch.py
```

---

### Python 脚本控制

**运行**：
```bash
source install/setup.bash
python3 src/panda_description/scripts/panda_joint_controller.py <command>
```

**文件**：
```
src/panda_description/scripts/panda_joint_controller.py
```

**可用命令**：
- `home` - 初始位置
- `ready` - 准备位置
- `stretch` - 伸展位置
- `open [width]` - 打开夹爪
- `close` - 关闭夹爪

---

### Jupyter Notebook 交互控制

**启动**：
```bash
pip install jupyter ipywidgets
source install/setup.bash
jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb
```

**文件**：
```
src/panda_description/notebooks/panda_control_interactive.ipynb
```

---

## 📊 文档速查表

| 文档 | 用途 | 阅读时间 | 适合人群 |
|------|------|----------|----------|
| QUICK_CONTROL_START.md | 快速开始 | 5 分钟 | 所有用户 |
| CONTROL_METHODS.md | 方法对比 | 10 分钟 | 初学者 |
| CONTROL_GUIDE.md | 详细教程 | 20 分钟 | 中级用户 |
| README.md | 项目概览 | 10 分钟 | 开发者 |
| OVERVIEW.md | 结构详解 | 15 分钟 | 开发者 |
| BUGFIX_REPORT.md | 问题解决 | 10 分钟 | 遇到问题时 |
| CHANGELOG.md | 更新历史 | 5 分钟 | 追踪更新 |

---

## 🎯 按用户角色推荐

### 👨‍🎓 学生/初学者

**推荐流程**：
1. 阅读 [QUICK_CONTROL_START.md](QUICK_CONTROL_START.md) - 了解基础
2. 尝试 GUI 滑块控制 - 学习机器人运动
3. 阅读 [CONTROL_METHODS.md](CONTROL_METHODS.md) - 了解不同方法
4. 尝试 Jupyter Notebook - 互动学习
5. 阅读 [CONTROL_GUIDE.md](CONTROL_GUIDE.md) - 深入学习

---

### 👨‍💼 研究员/工程师

**推荐流程**：
1. 阅读 [README.md](README.md) - 了解项目结构
2. 阅读 [OVERVIEW.md](OVERVIEW.md) - 了解实现细节
3. 使用 Python 脚本控制 - 集成到研究项目
4. 参考 [CONTROL_GUIDE.md](CONTROL_GUIDE.md) - 高级用法
5. 根据需要修改 URDF 和脚本

---

### 👨‍💻 开发者

**推荐流程**：
1. 阅读 [OVERVIEW.md](OVERVIEW.md) - 理解架构
2. 浏览源代码 - 查看实现
3. 阅读 [README.md](README.md) - 开发指南
4. 修改脚本或创建新功能
5. 参考 [CHANGELOG.md](CHANGELOG.md) - 跟踪变更

---

## 🔧 快速命令参考

```bash
# 进入工作区
cd /media/dubhe/store/sim/panda/PandaRobot/ros2_ws

# 一键启动（推荐）
./run_panda.sh

# 手动启动主程序
source install/setup.bash
ros2 launch panda_description view_panda.launch.py

# 启动 GUI 控制
source install/setup.bash
ros2 launch panda_description view_panda_gui.launch.py

# 运行 Python 脚本
source install/setup.bash
python3 src/panda_description/scripts/panda_joint_controller.py home

# 启动 Jupyter Notebook
source install/setup.bash
jupyter notebook src/panda_description/notebooks/panda_control_interactive.ipynb

# 查看节点列表
ros2 node list

# 查看话题列表
ros2 topic list

# 监听 joint_states 话题
ros2 topic echo /joint_states

# 重新构建
colcon build --packages-select panda_description
```

---

## 💡 常见问题速答

### Q: 我该从哪里开始？
A: 👉 阅读 [QUICK_CONTROL_START.md](QUICK_CONTROL_START.md)

### Q: 如何控制机器人？
A: 👉 有三种方式，详见 [CONTROL_METHODS.md](CONTROL_METHODS.md)

### Q: 机器人不动怎么办？
A: 👉 查看 [BUGFIX_REPORT.md](BUGFIX_REPORT.md) 的故障排除部分

### Q: 文件在哪里？
A: 👉 查看 [OVERVIEW.md](OVERVIEW.md) 的项目结构部分

### Q: 我想修改机器人模型？
A: 👉 查看 [README.md](README.md) 的开发指南部分

---

## 📂 完整文件清单

```
ros2_ws/
├── 📖 文档文件
│   ├── INDEX.md (本文件)                    # 文档索引
│   ├── QUICK_CONTROL_START.md               # 快速开始
│   ├── CONTROL_METHODS.md                   # 控制方法详解
│   ├── CONTROL_GUIDE.md                     # 控制完整指南
│   ├── README.md                            # 项目概览
│   ├── OVERVIEW.md                          # 结构详解
│   ├── BUGFIX_REPORT.md                     # 问题报告
│   ├── CHANGELOG.md                         # 更新历史
│   ├── FILE_MANIFEST.txt                    # 文件清单
│   └── QUICK_START.md                       # 基础快速开始
│
├── 🚀 启动脚本
│   └── run_panda.sh                         # 一键启动脚本
│
└── 🔧 源代码 (src/panda_description/)
    ├── 📋 配置文件
    │   ├── CMakeLists.txt                   # CMake 构建配置
    │   └── package.xml                      # ROS 2 包信息
    │
    ├── 🎯 启动文件 (launch/)
    │   ├── view_panda.launch.py             # 标准启动
    │   ├── view_panda_gui.launch.py         # GUI 启动
    │   └── panda.rviz                       # RViz 配置
    │
    ├── 🤖 机器人模型 (urdf/)
    │   └── panda.urdf                       # URDF 机器人定义
    │
    ├── 📦 网格文件 (meshes/)
    │   ├── collision/                       # 碰撞网格（OBJ）
    │   └── visual/                          # 可视化网格（DAE）
    │
    ├── 🐍 脚本文件 (scripts/)
    │   └── panda_joint_controller.py         # 关节控制脚本
    │
    └── 📓 笔记本 (notebooks/)
        └── panda_control_interactive.ipynb  # 交互式 Jupyter
```

---

## 🔗 相关链接

- [ROS 2 官方文档](https://docs.ros.org/en/humble/)
- [URDF 教程](http://wiki.ros.org/urdf/Tutorials)
- [RViz2 使用指南](https://github.com/ros2/rviz/wiki)
- [Franka Emika Panda 官网](https://www.franka.de/)

---

## 📝 最后更新

- **日期**: 2025-12-04
- **版本**: 2.0 (完整的控制系统)
- **包含**: GUI、Python 脚本、Jupyter Notebook 三种控制方式

---

**准备好了吗？** 👉 从 [QUICK_CONTROL_START.md](QUICK_CONTROL_START.md) 开始吧！

有任何问题或建议，欢迎参考相关文档或查看 [BUGFIX_REPORT.md](BUGFIX_REPORT.md)。
