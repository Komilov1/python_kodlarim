import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """car klassini tekshiruvchi test"""
    # def test_create(self):
    #     #avto1 obektini km va narh bermasdan yaeatamiz
    #     avto1=Car("Gm", 'Malibu', 2023)
    #     #Qiymat mavjudligini assertIsNotNone orqali tekshiramiz
    #     self.assertIsNotNone(avto1.make)
    #     self.assertIsNotNone(avto1.model)
    #     self.assertIsNotNone(avto1.year)
    #     #narh mavjud emasligini assertIsNone bilan tekshiramiz
    #     self.assertIsNone(avto1.price)
    #     #avto1ga km 0 tengligini tekshirammiz
    #     self.assertEqual(0, avto1.get_km())
    #     #Yangi obyekt yaratamiz va narh va km berib tekshiramiz
    #     avto2=Car("Gm", 'spark', 2011,6500,30000)
    #     self.assertIsNotNone(avto2.price)
    #     self.assertIsNotNone(avto2.get_km())        
        
    def setUp(self):
        make="Gm"
        model="malibu"
        year=2023
        self.price=35000
        self.km=10000
        self.avto1=Car(make, model, year)
        self.avto2=Car(make, model, year,price=self.price)
    
    def test_create(self):
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertIsNone(self.avto1.price)
        self.assertIsNotNone(self.avto2.price)
    
    def test_set_price(self):
        new_price=40000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)

    def  test_add_km(self):
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        try:
            self.avto1.add_km(-500)
        except ValueError as error:
            self.assertEqual(type(error),ValueError)
            
    def test_get_info(self):
        info = f"{self.avto1.make.upper()} {self.avto1.model.title()}, " 
        info += f"{self.avto1.year}-yil, {self.avto1.get_km()}km yurgan."
        self.assertEqual(info, self.avto1.get_info())
        if self.avto1.price:
            info+=f" Narhi: {self.price}"
            self.assertEqual(info, self.avto1.get_info())

    
unittest.main()