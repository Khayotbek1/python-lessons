# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:00:58 2024

@author: Khayotbek
"""

# =============================================================================
# def salom_ber(ism, familya):
#     """Foydalanuvchini ismini qabul qilib, unga salom beruvchi funksiya """
#     toliq_ism = f"Assalomu aleykum, Hurmatli {ism.title()} {familya.title()}"
#     return toliq_ism
#     
# talaba = salom_ber('khayotbek', 'razzoqov')
# talaba1 = salom_ber('doston', 'khamidjonov')
# talaba2 = salom_ber('jalol', 'xolmatjonov')
# print(f"{talaba}, {talaba1}, {talaba2}")
# =============================================================================


def salom_ber(familya, ism, otasining_ismi=''):
    if otasining_ismi:
        toliq_ism = f"{familya} {ism} {otasining_ismi}"
    else:
        toliq_ism = f"{familya} {ism}"
    return toliq_ism.title()

talaba = salom_ber('razzoqov', 'khayotbek', 'xasanovich')
talaba2 = salom_ber('xolmatov', 'jalol')

print(f"{talaba}, {talaba2} ") 



def oraliq (min,max,qadam=None):
    sonlar = []
    while min<max:
        if qadam:
            sonlar.append(min)
            min += qadam
        else:
            sonlar.append(min)
            min += 1 
            
    return sonlar


sana = oraliq(0,10,)
sana1 = oraliq(10,21,3)

print(f"{sana} {sana1}")
            