"""
@author: Abduljabbor
"""
import random


def sontop(x=10):
    print(f"1 dan {x} gacha son o'yladim topa olasizmi?")
    taxminiy_son=random.randint(1, x)
    taxminlar=0
    while True:
        taxminlar+=1
        javob=int(input(">>>"))
        if javob>taxminiy_son:
            print("Xato men o'ylagan son bundan kichikroq")
        elif javob<taxminiy_son:
            print("Xato men o'ylagan son bundan kattaroq")
        else:
            break
        
    print(f"{taxminiy_son} sonini o'ylagan edim {taxminlar} ta taxmin bilan topdingiz")
    return taxminlar

def sontop_pc(x=10):
    input(f"1da {x} gacha son o'ylang men topaman\n"
          "o'ylagan bo'lsangiz istalgan tugmani bosing")
    quyi=1
    yuqori=x
    taxminlar=0
    while True:
        taxminlar+=1
        if quyi!=yuqori:
            taxminiy_son=random.randint(quyi, yuqori)
            javob=input(f"{taxminiy_son} sonini o'yladingizmi,to'g'ri bo'sa(t)ni bosin,kattaroq(+),kichikroq(-)")
            if javob=="-":
                yuqori=taxminiy_son-1
            elif javob=="+":
                quyi=taxminiy_son+1
            else:
                break
        else:
            break
    print(f"{taxminlar} ta urunishda topdim")
    return taxminlar

def play(x=10):
    yana=True
    while yana:
        taxmin_user=sontop(x)
        taxmin_pc=sontop_pc(x)
        if taxmin_user>taxmin_pc:
            print(f"{taxmin_pc} ta taxmin bilan topdim yutdim")
        elif taxmin_user<taxmin_pc:
            print(f"{taxmin_user} ta taxmin bilan topdingiz va yutdingiz")
        else:
            print("durrang")

        yana=int(input("Yana o'ynaysizmi ha(1),yo'q(0)"))
        


























