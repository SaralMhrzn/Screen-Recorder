import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# capturing width and height of current display
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# storing value of width and height in dim variable
dim = (width, height)

# compression video files
f = cv2.VideoWriter_fourcc(*"XVID")

# storing video
output = cv2.VideoWriter("test.mp4",f,30.0,dim)

# recort start time
now_start_time = time.time()

# Duration of the video in seconds
dur = 10 + 4
# 10 sec for screen recording and 4 min is for starting ma code run huna lie 

# stoping screen recorder
end_time = now_start_time + dur

while True:
    # taking ss using screenshot function calling from pyautogui module
    image = pyautogui.screenshot()

    #storing ss 
    frame_1 = np.array(image) 
    # np.array creates array and we storing all ss in array

    # setting color (Convert the color from BGR to RGB)
    setting_color = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    # cvtColor = color function and cv2.COLOR_BGR2RGB this sets original color of image jun ss leko theyo

    # write the frame to the video file
    output.write(setting_color)

    # check the current time
    current_time = time.time()

    if current_time > end_time:
        break

# releasing video(mathi compress garera rakheko video aba video format ma rakhni)
output.release()

print("End")



