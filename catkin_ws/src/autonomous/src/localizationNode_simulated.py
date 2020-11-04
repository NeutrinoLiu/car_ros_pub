#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from autonomous.msg import Localization
import numpy as np

#initalize variables
path_segment = Localization()
path_segment.x = 0
path_segment.y = 0
path_segment.z = 0
path_segment.yaw = 0
path_segment.pitch =0
path_segment.roll = 0

def talker():

    global path_segment

    #create a publish with topic name, message type string
    pub = rospy.Publisher('Location_info', Localization, queue_size=10)
    
    #launch a node called "get_location_and_publish"
    rospy.init_node('get_location_and_publish', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():

        message = path_segment

        rospy.loginfo(message)
        pub.publish(message)
        update_location()
        rate.sleep()

def update_location():
    global path_segment

    path_segment.x = path_segment.x + 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
