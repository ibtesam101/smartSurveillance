import pprint
import pymongo
import datetime
import cv2



class Logger:

    def __init__(self,database="surveillance",collection="logger"):
        self.client = pymongo.MongoClient()
        self.logger = self.client.database.collection

    def LogDetectedFrame(self,image):
        current_time=datetime.datetime.now()
        # The Write Path is set Based on the place the Function is called
        cv2.imwrite("CapturedFrames/"+str(current_time).replace(":","-")+".png",image)
        self.logger.insert_one({
            "detection_time":current_time,
            "path":"CapturedFrames/"+str(current_time).replace(":","-")+".png",
            "location":"parking"
            })


    def getCollection(self):
        return self.logger
        





        
        
    
