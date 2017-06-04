import cv2
import numpy as np
# This path is Given Relative to the Place where File is Executed
import sys
sys.path.append('Extractor/')
sys.path.append('../Extractor/')
from feature_extractor import *


class FlannMatcher:

    def __init__(self):
        self.FLANN_INDEX_KDTREE=0
        self.flannParam=dict(algorithm=self.FLANN_INDEX_KDTREE,tree=5)
        self.flann=cv2.FlannBasedMatcher(self.flannParam,{})

    def getFlann(self):
        return self.flann

    def train(self):
        self.flann.train()

    def findMatches(self,queryImageDescriptor):
        res=self.flann.knnMatch(queryImageDescriptor,k=2)
        return res


    def getBestCombinations(self,matches):
        better_result=[]
        for camera_image,test_image in matches:
            if camera_image.distance< 0.75*test_image.distance:
                better_result.append(camera_image)

        return better_result
        
        

    
        



 

