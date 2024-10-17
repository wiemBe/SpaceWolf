#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class APICallerNode(Node):
    def __init__(self):
        super().__init__('api_caller_node')
        self.publisher = self.create_publisher(String, 'api_response', 10)
        self.call_api()
        self.create_timer(1.0,self.call_api) #TODO:will add have_job to check there is a job currently working on

    def call_api(self):
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
            if response.status_code == 200:
                data = response.json()
                self.get_logger().info(f"API response:{data} ")

                message = String()
                message.data = f"API response:{data}"
                self.publisher.publish(message)
            else:
                self.get_logger().info(f"failed to reach status code:{response.status_code} ")
        except requests.exceptions.RequestException as e:
            self.get_logger().error(f"api call failed:{e} ")






def main(args=None):
    rclpy.init()
    
    node = APICallerNode()
    rclpy.spin(node)

    rclpy.shutdown()




if __name__ =='__main__':
    main()