#!/usr/bin/env python

import rospy
import sys
import os
from autonomous.msg import TaskCMD
from cqueue import CommandQueue

cmd_dict = {
    "DRIVE_TO" : 1,
    "PARK" : 2,
    "RETURN_TO_DOCK" : 3,
    "START_CLOCK" : 4,
    "WAIT_AT_BARRIER" : 5,
    "WAIT_UNTIL" : 6
}

def transmit(command):
    global pub
    t = TaskCMD()
    cmdtype = command["command"]
    cmdarg = command["args"]
    t.task_type = cmd_dict.get(cmdtype, None)
    if t.task_type == 1:
        t.tox = cmdarg["X"]
        t.toy = cmdarg["Y"]
        t.atTime = int(cmdarg["TIME"])
        t.stop_flag = cmdarg["STOP"]
    if t.task_type == 5:
        t.name = cmdarg["NAME"]
        t.count = cmdarg["COUNT"]
    if t.task_type == 6:
        t.atTime = int(cmdarg["TIME"])
    pub.publish(t)




print("Autonomous Car CMD Frontend v1.0")
print("Current path: " + os.getcwd())
rospy.init_node("FrontEnd", anonymous=False)
pub = rospy.Publisher("Task_Delivery", TaskCMD, queue_size = 50)
print("ROS node init successfully!")
print("Please specify a CMD file, type in q for exit")
print("[NOTE] at most 30 commands in one cmd file (after extract the loop)")
while True:
    path = input(">>> ")
    if path == "q":
        exit()
    try:
        file = open(path)
    except (FileNotFoundError):
        print("<<< No such file, plz recheck the path")
        continue
    else:
        print("<<< CMD file load successfully. Breaking it into tasks ...")
        commandQ = CommandQueue()
        commandQ.importFile(file)
        command = commandQ.nextCommand()
        while command != None:
            transmit(command)
            command = commandQ.nextCommand()
        print("<<< all tasks in the CMD file has been assigned!")
