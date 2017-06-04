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

MIN_MATCH_COUNT = 740


descA = []

trainedKP = []


for x in range(1, 175):

    a = cv2.imread('snipped/img'+str(x)+'.PNG', 0)

    trainKP,trainDesc = Detect.detectionAndCompution(a) # Key Point And Descriptor

    trainedKP.append(trainKP)

    if(trainDesc!=None):

        flannMatcher.getFlann().add(np.float32(trainDesc))

    descA.append(trainDesc)



trainedKP = np.array(trainedKP)


flannMatcher.train()

cam=cv2.VideoCapture('3.mp4')

cam.set(cv2.cv.CV_CAP_PROP_FPS, 20)

cam.set(cv2.cv.CV_CAP_PROP_POS_MSEC, 10000)

while True:
    ret,cameraImg = cam.read()

    cameraImg = cv2.cvtColor(cameraImg, cv2.COLOR_BGR2GRAY)

    cameraImgKP,cameraImgDesc = Detect.detectionAndCompution(cameraImg) # Feature of Current Frame

    matches=flannMatcher.findMatches(cameraImgDesc)
                           
    goodMatch = flannMatcher.getBestCombinations(matches)
    
    
    if(len(goodMatch)>MIN_MATCH_COUNT):

        queryPoints = []

        for m in goodMatch:

            queryPoints.append(cameraImgKP[m.queryIdx])

        cameraImg = cv2.drawKeypoints(cameraImg, queryPoints, color=(0,255,0), flags=0)
        
        print "match found"
        
        logger_frame.LogDetectedFrame(cameraImg)

    else:

        print "Not enough matches - %d/%d", (len(goodMatch), MIN_MATCH_COUNT)

        cameraImg = cv2.drawKeypoints(cameraImg, cameraImgKP, color=(255,0,0), flags=0)
                        
            
     
    cv2.imshow('frame',cameraImg)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

cam.release()

cv2.destroyAllWindows()

