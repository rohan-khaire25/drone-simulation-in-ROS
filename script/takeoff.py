#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def takeoff():
    rospy.init_node('takeoff_drone', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("taking off")
    

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0.11
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    rospy.sleep(1)

    velocity_publisher.publish(vel_msg)

    rospy.sleep(0.8)

    vel_msg.linear.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.loginfo("All went well. Published to topic ")


if __name__ == '__main__':
    try:
        takeoff()
    except rospy.ROSInterruptException: pass    
