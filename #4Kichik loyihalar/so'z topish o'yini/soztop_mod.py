"""
@author: Abduljabbor
"""

import random
from uzwords import words

def get_word():
    tasodifiy_soz=random.choice(words)
    return tasodifiy_soz

# word=get_word()

def display(latters,word):
    
    borlar=""
    for x in word:
        if x in latters:
            borlar+=x
        else:
            borlar+="-"
    return borlar
    
        
def play():
    word=get_word()    
    latters=[]
    a=''
    print(f"Men {len(word)} harfli so'z o'yladim topa olasizmi?")
    print(display(latters, word))
    while latters!=word:

        latter=input("\nHarf kiriting>>>")
        if latter:
            if latter in a:
                print("Bu harfni avval kiritgansiz")
                
            if latter in word:
                a+=latter
                print(f"{latter} harfi to'g'ri ")
            else:
                print("bunday harf yo'q")
                a+=latter
        
        latters=display(a, word)
        print(latters)
        print(f"shu vaqtgacha kiritgan harflaringiz: {a}")
    print(f"Tabriklayman {len(a)} ta urunishda topdingiz")
    
