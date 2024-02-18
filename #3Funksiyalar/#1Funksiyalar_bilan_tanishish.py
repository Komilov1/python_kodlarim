"""
@author: Abduljabbor

Funksiya bilan tanishish
"""

def tyil_hisobla(ism,yosh):
    """Foydalanuvchini yoshini hisoblash"""
    print(f"{ism.title()} {2024-yosh}-yilda tug'ilgan")

# tyil_hisobla("olim", 25)


def kvadrat_kub_hisobla(son):
    """Foydalanuvchidan son olib, uning kvadrati
        va kubini konsolga chiqaruvchi funksiya """
    print(f"{son} ning kvadrati {son**2}")
    print(f"kubi esa {son**3}")


# kvadrat_kub_hisobla(2)

def juft_toq(son):
    """Foydalanuvchidan son olib, son juft
        yoki toqligini konsolga chiqaruvchi funksiya """
    if son%2==0:
        print("juft son")
    else:
        print("toq son")


def katta_kichik(x,y):
    """Foydalanuvchidan ikkita son olib,
        ulardan kattasini konsolga chiqaruvchi funksiya"""
    if x<y:
        print(f"{x}<{y}")
    elif x>y:
        print(f"{x}>{y}")
    else:
        print(f"sonlar teng")

def daraja_hisobla(x,y=2):
    """Berilgan 'x' ning 'y' darajasini hisoblaydi """
    print(f"{x} ning {y} darajasi {x**y}")

def bolinish_alomatlari(son):
    """Foydalanuvchidan son qabul qilib,
    sonni 2 dan 10 gacha bo'lgan sonlarga
    qoldiqsiz bo'linishini tekshiruvchi funksiya """
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n}ga qoldiqsiz bo'linadi")
            

bolinish_alomatlari(80)







