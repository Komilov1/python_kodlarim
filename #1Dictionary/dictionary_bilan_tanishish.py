"""lugat bilan tanishamiz"""

car0={} #Bo'sh lug'at
car0["model"]='spark' 
car0["rang"]='oq'
car0["yurgani"]=35000
car0["narh"]=6500

del car0["yurgani"]
# print(car0)

# kalit=input("kalitni kiriting")
# car=car0.get(kalit,"bunday kalit mavjud emas")
# print(car)

otam={"ism":"Zafarjon","tyil":1975,"tugilgan":"Qo'qon shaxrida"}
onam={"ism":"Yulduzxon","tyil":1977,"tugilgan":"Qo'qon shaxrida"}
akam={"ism":"Abdulmo'min","tyil":1997,"tugilgan":"Qo'qon shaxrida"}
Abduljabbor={}
Abdulvohid={}
# print(f"Otamning ismi {otam['ism']} {otam['tyil']}-yilda {otam['tugilgan']}da tug'ilganlar")
# print(f"Onamning ismi {onam['ism']} {onam['tyil']}-yilda {onam['tugilgan']}da tug'ilganlar")
# print(f"Akamning ismi {akam['ism']} {akam['tyil']}-yilda {akam['tugilgan']}da tug'ilganlar")

otam["sevgan_taom"]="osh"
onam["sevgan_taom"]="manti"
akam["sevgan_taom"]="sho'rva"
Abduljabbor["sevgan_taom"]="chuchvara"
Abdulvohid["sevgan_taom"]="qozonkabob"

a=f"otamning sevgan otaomi {otam['sevgan_taom']}"
b=f"onamning sevgan taomi {onam['sevgan_taom']}"
c=f"akamning sevgan taomi {akam['sevgan_taom']}"
d=f"Abduljabborning sevgan taomi {Abduljabbor['sevgan_taom']}"
f=f"Abdulvohidning sevgan taomi {Abdulvohid['sevgan_taom']}"

izohli_lugat={
    "string":"malumotni matn turi",
    "integer":"malumotni butun son turi",
    "float":"malumotni o'nlik son turi",
    "list":"malumotni ro'yxat ko'rinishda saqlash",
    "for":"loop takrorlash",
    "if":"tarmoqlanish agar shartini bajaradi",
    "elif":"aksholda agar shrtini tekshiradi",
    "else":"aksholda shartini bajaradi",
    }
kalit=input("kalit so'zni kiriting: ")
# print(izohli_lugat.get(kalit,"bunday kalit mavjud emas"))
if kalit in izohli_lugat:
    print(izohli_lugat[kalit])
else:
    print("bunday kalit mavjud emas")        



