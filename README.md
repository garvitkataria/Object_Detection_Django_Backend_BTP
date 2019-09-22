# Pothole Detection System using UAV Imagery and Smartphone Devices
Potholes have been a major cause of causalities in India. As per the latest data, in
2017, a total of 4,64,910 road accidents were reported in India. A constant
detection of potholes and repair in proper time can not only result in ensure road
surface quality but can also save many lives.
The proposal describes one such low-cost road maintenance system by detecting
potholes from images and videos gathered from drones and smartphone devices by
using state of the art deep learning models. The objective is to detect the potholes
from the images and map it to the Google Maps in real time.

### Tech. Stack
Django, Flask, Ionic 4.0, Angular, TensorFlow

### Server Architecture
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
## About The Dataset

Source: http://machineintelligenceafrica.org/activities/hackathon/

We got our dataset from a hackathon where the challenge was to detect pothole in images, which is a binary classification problem.
There were about 5000+ training images with labels. We got the images from dataset. However we had to manually label each of them for potholes. We
manually labelled about 1500+ images using [labellmg](https://github.com/tzutalin/labelImg) .


## Mobile App
We created a mobile app for our project which have the following features:
<ul>
<li>
Authentication and Authorization.
</li>

<li>
Mapping of pothole data on Google Maps
</li>

<li>
Admin Dashboard for monitoring
</li>

<li>
Camera Photograph upload of potholes with position from GPS.
</li>

<li>
Feedback feature
</li>
</ul>

## Experimental analysis
We were able to train 3 tensor-flow deep learning state of the art models for object detection. The models and their results are listed below.
 
 1. SSD_MOBILENET_V2_COCO (map=21)<br>
    • Average Precision (AP) @[IOU=1.50] = 0.409<br>
    • Average Recall (AR) @[IOU=1.50] = 0.473
    
2. FASTER_RCNN_INCEPTION_V2_COCO (map=24)<br>
    • Average Precision (AP) @[IOU=1.50] = 0.467 <br>
    • Average Recall (AR) @[IOU=1.50] = 0.494
    
3. FASTER_RCNN_INCEPTION_RESNET_V2_ATROUS_COCO (map=37)<br>
    • Average Precision (AP) @[IOU=1.50] = 0.495 <br>
    • Average Recall (AR) @[IOU=1.50] = 0.562
   
   
   
## Observations
1. SSD with MobileNet provides the best accuracy tradeoff within the fastest
2. SSD is fast but performs worse for small objects comparing with others.
3. SSD models are faster on average but cannot beat the Faster R-CNN in accuracy if speed is not a concern.
 
## Challenges
• Output depends on factors such as height from which image is taken, angle of inclination.<br>
• Images captured in a wide variety of weather and illuminance conditions.<br>
• Capturing video frames from drones and testing in real time.<br>

## Summary and conclusion
Prototype of one such low-cost road maintenance system by detecting potholes
from images and videos gathered from smartphone devices by using state of the art
deep learning models. The objective is to detect the potholes from the images and
map it to the Google Maps in real time.
