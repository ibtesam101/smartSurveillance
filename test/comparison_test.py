import unittest
import sys
sys.path.append('../Comparison/')
from feature_matcher import *



class Test(unittest.TestCase):

    def test_CollectionSetting(self):
        self.matcher = FlannMatcher()
        self.assertEqual(self.matcher.FLANN_INDEX_KDTREE,0)
        self.assertNotEquals(self.matcher.getFlann(),"")
