#!/usr/bin/env python3
"""
Panda Robot Joint Control Script
允许用户通过发布关节状态来控制 Panda 机器人的关节角度
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import math
import sys


class PandaJointController(Node):
    """Panda 机器人关节控制器"""
    
    def __init__(self):
        super().__init__('panda_joint_controller')
        
        # 创建发布者
        self.joint_state_pub = self.create_publisher(
            JointState, '/joint_states', 10
        )
        
        # Panda 机器人的所有关节名称
        self.joint_names = [
            'panda_joint1',
            'panda_joint2',
            'panda_joint3',
            'panda_joint4',
            'panda_joint5',
            'panda_joint6',
            'panda_joint7',
            'panda_hand_joint',
            'panda_leftfinger_joint',
            'panda_rightfinger_joint'
        ]
        
        self.get_logger().info('Panda Joint Controller 已启动')
        self.get_logger().info(f'可控制的关节: {", ".join(self.joint_names)}')
    
    def publish_joint_state(self, positions):
        """
        发布关节状态
        
        Args:
            positions: 字典，键为关节名称，值为角度（弧度）
        """
        msg = JointState()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        
        # 初始化所有关节为 0
        msg.name = self.joint_names
        msg.position = [0.0] * len(self.joint_names)
        msg.velocity = [0.0] * len(self.joint_names)
        msg.effort = [0.0] * len(self.joint_names)
        
        # 更新指定关节的位置
        for joint_name, position in positions.items():
            if joint_name in self.joint_names:
                idx = self.joint_names.index(joint_name)
                msg.position[idx] = position
            else:
                self.get_logger().warn(f'未知的关节: {joint_name}')
        
        self.joint_state_pub.publish(msg)
        self.get_logger().info(f'发布关节状态: {positions}')
    
    def set_home_position(self):
        """设置机器人回到初始位置"""
        positions = {
            'panda_joint1': 0.0,
            'panda_joint2': 0.0,
            'panda_joint3': 0.0,
            'panda_joint4': 0.0,
            'panda_joint5': 0.0,
            'panda_joint6': 0.0,
            'panda_joint7': 0.0,
            'panda_hand_joint': 0.0,
            'panda_leftfinger_joint': 0.0,
            'panda_rightfinger_joint': 0.0,
        }
        self.publish_joint_state(positions)
    
    def set_ready_position(self):
        """设置机器人到准备位置（类似于 Panda 的标准准备姿态）"""
        positions = {
            'panda_joint1': 0.0,
            'panda_joint2': -math.pi / 4,
            'panda_joint3': 0.0,
            'panda_joint4': -3 * math.pi / 4,
            'panda_joint5': 0.0,
            'panda_joint6': math.pi / 2,
            'panda_joint7': math.pi / 4,
            'panda_hand_joint': 0.0,
            'panda_leftfinger_joint': 0.0,
            'panda_rightfinger_joint': 0.0,
        }
        self.publish_joint_state(positions)
    
    def set_stretch_position(self):
        """设置机器人到伸展位置"""
        positions = {
            'panda_joint1': 0.0,
            'panda_joint2': -math.pi / 6,
            'panda_joint3': 0.0,
            'panda_joint4': -math.pi / 2,
            'panda_joint5': 0.0,
            'panda_joint6': math.pi / 3,
            'panda_joint7': 0.0,
            'panda_hand_joint': 0.0,
            'panda_leftfinger_joint': 0.0,
            'panda_rightfinger_joint': 0.0,
        }
        self.publish_joint_state(positions)
    
    def open_gripper(self, width=0.04):
        """
        打开夹爪
        
        Args:
            width: 夹爪宽度（米），默认 0.04
        """
        # 计算手指角度（简化模型）
        finger_angle = width / 2
        positions = {
            'panda_leftfinger_joint': finger_angle,
            'panda_rightfinger_joint': finger_angle,
        }
        self.publish_joint_state(positions)
        self.get_logger().info(f'打开夹爪，宽度: {width} m')
    
    def close_gripper(self):
        """关闭夹爪"""
        positions = {
            'panda_leftfinger_joint': 0.0,
            'panda_rightfinger_joint': 0.0,
        }
        self.publish_joint_state(positions)
        self.get_logger().info('关闭夹爪')


def main():
    """主函数"""
    rclpy.init()
    controller = PandaJointController()
    
    # 处理命令行参数
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'home':
            controller.set_home_position()
        elif command == 'ready':
            controller.set_ready_position()
        elif command == 'stretch':
            controller.set_stretch_position()
        elif command == 'open':
            width = float(sys.argv[2]) if len(sys.argv) > 2 else 0.04
            controller.open_gripper(width)
        elif command == 'close':
            controller.close_gripper()
        else:
            print_help()
    else:
        print_help()
    
    # 保持节点运行（用户可以继续发送命令）
    print('\n按 Ctrl+C 退出')
    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()


def print_help():
    """打印帮助信息"""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║           Panda Robot Joint Control - 使用说明                ║
╚═══════════════════════════════════════════════════════════════╝

用法:
    python3 panda_joint_controller.py <command> [args]

命令:
    home       - 将机器人回到初始位置（所有关节 0°）
    ready      - 将机器人设置到准备位置
    stretch    - 将机器人设置到伸展位置
    open [宽度] - 打开夹爪（可选宽度，默认 0.04 米）
    close      - 关闭夹爪

示例:
    python3 panda_joint_controller.py home
    python3 panda_joint_controller.py ready
    python3 panda_joint_controller.py open
    python3 panda_joint_controller.py open 0.08
    python3 panda_joint_controller.py close

在 Python 代码中使用:
    
    from panda_joint_controller import PandaJointController
    import rclpy
    
    rclpy.init()
    controller = PandaJointController()
    
    # 设置关节到特定角度
    controller.publish_joint_state({
        'panda_joint1': 0.5,    # 关节1 - 0.5 弧度
        'panda_joint2': -0.7,   # 关节2 - -0.7 弧度
        'panda_joint3': 0.3,    # 关节3 - 0.3 弧度
    })
    
    rclpy.shutdown()

按 Ctrl+C 退出程序
═══════════════════════════════════════════════════════════════════
    """)


if __name__ == '__main__':
    main()
