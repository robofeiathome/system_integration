#!/usr/bin/env python3

import os
import rospy

from system_integration.srv import CmdService

def handle_cmd(req):
    return os.system(req.cmd)

def cmd_server():
    rospy.init_node('cmd_service.py')
    rospy.Service('cmd_service', CmdService,  handle_cmd)
    print("Ready to receive commands")
    rospy.spin()

if __name__ == "__main__":
    cmd_server()