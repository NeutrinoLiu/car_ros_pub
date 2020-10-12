#!/usr/bin/env python
import rospy
from std_msgs.msg import String

motorSetting = "0,0,0"

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "next position at %s", data.data)

def get_motor_speed():
    #somehow figure out motor speed and angle
    #for example
    return "180,180,0"

def talker():
    global motorSetting
    #launch a node
    rospy.init_node('TrackFollowerNode', anonymous=True)

    #create subscriber
    rospy.Subscriber("Trajectory", String, callback)

    #creat a publisher
    pub = rospy.Publisher("MotorInfo",String,queue_size = 10)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        motorSetting = get_motor_speed()
        rospy.loginfo(motorSetting)
        pub.publish(motorSetting)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
