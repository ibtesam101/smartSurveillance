import cv2
import numpy as np

from Extractor.feature_extractor import *
from Comparison.feature_matcher import *
from Alarm.alarm import *
from Log.logger import *
import datetime
import time


class MainExecutioner:
    # Initialization With the Content
    def __init__(self):
        self.Detect=Detector()
        self.flannMatcher=FlannMatcher()
        self.logger_frame=Logger()
        self.alarming=Alarm()
        self.MIN_MATCH_COUNT = 740
        self.frame_count=0
        self.descA = []
        self.trainedKP = []

    def trainSurf(self):
        for x in range(1, 175):

            a = cv2.imread('snipped/img'+str(x)+'.PNG', 0)

            trainKP,trainDesc = self.Detect.detectionAndCompution(a) # Key Point And Descriptor

            self.trainedKP.append(trainKP)

            if(trainDesc!=None):

                self.flannMatcher.getFlann().add(np.float32(trainDesc))

            self.descA.append(trainDesc)


        self.trainedKP = np.array(self.trainedKP)

        self.flannMatcher.train()


    def start_surveillance(self):
        cam=cv2.VideoCapture('3.mp4')

        cam.set(cv2.cv.CV_CAP_PROP_FPS, 20)

        cam.set(cv2.cv.CV_CAP_PROP_POS_MSEC, 12000)

        while True:
            ret,cameraImg = cam.read()

            cameraImg = cv2.cvtColor(cameraImg, cv2.COLOR_BGR2GRAY)

            cameraImgKP,cameraImgDesc = self.Detect.detectionAndCompution(cameraImg) # Feature of Current Frame

            matches=self.flannMatcher.findMatches(cameraImgDesc)
                           
            goodMatch = self.flannMatcher.getBestCombinations(matches)
    
    
            if(len(goodMatch)>self.MIN_MATCH_COUNT):

                queryPoints = []

                for m in goodMatch:

                    queryPoints.append(cameraImgKP[m.queryIdx])

                cameraImg = cv2.drawKeypoints(cameraImg, queryPoints, color=(0,255,0), flags=0)
        
                print "match found"
        
                self.logger_frame.LogDetectedFrame(cameraImg)
                self.frame_count=self.frame_count+1
                if self.frame_count==5:
                    self.alarming.raise_alarm()
                    self.frame_count=0
                    

            else:

                print "Not enough matches - %d/%d", (len(goodMatch), self.MIN_MATCH_COUNT)

                cameraImg = cv2.drawKeypoints(cameraImg, cameraImgKP, color=(255,0,0), flags=0)
                self.frame_count=0
                        
            
     
            cv2.imshow('frame',cameraImg)

            if cv2.waitKey(1) & 0xFF == ord('q'):

                break

        cam.release()

        cv2.destroyAllWindows()
        
        
        
    
