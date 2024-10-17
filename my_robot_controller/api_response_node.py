#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class APISubscriberNode(Node):
    def __init__(self):
        super().__init__('api_subscriber_node')
        
        self.subscription = self.create_subscription(String, 'api_response', self.listener_callback,10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f"Received api response:{msg.data} ")

def main(args=None):
    rclpy.init(args=args)
    
    node = APISubscriberNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()