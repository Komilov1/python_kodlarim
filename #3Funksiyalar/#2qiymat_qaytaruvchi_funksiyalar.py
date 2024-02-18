"""
@author: Abduljabbor
Funksiyadan qiymat qaytarish
"""

def user_info(ism,familiya,tyil,tjoy,email='',tel=None):
    user={
        'ism':ism,
        'familiya':familiya,
        'tyil':tyil,
        'tjoy':tjoy,
        'email':email,
        'tel':tel
        }
    return user
            
print("Ijtimos mijozlar haqida ma'lumot bering")
mijozlar=[]
while True:
    ism=input("Ismi ")
    familiya=input("Familiyasi ")
    tyil=input("Tug'ilgan yili ")
    tjoy=input("Tug'ilgan joyi ")
    email=input("Email manzili ")
    tel=input("Telefon raqami ")
    mijozlar.append(user_info(ism, familiya, tyil, tjoy,email,tel))
    yana=input("Yana mijoz bormi (yes/no) ")
    if yana=='no':
        break
for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['tyil']}-yilda tug'ilgan, telefoni: {mijoz['tel']}"
    )


def big_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def aylana_info(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana

def tubson(a,b):
    tublar=[]
    for i in range(a,b+1):
        tub=True
        if i==1:
            tub=False
        elif i==2:
            tub= True
        else:
            for j in range(2,i):
                if i % j==0:
                    tub=False
                    
        if tub:
            tublar.append(i)
    return tublar

def fiboncci(x):
    fibon=[]
    for n in range(x):
        if n==0 or n==1:
            fibon.append(n)
        else:
            fibon.append(fibon[-1]+fibon[-2])
    return fibon































