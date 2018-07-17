#!/usr/bin/env python
import rospy
import os
import time
import sys
from os.path import expanduser

def camera_reader():
    rospy.init_node ('RGBCamera', anonymous=True)
    rospy.loginfo ("Open Camera Function")

    #Find RGB camera name
    camera_info = os.popen("v4l2-ctl --list-devices |tr -s '\n\t' '_'").read()
    camera_info_split = camera_info.split('_')
    find_camera = "RGB"
    camera = ""
    for idx, val in enumerate(camera_info_split):
        if val.find(find_camera) != -1:
            camera = camera_info_split[idx+1]
            break
    rospy.loginfo (camera)
    if camera == "":
        rospy.loginfo ("There is no RGB camera")
        sys.exit(0)

    #Check the folder exist
    path = expanduser("~") + "/video/"
    if not os.path.isdir(path):
        rospy.loginfo ("Create agv_video Folder")
        os.mkdir(path)

    #Recording
    while not rospy.is_shutdown():
        video_name = time.strftime('%Y_%m_%d_%H_%M_%S')
        file_number = int(os.popen("ls -l | grep '/*.mp4' | wc -l").read())
        rospy.loginfo (file_number)
        if file_number > 59:
            rm_file = os.popen("ls -rt | grep '/*.mp4' | head -n1").read()
            os.popen("rm -r " + rm_file)
        os.popen("ffmpeg -t 300 -s 640x480 -i " + camera + " -vf hflip -b:v 700K "+ path + video_name + ".mp4")

if __name__ == "__main__":
    try:
        camera_reader()
    except rospy.ROSInterruptException, e:
        rospy.loginfo ("'RGBCamera' cannot launch.")
        rospy.loginfo(e)
        pass