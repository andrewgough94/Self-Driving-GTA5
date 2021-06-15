import sys
import time

import cv2
import numpy as np
from PIL import ImageGrab
from drawlanes import DrawLanes


def roi(img, vertices):
    # Empty mask of size image
    mask = np.zeros_like(img)
    # Fill mask by vertices at full value of 255
    cv2.fillPoly(mask, vertices, 255)
    # Apply roi mask to our image and keep that as masked
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)

    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)

    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                         ], np.int32)

    processed_img = roi(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                                     rho   theta   thresh  min length, max gap:
    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 180, 20, 15)
    try:
        l1, l2 = DrawLanes(original_image, lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)


            except Exception as e:
                print(str(e))
    except Exception as e:
        pass

    return processed_img, original_image

# Let's know how big each frame is
def get_screen_data(img):
    # processing img is now a numpy ndarray
    shape = img.shape
    size = img.size
    print(shape, size)

    memory_size = sys.getsizeof(img)
    print('array size in bytes = ', memory_size)

def main():
    # Removed the wait because no input will be entered with this file
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))
        new_screen, original_image = process_img(screen)
        #get_screen_data(screen)
        #print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()