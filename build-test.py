#!/usr/bin/env python3
from renamer import renamer
import unittest

class UnitTestExample(unittest.TestCase):
    def test_wrong_input(self):
        name = "Ahmed, Abbasi"
        expected = "Abbasi Ahmed"
        self.assertEqual(renamer(name), expected)
        
    def test_empty(self): # that's an edge case as it produces output which is unexpected.
        name = ""
        expected = ""
        self.assertEqual(renamer(name), expected)
        
    #There could be multiple edge cases
    
    #def test_doublenames(self):
    
    #def test_singlenames(self):
    
    #def test_numbernames(self):
    
    # and so on...
        
unittest.main()