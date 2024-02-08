"""
@author: Abduljabbor
"""

malibus=[]

for n in range(10):
    new_car={
        "model":"malibu",
        "rang":None,
        "yil":2024,
        "narh":None,
        "km":0,
        "karobka":"avto"
        }
    malibus.append(new_car)
    
for malibu in malibus[:3]:
    malibu["rang"]="oq"


for malibu in malibus[3:6]:
    malibu["rang"]="qora"

for malibu in malibus[6:]:
    malibu["rang"]="qizil"

for malibu in malibus[6:]:
    malibu["karobka"]="mexanika"
    
for malibu in malibus:
    if malibu['karobka']=="mexanika":
        malibu['narh']=35000
    else:
        malibu["narh"]=40000

# LUG'AT ICHIDA RO'YXAT
dasturchilar={
    "ali":["python","c++"],
    "vali":["php","sql"],
    "hasan":["html","css","js"],
    "husan":["python","php"],
    "maryam":["c++","c#"]
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quydagi dasturlash tillarni biladi",end=" ")
    for til in tillar:
        print(f"{til.upper()}",  end=" ")


hamkasblar={
    "ali":{"familiya":"valiyev",
           "tyil":1995,
           "malumoti":"oliy",
           "tillar":["python","c++"]
           },
    "vali":{"familiya":"aliyev",
           "tyil":2001,
           "malumoti":"o'rta_maxsus",
           "tillar":["html","css","js"]
           },
    "hasan":{"familiya":"husanov",
           "tyil":1999,
           "malumoti":"maxsus",
           "tillar":["python","php"]
           }
    }


for ism,info in hamkasblar.items():
    print(f"{ism.title()} {info['familiya'].title()} "
          f"{info['tyil']}-yilda tug'ilgan "
          f"malumoti {info['malumoti']}\n"
          "Quydagi dasturlash tillarini biladi")
    for til in info['tillar']:
        print(f"{til.upper()}")


shaxs0={"ism":"Abu Abdulloh Muhammad ibn Ismoil",
        "tyil":810,
        "tjoy":"Buxoro",
        "umr":"60",
        "asarlar":["Al-jome' as-sahih","Al-adab al-mufrad",
                            "At-tarix al-kabir","At-tarix as-sag'ir"]
        }
shaxs1={"ism":"Abdulla Qodiriy",
                "tyil":1894,
                "tjoy":"Toshkend",
                "umr":"44",
                
                }
shaxs2={"ism":"Erkin Vohidov",
        "tyil":1936,
        "tjoy":"Farg'ona",
        "umr":"80"
        }
shaxs3={"ism":"Alisher Navoiy",
        "tyil":1441,
        "tjoy":"Xirot",
        "umr":"60"
        }
shaxs1["asarlar"]=["O'tgan kunlar","Mehrobdan chayon","Obid ketmon"]
shaxs2["asarlar"]=["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
shaxs3["asarlar"]=["Xamsa","Lison ut-tayr","Mahbub Al-Qulub","Munojot"]
mashxur_shaxslar=[shaxs0,shaxs1,shaxs2,shaxs3]

for shaxs in mashxur_shaxslar:
    print(f"{shaxs['ism']} {shaxs['tyil']}"
          f"-yilda {shaxs['tjoy']}da tavallud topgan "
          f"{shaxs['umr']} yil umr ko'rgan")
     
for shaxs in mashxur_shaxslar:
    print(f"\n{shaxs['ism']} ning mashxur asarlari ")
    for asar in shaxs["asarlar"]:
        print(asar)

kinolar={
    "Nurislom":["Terminator","Ramo","Josus 007"],
    "Alisher":["Boyka","Qo'lga tushmas qasoskor","Rambo"],
    "Hasan":["Garri potter","O'rgumchak odam","Rokkiy"],
    "Ahmad":["Cho'qintirgan ota","Karib dengizi qaroqchilari","Robinzon kuruzo"]
    }

for ism,kinolar in kinolar.items():
    print(f"\n{ism}ning sevimli kinolari")
    for kino in kinolar:
        print(kino)


davlatlar={
    "Germaniya":{"poytaxti":"Berlin",
                 "aholisi":"84,4 million",
                 "hududi":'357021 km',
                 "pul":"euro",
                 "til":"Nemis tili"},
    "Xitoy":{"poytaxti":"Pekin",
                 "aholisi":"1,347,374,752 million",
                 "hududi":'9,596,962 km',
                 "pul":"Yuan",
                 "til":"Xitoy tili"},
    "Avstraliya":{"poytaxti":"Kanberra",
                 "aholisi":"26,510,600",
                 "hududi":'7,692,024 km',
                 "pul":"Avstraliya dollari",
                 "til":"Ingiliz tili"},
    "Aqsh":{"poytaxti":"Vashington",
                 "aholisi":"331 449 281[4]",
                 "hududi":'9 833 520[2] km',
                 "pul":"AQSh dollari",
                 "til":"Ingiliz tili"}
    }

for davlat,info in davlatlar.items():
       print(f"\n{davlat}ning poytaxti {info['poytaxti']}"
           f"\nHududi: {info['hududi']}"
           f"\nAholisi {info['aholisi']}"
           f"\nPul birligi {info['pul']}"
           f"\nRasmiy tili {info['til']}")

Davlat=input("Davlat nomini kiriting: ").title()

if Davlat in davlatlar:
        print(f"\n{Davlat}ning poytaxti {davlatlar[Davlat]['poytaxti']}"
                f"\nHududi: {davlatlar[Davlat]['hududi']}"
                f"\nAholisi: {davlatlar[Davlat]['aholisi']}"
                f"\nPul birligi: {davlatlar[Davlat]['pul']}"
                f"\nRasmiy tili {davlatlar[Davlat]['til']}")
else:
    print("Bizda bu davlat haqida malumot mavjud emas")













