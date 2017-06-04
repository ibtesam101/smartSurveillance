import cv2
import numpy as np

from Extractor.feature_extractor import *
from Comparison.feature_matcher import *
from Log.logger import *
import datetime
import time

Detect=Detector()
flannMatcher=FlannMatcher()
logger_frame=Logger()


trainImg=cv2.imread('TrainingSet/img25_new.png',1)
#trainImg=cv2.cvtColor(trainImg,cv2.COLOR_BGR2GRAY)


trainKP,trainDesc=Detect.detectionAndCompution(trainImg) # Key Point And Descriptor
# To show the Keypoints of the Training Image
img=cv2.drawKeypoints(trainImg,trainKP,trainImg)

cv2.imshow('image',img)


min_match_count=20   # Minimum threshold to detect object

height,width,channels=trainImg.shape

cam=cv2.VideoCapture('3.mp4')

print cam.grab()
cam.set(cv2.cv.CV_CAP_PROP_FPS,60)
cam.set(cv2.cv.CV_CAP_PROP_POS_MSEC,22000)


while True:
    ret,cameraImg=cam.read()
    #cameraImg=cv2.cvtColor(cameraImg,cv2.COLOR_BGR2GRAY)
    cameraImgKP,cameraImgDesc=Detect.detectionAndCompution(cameraImg) # Feature of Current Frame
    matches=flannMatcher.findMatches(cameraImgDesc,trainDesc)
    better_result=flannMatcher.getBestCombinations(matches)


    if (len(better_result)> min_match_count):
        print "Match Found"
        
        training_key_points=[]
        camera_key_points=[]
        
        # Getting the index vals 
        for current in better_result:
            training_key_points.append(trainKP[current.trainIdx].pt)
            camera_key_points.append(cameraImgKP[current.queryIdx].pt)
            
        training_key_points,camera_key_points=np.float32((training_key_points,camera_key_points))
        trans_const,status=cv2.findHomography(training_key_points,camera_key_points,cv2.RANSAC,3.0)
        
        
        trainingBorder=np.float32([[[0,0],[0,height-1],[width-1,height-1],[width-1,0]]])
        
        queryBorder=cv2.perspectiveTransform(trainingBorder,trans_const)
        cv2.polylines(cameraImg,[np.int32(queryBorder)],True,(0,255,0),5)
        # Logging the Detected Frame
        logger_frame.LogDetectedFrame(cameraImg)
        
        print "Frame Logged"
    
            
            
     
    cv2.imshow('frame',cameraImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
