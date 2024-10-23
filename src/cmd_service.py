#!/usr/bin/env python3

import os
import rospy

from system_integration.srv import CmdService

def handle_cmd(req):
    return os.system(req.cmd)

def cmd_server():
    nodename = "cmd_service_node"
    servicename = "cmd_service"
    if(os.getlogin() == "robofeilab"):
        nodename += "_nuc"
        servicename += "_nuc"
    if(os.getlogin() == "robofei"):
        nodename += "_jetson"
        servicename += "_jetson"
    rospy.init_node(nodename)
    rospy.Service(servicename, CmdService,  handle_cmd)
    print("Ready to receive commands")
    rospy.spin()

if __name__ == "__main__":
    cmd_server()
