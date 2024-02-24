# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:56:21 2024

@author: Asus
"""

import unittest
from shaxs_talaba import Shaxs,Talaba
class SHaxs_test(unittest.TestCase):
    """shaxs klasini tekshiruvchi test"""
    def setUp(self):
        ism="Ali"
        familiya="Valiyev"
        passport="AC157862"
        self.tyil=2004
        self.shaxs1=Shaxs(ism, familiya, passport, tyil=self.tyil)
        
    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        self.assertEqual(self.tyil, self.shaxs1.tyil)
        
    def test_get_age(self):
        info=2024-self.shaxs1.tyil
        self.assertEqual(info, self.shaxs1.get_age(2024))
        
    def test_get_info(self):
        info=f"{self.shaxs1.ism.title()} {self.shaxs1.familiya.title()}. "
        info+=f"Passport:{self.shaxs1.passport}, {self.shaxs1.tyil}-yilda tug'ilgan"
        self.assertEqual(info, self.shaxs1.get_info())

class Talaba_test(unittest.TestCase):
    """Talaba klassini tekshiruvchi test"""
    def setUp(self):
        self.idraqam="0000114"
        self.bosqich=1
        self.talaba1=Talaba('Abbos', 'Yusupov', "AC437286", 2004, idraqam=self.idraqam)
        self.shaxs1=Shaxs("ism", "familiya", "passport", "tyil")

    def test_create(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba1.idraqam)
        self.assertIsNotNone(self.talaba1.bosqich)
        
    def tets_get_id(self):
        info=self.talaba1.idraqam
        self.assertEqual(info, self.talaba1.get_id())
        
    def test_get_bosqich(self):
        self.assertEqual(self.bosqich, self.talaba1.get_bosqich())
        
    def test_get_info(self):
        info=f"{self.talaba1.ism} {self.talaba1.familiya}. "
        info+=f"{self.talaba1.bosqich}-bosqich. ID raqami: {self.talaba1.idraqam}"
        self.assertEqual(info, self.talaba1.get_info())
        
    def test_vorismi(self):
        self.assertIsInstance(self.talaba1, Talaba)
        self.assertIsInstance(self.shaxs1, Shaxs)


unittest.main()


































