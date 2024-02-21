# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:52:46 2024

@author: Asus
"""

# yosh = input("Yoshingizni kiriting: ")
# yosh=int(yosh)
# print(f"siz {2024-yosh}-yilda tug'ilgansiz")

# Xatolikni try except orqali tutib olish
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh=int(yosh)
# except:
#     print("butun son kiritmadingiz")
# else:
#     print(f"siz {2024-yosh}-yilda tug'ilgansiz")

# try except va else 
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")

# MA'LUM TURDAGI XATOLARNI USHLASH
# yosh=input("Yoshingizni kiriting: ")
# try:
#     yosh=int(yosh)
# except ValueError: #faqat ValueError xatoligini tutish
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")

    
#ZeroDivisionError
# x,y=5,10

# try:
#     y/(x-2)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")

# mevalar = ['olma','anor','anjir','uzum']
# index=5
# try:
#     mevalar[index-1]
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta element bor xolos")
# except TypeError:
#     print("butun son kiriting")
# else:
#     print(mevalar[index-1])



# 

# foydalanuvchi={"ism":"Ali",
#                "familiya":"Valiyev",
#                "tyil":2002,
#                "email":"valiyev01@gmail.com"
#                }

# key="gmail"
# try:
#     print("Foydalanuvchi",foydalanuvchi[key])
# except KeyError:
#     print('Bunday kalit mavjud emas!')


# try:
#     x = int(input("son kiriting: "))
#     y = int(input("yana son kiriting: "))
#     print(x, "/", y, "=", x / y)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# except ValueError:
#     print("Bu son emas")
# except:
#     print("Xato yuz berdi!")



# print("x/y hisoblovchi dastur ")

# while True:
#     x=input("x ni kiriting: ")
#     if x.isdigit():
#         x=int(x)
#     else:
#         print("butun son kiriting")
#         continue
    
#     y=input("y ni kiriting: ")
#     if y.isdigit():
#         y=int(y)
#     else:
#         print("butun son kiriting")
#         continue
    
#     if y==0:
#         print("0 ga bo'lib bo'lmaydi")
#     else:
#         print(x,"/",y,"=",x/y)
#         break


import json

files = ["talaba1.json", "talaba2.json", "talaba3.json", "talaba4.json"]

for filename in files:
    try:
        with open(filename) as  f:
            talaba=json.load(f)
    except FileNotFoundError:
        print(f"{filename} fayli mavjud emas")
        
    else:
        print(talaba['ism'])





















