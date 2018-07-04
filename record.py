import os
import time

camera_info = os.popen("v4l2-ctl --list-devices |tr -s '\n\t' '_'").read()
camera_info_split = camera_info.split('_')
find_camera = "RGB"
 
for idx, val in enumerate(camera_info_split):
	if val.find(find_camera) != -1:
		camera = camera_info_split[idx+1]
		break
print camera


while (1):
	video_name = time.strftime('%Y_%m_%d_%H_%M_%S')
	file_number = int(os.popen("ls -l | grep '/*.mp4' | wc -l").read())
	print file_number
	if file_number > 59:
		rm_file = os.popen("ls -rt | grep '/*.mp4' | head -n1").read()
		os.popen("rm -r " + rm_file)
	os.popen("ffmpeg -t 300 -s 640x480 -i " + camera + " -vf hflip -b:v 700K " + video_name + ".mp4")