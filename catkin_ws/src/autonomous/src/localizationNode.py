#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import numpy as np

#initalize variables
location = np.array(["0,0,0","0,1,2","0,2,4","0,3,6"])
segment_number = 0;
path_complete = False;

def talker():

    global location, segment_number, path_complete

    #create a publish with topic name, message type string
    pub = rospy.Publisher('Location_info', String, queue_size=10)
    
    #launch a node called "get_location_and_publish"
    rospy.init_node('get_location_and_publish', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():

        message = location[segment_number]
        rospy.loginfo(message)
        pub.publish(message)
        increment_segment()
        rate.sleep()

def increment_segment():
    global segment_number, path_complete
   
    segment_number = segment_number+1

    if(segment_number >= location.size):
        path_complete = True;
        segment_number = 0;
    else:
        path_complete - False;

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
