#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import numpy as np

#initalize variables
objects = np.array(["701,0,10,0","702,1,0,10","703,2,10,10","704,3,20,20"])
segment_number = 0;

def talker():

    global objects, segment_number

    #create a publisher with topic name, message type string
    pub = rospy.Publisher('Object_Detection', String, queue_size=10)

    #launch a node called "get_location_and_publish"
    rospy.init_node('ObjectDetectionNode', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():

        message = objects[segment_number]
        rospy.loginfo(message)
        pub.publish(message)
        increment_segment()
        rate.sleep()

def increment_segment():
    global segment_number

    segment_number = segment_number+1

    if(segment_number >= objects.size):
        segment_number = 0;


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
