"""
@author: Abduljabbor

while, Ro'yxatlar va Lug'atlar"""


ismlar = []
print("Yaqin do'stlaringizni ro'yxatini tuzamiz")
n=1
while True:
    salvol=f"{n}-do'stingizni ismini kiriting: "
    dost=input(salvol)
    ismlar.append(dost.title())
    takrorlash=input("Yana ism qo'shasizmi (ha/yo'q)")
    if takrorlash == "ha":
        n+=1
        continue
    else:
        break
print("\nDo'stlaringiz ro'yxati")
for ism in ismlar:
    print(ism.title())

buyurtmalar=[]
n=1
while True:
    salvol=f"{n}-buyurtmangizni kiriting: "
    buyurta=input(salvol)
    buyurtmalar.append(buyurta)
    loop=input("Yana buyurtma qo'shasizmi (ha/yo'q)")
    if loop == "ha":
        n+=1
        continue
    else:
        break
print("\nQuydagi mahsulotlarni buyurtma qildingiz")
for buyurta in buyurtmalar:
    print(buyurta)


print("Elektron bozorga mahsulot joylang")
mahsulotlar={}
ishora=True
while ishora:
    savol=f"Mahsulotingizni kiriting: "
    mahsulot=input(savol)
    narh=f"{mahsulot}ni narhini kiriting: "
    narh=float(input(narh))
    mahsulotlar[mahsulot]=narh
    takrorlash=input("Yana mahsulot qo'shasizmi (ha/yo'q): ")
    if takrorlash=="ha":
        continue
    else:
        ishora=False
     
for mahsulot,narh in mahsulotlar.items():
    print(f"{mahsulot}-{narh}")
buyurtmalar=['banan','olma','uzum','anjir']
mahsulotlar={"olma":5000,
              "anor":10000,
              "uzum":15000,
              "banan":23000}
while buyurtmalar:
    buyurtma=buyurtmalar.pop()    
    if buyurtma in mahsulotlar:
        narh=mahsulotlar[buyurtma]
        print(f"{buyurtma} narhi {narh} so'm")
    else:
        print(f"Bizda {buyurtma} mahsuloti yo'q")
    


























