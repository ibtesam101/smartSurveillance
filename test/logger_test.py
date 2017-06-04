import unittest
import sys
sys.path.append('../Log/')
from logger import *



class Test(unittest.TestCase):

    def test_CollectionSetting(self):
        self.log = Logger()
        self.assertNotEqual(self.log.getCollection(),"")
