# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:51:14 2024

@author: Asus
"""
import json

sonlar=(1,2,3,4,5,6)
sonlar_json=json.dumps(sonlar)
sonlar2=json.loads(sonlar_json)


son1=501
son2=5.01

son_json=json.dumps(son1)
son_json2=json.dumps(son2)

son3=json.loads(son_json)
son4=json.loads(son_json2)


data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json=json.dumps(data)
# print(data_json)

data2=json.loads(data_json)

talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
ism=talaba_json["ism"]
familiya=talaba_json["familiya"]
# print(ism,familiya)

with open("data_json","w") as f:
    json.dump(data,f)

with open("talaba_json","w") as f:
    json.dump(talaba_json, f)


with open("C:/Users/Asus/Downloads/students.json") as f:
    talabalar=json.load(f)

for talaba in talabalar['student']:
    info=f"{talaba['name']} {talaba['lastname']} "
    info+=f"{talaba['year']}-kurs {talaba['faculty']} "
    info+=f"fakultet talabasi"
    # print(info)

with open("C:/Users/Asus/Downloads/api-result.json")as f:
    python_maqola=json.load(f)

title=python_maqola["query"]['pages']['13801']["title"]
extract=python_maqola["query"]['pages']['13801']["extract"]
# print(title)
# print(extract)


    





























