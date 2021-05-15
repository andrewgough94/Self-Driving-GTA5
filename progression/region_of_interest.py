import numpy as np
from PIL import ImageGrab
import cv2
import time
import sys

def roi(img, vertices):
    # Empty mask of size image
    mask = np.zeros_like(img)
    # Fill mask by vertices at full value of 255
    cv2.fillPoly(mask, vertices, 255)
    # Apply roi mask to our image and keep that as masked
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                         ], np.int32)
    processed_img = roi(processed_img, [vertices])
    return processed_img

# Let's know how big each frame is
def get_screen_data(img):
    # processing img is now a numpy ndarray
    shape = img.shape
    size = img.size
    print(shape, size)

    memory_size = sys.getsizeof(img)
    print('array size in bytes = ', memory_size)

def main():
    print('andrew')
    # Removed the wait because no input will be entered with this file
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))
        new_screen = process_img(screen)
        get_screen_data(new_screen)
        print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()