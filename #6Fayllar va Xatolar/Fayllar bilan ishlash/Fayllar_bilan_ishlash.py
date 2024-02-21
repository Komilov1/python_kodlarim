# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:20:40 2024

@author: Asus
"""
fayl_nomi="faylni_ochish.txt"

info="faylni ochish uchun file=open(\"file name\")"
info+="ammo bunday qilish maslahat berilmaydi hosh unda qanday yo'li bor with opertoridan foydalanamiz"


# faly= open("faylni_ochish.txt")
# file=faly.read()
# faly.close()

# print(file)

# with open("faylni_ochish.txt") as fayl: #fayl with operatori yankunlanguncha ochiq holada turadi va avtomat tarzda yopiladi
#     malumot=fayl.read()
    
# print(malumot)

# with open(fayl_nomi,"w") as faly:
#     faly.write(info)
    
# with open(fayl_nomi,"r") as faly:
#     malumot=faly.read()

# print(malumot)


def tyil_in_pi(tyil):
    with open("C:/Users/Asus/Downloads/pi_million_digits.txt","r") as fayl:
        file=fayl.read()
        if str(tyil) in file:
            print("ha")
        else:
            print("yo'q")

with open("C:/Users/Asus/Downloads/pi_million_digits.txt",) as file:
    fayl=file.read()
    
fayl.rstrip()
fayl.replace("\n", "")
fayl.replace(" ", "")
fayl.float(fayl)



while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book:
        break
    with open("amaliyot/books.txt", "a") as file:
        file.write(book + "\n")

# users("Ism Abduljabbor","Familiya Komilov")























