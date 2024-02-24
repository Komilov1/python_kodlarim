# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:13:09 2024

@author: Asus
"""

import unittest
from name import *



class NameTest(unittest.TestCase):
    def test_name(self):
        name=get_full_name("Akrom",'mahmudov')
        self.assertEqual(name, "Akrom Mahmudov")
    def test_otasini_ismi(self):
        name=get_full_name("abror",'mahmudov','abrorivich')
        self.assertEqual(name, 'Abror Abrorivich Mahmudov')

    def test_big(self):
        big=get_big(5, 41, 30)
        self.assertEqual(big, 41)
        
    def test_title(self):
        title=list_title(['abror', 'axror', 'umid'])
        self.assertEqual(title,['Abror', 'Axror', 'Umid'] )

    def test_couple(self):
        couple=couple_number(list(range(10)))
        self.assertEqual(couple, [0, 2, 4, 6, 8])
        
    def test_fibon(self):
        self.assertTrue(fibonacci(89))
        self.assertTrue(fibonacci(2))
        


unittest.main()

