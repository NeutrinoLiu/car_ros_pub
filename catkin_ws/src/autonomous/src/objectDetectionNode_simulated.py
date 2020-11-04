#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from autonomous.msg import ObjDetect
import numpy as np

#initalize variables
objects = ObjDetect()
objects.ID = 0
objects.type = "Rock"
objects.x = 10
objects.y = 0

def talker():

    global objects

    #create a publisher with topic name, message type string
    pub = rospy.Publisher('Object_Detection', ObjDetect, queue_size=10)

    #launch a node called "get_location_and_publish"
    rospy.init_node('ObjectDetectionNode', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():

        message = objects
        rospy.loginfo(message)
        pub.publish(message)
        update_objects()
        rate.sleep()

def update_objects():
    # get new objects location
    pass

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
