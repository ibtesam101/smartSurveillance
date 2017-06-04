import unittest
import sys
sys.path.append('../Alarm/')
from alarm import *



class Test(unittest.TestCase):

    def test_AlarmSetting(self):
        self.alarm = Alarm()
        self.assertEqual(self.alarm.getAlarm(),"Test Alarm")
