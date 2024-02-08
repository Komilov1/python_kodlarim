"""
LUG'AT ELEMENTLARI BILAN ISHLASH'
"""

car0={}

car0['model']="spark"
car0['yili']=2011
car0['rang']="oq"
car0['yurgani']=35000
car0['karobka']="mexanik"

for key,value in car0.items():
    print(f"{key} {value}")

izohli_lugat={
    "string":"malumotni matn turi",
    "integer":"malumotni butun son turi",
    "float":"malumotni o'nlik son turi",
    "list":"malumotni ro'yxat ko'rinishda saqlash",
    "for":"loop takrorlash",
    "if":"tarmoqlanish agar shartini bajaradi",
    "elif":"aksholda agar shartini tekshiradi",
    "else":"aksholda shartini bajaradi",
    }
for key,value in sorted(izohli_lugat.items()):
    print(f"{key}:{value}")

davlatlar={}
davlatlar["Aqsh"]="Washington"
davlatlar["Turkiya"]="Anqara"
davlatlar["Germanya"]="Berlin"
davlatlar["Fransiya"]="Parij"
davlatlar["Rossiya"]="Moskva"
davlatlar["Xitoy"]="Pekin"

for davlat in sorted(davlatlar.keys()):
    print(davlat.title())

for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

davlat=input("istalgan davlatni kiriting>>>").title()
print(davlatlar.get(davlat,"bunday davlat ro'yxatda mavjud emas"))

if davlat in davlatlar:
    print(f"{davlat}ning poytaxti {davlatlar[davlat]}")
else:
    print(f"{davlat} degan davlat ro'yxatda mavjud emas")

taom_menyu={
    "osh":20000,
    "sho'rva":18000,
    "chuchvara":19000,
    "somsa":8000,
    "manti":20000,
    "qiyma_kabob":12000,
    "burda_kabob":18000,
    "qozon_kabob":25000,
    "norin":25000,
    "mastava":17000
    }

n=1
for taom in range(3):
    taom=input(f"{n}-qanday taom buyurma qilasiz>>>").lower()
    if taom in taom_menyu:
        print(f"{taom} narhi {taom_menyu[taom]}so'm")
    else:
        print(f"uzur bizda {taom} yo'q")
    n=n+1
    


















