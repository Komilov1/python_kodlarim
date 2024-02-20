# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:42:48 2024

@author: Asus
"""
 

class  Shaxs:
    """Shaxs haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        
    def get_info(self):
        """Shaxs haqida to'liq ma'lumot qaytaruvchi metod"""
        info=f"{self.ism.title()} {self.familiya.title()}. "
        info+=f"passport:{self.passport.upper()} {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil-self.tyil

inson=Shaxs("Odil", "oripov", "ab156885", 1999)

class Manzil:
    """Talabaning manzilini qaytaradi"""
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat
    
    def get_manzil(self):
        info=f"{self.viloyat} viloyati {self.tuman} tumani "
        info+=f"{self.kocha} ko'chasi {self.uy}-uy "
        
        return info


class Talaba(Shaxs):
    """Talaba haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil, id_raqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.id_raqam=id_raqam
        self.bosqich=1
        self.manzil=manzil
        self.fanlar=[]
    def get_id(self):
        return self.id_raqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        """Shaxs haqida to'liq ma'lumot qaytaruvchi metod"""
        info=f"{self.ism.title()} {self.familiya.title()}. "
        info+=f"{self.bosqich}-bosqich id raqami {self.id_raqam}"
        return info
    
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
    
    def remove_fan(self,fan):
        return self.fanlar.remove(fan) if fan in self.fanlar else print("Siz bu fanga yozilmagansiz")
    
    def get_fanlar(self):
        return [fan.nomi for fan in self.fanlar]
    
class Fan:
    def __init__(self,nomi):
        self.nomi=nomi

# talaba1_manzil=Manzil(75, "Tayanch", "Furqat", "Farg'ona")
# talaba1=Talaba("Erkin", "Turg'unov", "aa155996", 2001, "000023",talaba1_manzil)        

# fan1=Fan("Fizika")
# fan2=Fan("Kimyo")
# fan3=Fan("Matematika")

# talaba2_manzil=Manzil(22, 'olmazor', "Beshariq", "Farg'ona")
# talaba2=Talaba("Alisher", "Ahmedov", "AA558669", 2004, "000073", talaba2_manzil)

# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)

# talaba2.fanga_yozil(fan1)
# talaba2.fanga_yozil(fan2)
# talaba2.fanga_yozil(fan3)

# talaba2.remove_fan(fan3)
# talaba2.remove_fan(fan3)

class Ishchi(Shaxs):
    """Ishchi klass"""
    def __init__(self, ism, familiya, passport, tyil,ish_joyi,lavozim):
        super().__init__(ism, familiya, passport, tyil)
        self.ish_joyi=ish_joyi
        self.lavozim=lavozim
    def get_ishjoyi(self):
        return self.ish_joyi
    def get_lavozim(self):
        return self.lavozim
    def get_info(self):
        info=f"{self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilgan "
        info+=f"ish joyi {self.ish_joyi} lavozimi {self.lavozim}"
        return info    
    def set_lavozim(self,lavozim):
        self.lavozim=lavozim
        
    def set_ishjoyi(self,ish):
        self.ish_joyi=ish
    
    

class Foydalanuvchi(Shaxs):
    """Foydalanuvchi haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil,email,tel_raqam):
        super().__init__(ism, familiya, passport, tyil)
        self.email=email
        self.tel_raqam=tel_raqam
    def get_email(self):
        return self.email
    def get_tel(self):
        return self.tel_raqam
    def get_info(self):
        info=f"{self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilgan "
        info+=f"email manzili {self.email} telefon raqami {self.tel_raqam}"
        return info   
        
class Hamkor(Shaxs):
    """Hamkorlar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil,tashkilot,vazifalar):
        super().__init__(ism, familiya, passport, tyil)
        self.tashkilot=tashkilot
        self.vazifalar=vazifalar
    def get_tashkilot(self):
        return self.tashkilot
    def get_vazifalar(self):
        return self.vazifalar
    def get_info(self):
        info=f"{self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilgan "
        info+=f"{self.tashkilot} tashkilot ish boshqaruvchisi, vazifasi {self.vazifalar}"
        return info   
        
class Mijoz(Shaxs):
    """Mijozlar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil,buyurtmalar,haridor_turi):
        super().__init__(ism, familiya, passport, tyil)
        self.buyurtmalar=buyurtmalar
        self.haridor_turi=haridor_turi
    def get_buyurtma(self):
        return self.buyurtmalar
    def get_mijoz_turi(self):
        return self.haridor_turi
    def get_info(self):
        info=f"{self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilgan, "
        info+=f"buyutmalari '{self.buyurtmalar}' haridor turi {self.haridor_turi}"
        return info   



# ishchi1=Ishchi("Akom", "Alimov", "AA111111", 1975,"maktab","qorovul")    
# user1=Foydalanuvchi("qosim", "tursunov", "AB1478935", 2001, "tursunov@gmail.com", 998901234567)
# hamkor1=Hamkor("sherzod", "to'ychiyev", "AB3597486", 1994, "madad mchj", "bozor talabini o'rganish")
# mijoz1=Mijoz("temur", "qudratov", "AB99614523", 1999, "qurulish mahsulotlari", "doimiy")  

# ishchi1.set_ishjoyi("magazin")

# ishchi1.set_lavozim("sotuvchi")

class Admin(Foydalanuvchi):
    """Admin klass"""
    def __init__(self, ism, familiya, passport, tyil, email, tel_raqam,admin):
        super().__init__(ism, familiya, passport, tyil, email, tel_raqam)
        self.admin=admin
        self.spam=[]
    
    def ban_user(self,user):
        self.spam.append(user)
        return f"Foydalanuvchi bloklandi"

# admin=Admin("max", "ulmiz", "AA753159", 1998, "max@email.com", 998905614798,"max")

# admin.ban_user(user1)






























