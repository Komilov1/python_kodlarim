"""
@author: Abduljabbor

Funksiyaga ro'yxat uzatish'
"""

def katta_harf(List):
    katta=[]
    for n in List:
        katta.append(n.title())
    return katta
        
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

def bahola(ismlar):
    baholar = {}
    for n in ismlar:
        ism = n
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)

















