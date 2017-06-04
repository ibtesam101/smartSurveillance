import cv2
import numpy as np

# SIFT Detector Class
class Detector:
    
    def __init__(self):
        self.detector=cv2.SURF(100)

    def getDetector(self):
        return self.detector
    
    # SIFT Detector to get the Key point and Descriptor of the Given Image
    def detectionAndCompution(self,image):
        return self.detector.detectAndCompute(image,None)
