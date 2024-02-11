"""
@author: Abduljabbor
"""

"""AMALIYOT JAVOBLARI"""

savol="Sevimli kitobingiz kiriting "
savol+="Dasturni to'xtatish uchun 'Stop' deb yozing: "
ishora=True
kitobingiz=[]
while ishora:
    kitob=input(savol).title()
    if kitob == "Stop":
        ishora=False
    else:
        kitobingiz.append(kitob)
        print(kitobingiz)

# ishora usuli
ishora=True
while ishora:
    yosh=input("Yoshingizni kiriting: ").lower()
    if yosh:
        if yosh != "exit" and yosh != "quit":
            yosh=int(yosh)
            if yosh <7:
                narh=2000
            elif yosh<18:
                narh=3000
            elif yosh<65:
                narh=10000
            else:
                narh=0
            if narh==0:
                print("Sizga chipta bepul")
            else:
                print(f"Chipta narhi {narh} so'm")
        else:
            ishora=False
    else:
        print("Yosh kiritilmadi")
            
# shartni tekshirish usuli
# yosh=""      
# while yosh != "exit" and yosh !="quit":
#     yosh=input("Yoshingizni kiriting: ").lower()
#     if yosh:
#         if yosh != "exit" and yosh != "quit":
#             yosh=int(yosh)
#             if yosh<7:
#                 narh=2000
#             elif yosh<18:
#                 narh=3000
#             elif yosh<65:
#                 narh=10000
#             else:
#                 narh=0
#             if narh==0:
#                 print("Sizga chipta bepul")
#             else:
#                 print(f"Chipta narhi {narh} so'm")
#     else:
#         print("Yosh kiritilmadi")

# # break usuli
# while True:
#     yosh=input("Yoshingizni kiriting: ").lower()
#     if yosh:
#         if yosh != "exit" and yosh !="quit":
#             yosh=float(yosh)
#             if yosh <7:
#                 narh=2000
#             elif yosh <18:
#                 narh=3000
#             elif yosh <65:
#                 narh=10000
#             else:
#                 narh=0
#             if narh==0:
#                 print("Sizga chipta bepul")
#             else:
#                 print(f"Chipta narhi {narh} so'm")
#         else:
#             break
#     else:
#         print("Yosh kiritilmadi")

savol ="\nKiritilgan sonning ildizini qaytaruvchi dastur"
savol += "\nMusbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol).title()
    if qiymat=='Exit':
        break
    elif float(qiymat)<=0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"\n{qiymat} ning ildizi {ildiz} ga teng")







