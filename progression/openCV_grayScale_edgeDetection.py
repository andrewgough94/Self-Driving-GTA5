# This is a sample Python script.

import numpy as np
from PIL import Image, ImageGrab
import cv2
import time

# Defined in part 2
def process_img(original_image):
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img


print("hey")
last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)
    print("Loop took {} seconds".format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window',new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

print("hi")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
