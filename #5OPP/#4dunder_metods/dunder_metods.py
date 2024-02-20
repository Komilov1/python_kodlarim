"""
@author: Asus
"""

class Avto:
    """Avto klassi"""
    def __init__(self,konpanya,model,rang,yil,narh):
        self.konpaniya=konpanya
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=0

    # def __str__(self): #obyektni tushinarli qilib qaytaradi
    #     return f"Atvo:{self.konpaniya} {self.model}"

    def __repr__(self): #bu metod yuqoridagi str metodidan avzalroq
        """Avto klassidan yaratilgan obyektni malumotini tushunarli qilib ko'rsatadi"""
        return f"Atvo:{self.konpaniya} {self.model}"

    def __eq__(self, o): #tenglikni tekshiradi __ne__ buning aksi
        return self.narh==o.narh 
    
    def __lt__(self,o): # kichiklikni tekshirish __gt__ buning aksi
        return self.narh < o.narh
    
    def __le__(self,o): #kichik yoki teng __ge__ buning aksi
        return self.narh>=o.narh
    
    
    
    
class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self,nomi):
        self.nomi=nomi
        self.avtolar=[]
        
    def __repr__(self):
        """Avtosalon klassidan yaratilgan obyektni malumotini tushunarli qilib ko'rsatadi"""
        return f"{self.nomi} avtosaloni"
    
    def add_avto(self,*qiymat):
        """Avtosalon klassiga cheksiz avto qo'shadi"""
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto abketini kiriting")
            
    def __len__(self):
        """obyekdagi avtolar listini uzunligini o'lchaydi"""
        return len(self.avtolar)

    def __getitem__(self,index):
        """obyektni indexdagi ma'lumootini ko'rsatadi"""
        return self.avtolar[index]
    
    def __setitem__(self,index,avto):
        """berilgan obyektga boshqa yangi obyekt yuklaydi"""
        if isinstance(avto, Avto):
            self.avtolar[index]=avto
            
    def __add__(self,qiymat):
        """ikki obyektni birlashtirib uchinchi obyekt yaratadi"""
        if isinstance(qiymat, Avtosalon):
            yangi_salon=Avtosalon(f"{self.nomi} {qiymat.nomi}")
            yangi_salon.avtolar=self.avtolar+qiymat.avtolar
            return yangi_salon
            
                

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

salon1=Avtosalon("Madad")
salon1.add_avto(avto1,avto2,avto3)

salon2=Avtosalon("max")
salon2.add_avto(avto4,avto5,avto6)

salon3=salon1+salon2




class  Shaxs:
    """Shaxs haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        
    def __repr__(self):
        return f"Shaxs {self.ism} {self.familiya}"
    
    def __eq__(self, y):
        return self.tyil==y.tyil
        
    def __lt__(self,y):
        return self.tyil<y.tyil
    
    def __le__(self,y):
        return self.tyil<=y.tyil
    
    def get_info(self):
        """Shaxs haqida to'liq ma'lumot qaytaruvchi metod"""
        info=f"{self.ism.title()} {self.familiya.title()}. "
        info+=f"passport:{self.passport.upper()} {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil-self.tyil


class Talaba(Shaxs):
    """Talaba haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil, id_raqam):
        super().__init__(ism, familiya, passport, tyil)
        self.id_raqam=id_raqam
        self.bosqich=1
        self.fanlar=[]
    
    def __repr__(self):
        return f"Talaba {self.ism} {self.familiya}"
    
    def __eq__(self, y):
        return self.bosqich==y.bosqich
        
    def __lt__(self,y):
        return self.bosqich<y.bosiqich
    
    def __le__(self,y):
        return self.bosqich<=y.bosqich
        
    
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
    
    def set_bosqich(self,yangi_bosqich):
        self.bosqich=yangi_bosqich

class Fan:
    """Fan klassi"""
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar=[]
    
    def __repr__(self):
        return  self.nomi
    
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        
    def __getitem__(self,index):
        return self.talabalar[index]
    
    def __setitem__(self,index,new_value):
        self.talabalar[index]=new_value
        
    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self,new_value):
        self.talabalar.append(new_value)
        
    def __sub__(self,n):
        for talaba in self.talabalar:
            if n in talaba.passport or n in talaba.id_raqam:
                self.talabalar.remove(talaba)
        
    def __call__(self,*value):
        if value:
            for talaba in value:
                if isinstance(talaba, Talaba):
                    self.talabalar.append(talaba)
        else:
            return [talaba for talaba in self.talabalar]
                

talaba1=Talaba("Olim", "Ergashev","AA951258",2003,"0001478") 
talaba2=Talaba("Qosim", "Alimov", "AB659820", 2003, "0001479")  
talaba3=Talaba("Odil", "jurayev", "AB237964", 2004, "0001480")  
talaba4=Talaba("Tolib", "Botirov", "AC934558", 2005, "0001481")   
fan1=Fan("matematika")  
fan2=Fan("fizika")
fan3=Fan("kimyo")

fan1+talaba1
fan1+talaba2
fan1+talaba3

fan1-"0001479"
























