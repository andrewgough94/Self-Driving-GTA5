# Self-Driving-GTA5

Different versions of the self-driving agent will live under the 
`/progression/` folder 

1 - openCV_grayScale_edgeDetection.py - reads in game frames and processes frames using gray scale and detects / draws edges (13.34 FPS)

2 - input_to_game.py - interacts with GTA5 using Direct Keys defined in directkeys.py 

3 - region_of_interest.py - draws a polygon ROI through implementing roi() to mask our image, now with the ROI applied, we won't detect poles or wires, letting us focus on the road ahead while also minimizing the image further 
[download.png]

4 - Line detection Hough lines - draws lines detected using the Hough Line Transformation algorithm - https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html 
also smoothing the image to help detect stronger lines using cv2.GaussianBlur (https://docs.opencv.org/4.5.2/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1)

4? - Lane detection 


## Adding dependencies / Environment Mgmt
https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/

Project Settings, add python interpreter, from existing conda environment

## Frame size and data considerations

Raw screen from image grab as numpy array
(800, 600, 3) 1,440,000
array size in bytes =  1,440,128 = 1.4MB per un-processed frame

Gray scaling helps simplify things (by reducing our image to one value vs. RGB's 3 values per pixel) resulting in 
(800, 600, 1) 480,000
array size in bytes = 480KB per gray-scaled frame

With region of interest
(800, 600) 480000
array size in bytes =  480112, 480 KB, .48 MB

### To put this into perspective
1 black-white pixel contains 8 bits (2^8, 256 possible values)
1 RBG pixel contains 24 bits (2^24, 16777216 possible values)

4k displays represent a horizontal resolution of 4k pixels
Majority of 4k displays come with a (Ultra-HDTV) 3840 x 2160 pixel resolution which is 4x the pixel count of full HD displays 1920 x 1080 pixels

4k grayscale = (3840, 2160, 1) = 8,294,400B = 8.2MB per frame
4k rbg = (3840, 2160, 3) = 24,883,200 = 24.8MB per frame

TODO - Tesla's vehicles contain 12 cameras at (XXX resolution) - capturing X frames per second - recording XXX data per second - this is mind boggling data being generated every second

## Fun Experiments

Apply to rocket league, halo, valheim (tree identification+chop)
