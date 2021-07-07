# Self-Driving-GTA5

Different versions of the self-driving agent will live under the 
`/progression/` folder 

1 - openCV_grayScale_edgeDetection.py - reads in game frames and processes frames using gray scale and detects / draws edges

2 - input_to_game.py 

3? - Line detection Hough lines

4? - Lane detection 


## Adding dependencies / Environment Mgmt
https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/

Project Settings, add python interpreter, from existing conda environment

## Frame size

Raw screen from image grab as numpy array
(600, 800, 3) 1440000
array size in bytes =  1440128

With region of interest
(600, 800) 480000
array size in bytes =  480112, 480 KB, .48 MB

## Fun Experiments

Apply to rocket league, halo, valheim (tree identification+chop)
