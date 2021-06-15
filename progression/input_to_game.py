import time

import cv2
import numpy as np
from PIL import ImageGrab

from directkeys import PressKey, ReleaseKey, W

# 4 second countdown before image capture / action selection
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

# Defined in part 2
def process_img(original_image):
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection using canny edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)

    # Press forward down for 3 seconds at a time
    print('down')
    PressKey(W)
    time.sleep(3)
    print('up')
    ReleaseKey(W)

    print("Loop took {} seconds".format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
