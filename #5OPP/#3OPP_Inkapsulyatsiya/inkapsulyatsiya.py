
"""Inkapsulyatsiya"""

class  Shaxs:
    """Shaxs haqida ma'lumot"""
    __odamlar_soni=0 #klassga oid xususiyatlar
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.__passport=passport#<<<inkapsulyatsiya
        self.tyil=tyil
        Shaxs.__odamlar_soni+=1
   
    @classmethod #Klassga oid xususiyatlar bilan ishlash uchun maxsus metod
    def get_shaxs_soni(cls):
        return cls.__odamlar_soni        
    
    def get_info(self):
        """Shaxs haqida to'liq ma'lumot qaytaruvchi metod"""
        info=f"{self.ism.title()} {self.familiya.title()}. "
        info+=f"{self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil-self.tyil
    
    def get_passport(self):#inkapsulyatsiya hususiyatini ko'rish
        return self.__passport
    
    def set_passport(self,new_passport):
        self.__passport=new_passport
    
        
class Talaba(Shaxs):
    """Talaba haqida ma'lumot"""
    __talabalar_soni=0 #klassga oid xususiyatlar
    def __init__(self, ism, familiya, passport, tyil, id_raqam):
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich=1
        self.__id_raqam=id_raqam
        Talaba.__talabalar_soni+=1
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        """Shaxs haqida to'liq ma'lumot qaytaruvchi metod"""
        info=f"{self.ism.title()} {self.familiya.title()}. "
        info+=f"{self.bosqich}-bosqich talabasi"
        return info
    
    def get_id(self):
        return self.__id_raqam
   
    def set_id(self,new_id):
        self.__id_raqam=new_id
    
    
    @classmethod #Klassga oid xususiyatlar bilan ishlash uchun maxsus metod
    def get_talabalarsoni(cls):
        return cls.__talabalar_soni
                    
    


# shaxs1=Shaxs("Ali", "Valiyev", "AA159753", 1998)
# talaba1=Talaba("Alisher", "Akramov", "AA357654", 2002, "000133")
# # print(talaba1.get_info())
# talaba1.set_id("00189357")

# shaxs2=Shaxs("akrom", "bo'riyev", "AB456987", 1999)

# shaxs3=Shaxs("akrom", "bo'riyev", "AB456987", 1999)
# shaxs4=Shaxs("akrom", "bo'riyev", "AB456987", 1999)
# shaxs5=Shaxs("akrom", "bo'riyev", "AB456987", 1999)
# shaxs6=Shaxs("akrom", "bo'riyev", "AB456987", 1999)



























