import winsound


class Alarm:

    def __init__(self):
        self.alarm="Test Alarm"

    def raise_alarm(self):
        winsound.PlaySound("SystemHand", winsound.SND_ASYNC)

    def getAlarm(self):
        return self.alarm
        
        
        
    
