#!/usr/bin/env python
import rospy
from std_msgs.msg import String

trajectory = "0,0,0"


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Vehicle in position at %s", data.data)
    
def locateObjects(data):
    rospy.loginfo(rospy.get_caller_id()+ "Object detected: %s",data.data)

def get_trajectotry():
    #somehow figure out the next position this vehicle should goto
    #for example
    return "10,10,10"

def talker():
    global trajectory
    #launch a node
    rospy.init_node('ControllerNode', anonymous=True)

    #create subscriber
    rospy.Subscriber("Location_info", String, callback)
    #create subscriber
    rospy.Subscriber("Object_Detection",String,locateObjects)

    #creat a publisher
    pub = rospy.Publisher("Trajectory",String,queue_size = 10)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        trajectory = get_trajectotry()
        rospy.loginfo(trajectory)
        pub.publish(trajectory)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: 
        pass
