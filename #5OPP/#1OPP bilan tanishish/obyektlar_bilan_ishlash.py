
class Avto:
    """Avtomobil malumotlarini saqlovchi klass"""
    def __init__(self,konpaniya,model,yil,rang):
        self.konpaniya=konpaniya
        self.model=model
        self.yil=yil
        self.rang=rang
        self.narh="nomalum"
        self.km=0
    def get_info(self):
        info=f"Konpaniya {self.konpaniya},modeli {self.model} "
        info+=f"yili {self.yil} rangi {self.rang} "
        info+=f"narhi {self.narh} yosib o'tgan yo'li {self.km} km"
        return info

    def set_narh(self,narh):
        self.narh=narh


    def update_km(self):
        self.km += 5000

avto1=Avto("Gm", "malibu", 2023, "qora")
# print(avto1.set_narh(32000))
# print(avto1.update_km())
# print(avto1.get_info())

class Avto_salon:
    """Avto salon nomli klass"""
    def __init__(self,salon_name,location):
        self.name=salon_name
        self.location=location
        self.sale_cars=[]
    
    def get_info(self):
        info=f"{self.name} avto saloni manzil {self.location}da joylashgan "
        return info
    
    def add_car(self,car):
        self.sale_cars.append(car)
        
    def get_car(self):
        return [car.get_info() for car in self.sale_cars]
    

avto_salon1=Avto_salon("Baraka motors", "furqat tumani")

avto_salon1.add_car(avto1)


avto2=Avto("Gm", "spark", 2011, "oq")

avto_salon1.add_car(avto2)

# print(avto_salon1.get_car())


# print(dir(avto_salon1))

# print(avto1.__dict__)

avtolar={}

avtolar["avto1"]=avto1.__dict__






























