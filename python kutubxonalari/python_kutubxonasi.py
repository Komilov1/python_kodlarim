"""
@author: Abduljabbor
"""

import datetime as dt
import re

bugun=dt.date.today()
ikki_hafta=dt.date (2024,2,23)
farq=ikki_hafta-bugun
for n in range(10):
    print(ikki_hafta )
    ikki_hafta +=farq

ramazon=dt.date(2024,3,11)
qoldi=ramazon-bugun
# print (f"Ramazonga tahminan {qoldi.days} kun qoldi")
# print (f"Qurbon Hayitiga tahminan {qoldi.days+70} kun qoldi")

tyil=dt.date(1998,9,7)
kun=bugun-tyil
oy=kun/30
yil=oy/12
print (f"Tug'ilgan kinimdan bugungi kungacha {yil.days} yil, {oy.days} oy, {kun.days} kun o'tdi")


andoza="^\+[1-9]\d{1,14}$"
phone_number=input("\ntelehon raqamingizni kiriting:  ")

if re.match(andoza, phone_number):
    print("Telefon raqam qabul  qilindi")
else:
    print("telefon raqam noto'g'ri")

matn="""Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi:
    https://www.youtube.com/watch?v=vsxJPRLXpgI 
    Ushbu darsimizda unittest moduli yordamida klasslarning
    xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz.
    Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""  
def regUlr(matn):
    andoza= r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/[-\w./#?]*(?i:[.](?:txt|pdf|doc|docx))?"
    veb_manzil=re.findall(andoza, matn)
    return veb_manzil
    
print(regUlr(matn))

























