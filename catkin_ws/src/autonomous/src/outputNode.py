#!/usr/bin/env python
import rospy
from std_msgs.msg import String



def setMotor(data):
    rospy.loginfo(rospy.get_caller_id() + "Set motors speed to %s", data.data)
    #here we shouls somehow set the actual motor speed and angle


def listener():
    global trajectory
    #launch a node
    rospy.init_node('OutputNode', anonymous=True)

    #create subscriber
    rospy.Subscriber("MotorInfo", String, setMotor)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():

        rate.sleep()


if __name__ == '__main__':
    listener()
