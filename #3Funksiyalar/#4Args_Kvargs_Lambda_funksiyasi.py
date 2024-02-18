"""
@author: Abduljabbor

Moslashuvchan funksiyalar va Lambda nomsiz funksiya
"""

def multiplication(*numbers):#args  usuli
    yigindi=1
    for i in numbers:
        yigindi*=i
    return yigindi

def talabalar(ism,familiya,**qiymat):#kvargs usuli
    qiymat['ism']=ism
    qiymat['familiya']=familiya
    return qiymat

# talaba=talabalar("Ali", 'Valiyev',bosqich=4,idRaqam="011487" )

import math
uzunlik=lambda pi,r: 2*pi*r #aylana uzunligini o'lchovchi funksiya
# print(uzunlik(math.pi,9))

daraja=lambda x,y:x**y
# print(daraja(2,5))

# funksiya yasaydigan funksiya
def daraja1(n):
    return lambda x:x**n

kvadrat=daraja1(2)
kub=daraja1(3)
# print(f"3-ning kvadrati {kvadrat(3)} kubi {kub(3)} ga teng")

"""Lambda funksiyalaridan argument sifatida boshqa funksyani
 qabul qiluvchi funksiyalar bilan ishlashda ham keng foydalaniladi.
 Misol uchun map() va filter() funksiyalari.
"""

from math import sqrt

sonlar=list(range(11))
ildizlar=list(map(sqrt, sonlar))

# print(ildizlar)

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

# print(list(map(daraja2, sonlar))) 

kvadratlar=list(map(lambda x:x*x, sonlar))#yuqoridagi kodni lambda yordamida yozdim
# print(kvadratlar)

# map() funksiyasi bo'lmaganida biz bunday dasturlarni for yordamida yozishimiz kerak bo'lar edi:

kvadratlar = []
for son in sonlar:
    kvadratlar.append(son*son)
    
# map() funksiyasiga bir nechta ro'yxatlar ham uzatish mumkin:

a=[5,9,7]
b=[3,10,4]
a_plus_b=list(map(lambda x,y: x+y,a,b))
# print(a_plus_b)

# map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi:

ismlar=["Ali","Vali","Hasan","Husan","Olim","Erkin"]

# print(list(map(lambda ism:ism.upper() , ismlar)))

'''filter() Funksiyasi'''

import random as r

sonlar=r.sample(range(100), 10)

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0

juft_sonlar=list(filter(juftmi, sonlar))
# print(juft_sonlar)

# endi shu dasturni lambda yordamida yozaman

juft_sonlar1=list(filter(lambda x:x%2==0, sonlar))

# print(juft_sonlar1)

"""Kurib turganingizdek, lambda funksiya yordamida
 dastur bir muncha qisqaroq chiqadi. Agar juftmi funksiyasi
 kelajakda shart bo'lmasa, alohida funksiya yaratib o'tirmasdan,
 bir marttalik lambda funksiyasidan foydalangan afzal"""

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
# print(mevalar_b)

mevalar2=list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)

a_va_r=list(filter(lambda meva:(meva.startswith('a') and meva.endswith("r")), mevalar))
# print(a_va_r)

