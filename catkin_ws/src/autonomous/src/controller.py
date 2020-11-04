#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from autonomous.msg import Localization, ObjDetect
from math import sqrt

trajectory = "0,0,0"
car_pos = Localization()
object_pos = ObjDetect()

def update_car_pos(data):
    global car_pos
#    rospy.loginfo(rospy.get_caller_id() + "Vehicle in position at")
    car_pos = data

def update_object_pos(data):
    global object_pos
#    rospy.loginfo(rospy.get_caller_id()+ "Object detected: %s",data.x,data.y)
    object_pos = data

def get_distance(xa,xb, ya, yb):
    d = sqrt((xa-xb)**2+(ya-yb)**2)
    print("distance to object: "+ str(d))
    return d

def get_trajectotry():
    #somehow figure out the next position this vehicle should goto
    #for example
    global cat_pos, object_pos
    distance_to_object = get_distance(car_pos.x, object_pos.x, car_pos.y, object_pos.y)
    if (distance_to_object < 2):
        return "STOP"
    return "MOVE"

def talker():
    global trajectory
    #launch a node
    rospy.init_node('ControllerNode', anonymous=True)

    #create subscriber
    rospy.Subscriber("Location_info", Localization, update_car_pos)
    #create subscriber
    rospy.Subscriber("Object_Detection",ObjDetect, update_object_pos)

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
