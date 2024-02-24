"""
@author: Asus
"""

import re

andoza="[A-Za-z]"
matn="""FIFA tomonidan tashkil etilgan birinchi jahon chempionati.
 Turnir 1930-yil 13–30-iyul kunlari Urugvayda boʻlib oʻtgan. Birinchi jahon chempionatini
 oʻtkazish toʻgʻrisidagi qaror 1928-yil 26-mayda FIFA tomonidan qabul qilingan va 1929-yil
 18-mayda Urugvay davlati ovoz berish yoʻli bilan mezbon sifatida tanlab olingan.
 Birinchi jahon chempionatining barcha oʻyinlari Urugvay poytaxti — Montevideoda boʻlib oʻtgan.
 Montevideoda jahon chempionati uchun 90 000 tomoshabinga moʻljallangan Centenario stadioni qurilgan.
 Musobaqaga FIFAga aʼzo barcha davlatlar taklif qilingan. Biroq, bor-yoʻgʻi 13 ta jamoa
 musobaqada ishtirok etish uchun Urugvayga borgan: Janubiy Amerikadan yettita,
 Yevropadan toʻrtta va Shimoliy Amerikadan ikkita jamoa. Yevropa jamoalarining soni kamligi
 XX asrning birinchi yarmida Janubiy Amerikaga borish qiyin boʻlganligi bilan izohlangan.
 Qurʼa natijalariga koʻra jamoalar toʻrt guruhga boʻlingan. Har bir guruh gʻoliblari pley-off
 bosqichiga yoʻl olishdi. Jahon chempionatlari tarixidagi dastlabki ikki uchrashuv bir vaqtda boshlandi.
 Ularda Fransiya va AQSH mos ravishda Meksikani 4:1, Belgiyani 3:0 hisobida magʻlub etgan.
 Fransiyalik Lucien Laurent jahon chempionati tarixidagi ilk gol muallifi hisoblanadi."""


harf=re.findall(andoza, matn)
katta_harflar=[]
kichik_harflar=[]

for x in harf:
    if re.match("[A-Z]",x):
        if x not in katta_harflar:
            katta_harflar.append(x)
            katta_harflar=sorted(katta_harflar)
    elif re.match("[a-z]", x):
        if x not in kichik_harflar:
            kichik_harflar.append(x)
            kichik_harflar=sorted(kichik_harflar)
# print(katta_harflar)        
# print(len(kichik_harflar))
# print(re.findall(andoza, matn))

def telefon_raqam_qabul(number):
    number=str(number)
    uzb_phone_num="^[\+]?[(]?[8-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    if re.match(uzb_phone_num, number):
        print("telefon raqamingiz qabul qilindi")
    else:
        print("telefon raqam noto'g'ri")

telefon_raqam_qabul(+998905614795)









