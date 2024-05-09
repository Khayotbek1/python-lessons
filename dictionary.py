# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:05:21 2024

@author: Khayotbek 
"""

# =============================================================================
# car = {'model': 'ferrari', 'rang': 'oq'}
# print(car ['model'])
# print(car ['rang'])
# 
# =============================================================================

# =============================================================================
# talaba_0 = {'ism': 'murod', 'yosh':20, 't_yil':1997}
# 
# print(f"{talaba_0 ['ism'].title()}, {talaba_0 ['t_yil']}-yilda tug'ilgan', {talaba_0 ['yosh']} yoshda")

#  Yangi kalit so'z va qiymat qo'shish
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'
# 
# print(talaba_0)
# =============================================================================


#Bo'sh lug'at =============================================================================
# talaba_1 = {}
# 
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 2
# talaba_1['yosh'] = 25
# print(talaba_1)
# print(f"Talaba {talaba_1 ['ism'].title()}, {talaba_1 ['kurs']}- kurs, {talaba_1 ['yosh']} yosh")
# =============================================================================

#kalit so'z-qiymat ni o'chirib tashlash =============================================================================
# talaba_0 = {'ism': 'murod', 'yosh':20, 't_yil':1997}
# 
# del talaba_0['yosh']
# print(talaba_0)
# =============================================================================

# =============================================================================
# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'samsung',
#     'olim': 'redmi',
#     'anvar': 'nokia'
#         }
# print(telefonlar['anvar'])
# =============================================================================

#get methodi =============================================================================
# mevalar = {
#         'apple': 'olma',
#         'cherry': 'gilos',
#         'lemon': 'limon'
#         }
# meva = mevalar.get('peach', 'Bunday meva mavjud emas')
# print(meva)
# =============================================================================

#items methodi


# =============================================================================
# talaba_1 = {}
#  
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 2
# talaba_1['yosh'] = 25
# 
# print(talaba_1.items())
# 
# for key, value in talaba_1.items():
#     print(f"key: {key}")
#     print(f"value: {value}\n")
# =============================================================================

#for tsikl items() methodi bilan =============================================================================
# telefonlar = {
#      'ali': 'iphone x',
#      'vali': 'samsung',
#      'olim': 'redmi',
#      'anvar': 'nokia'
#      }
# 
# for k, v in telefonlar.items():
#     print(f"{k.title()}ning telefoni {v}")
# =============================================================================


# =============================================================================
# mevalar = {
#         'olma': 10000,
#         'anjir': 20000,
#         'gilos': 25000,
#         'uzum': 32000,
#         'anor': 15000
#         }
# =============================================================================
# =============================================================================
# print(mevalar.keys())
# print("Do'kondagi mahsulotlar")
# 
# for meva in mevalar.keys():
#     print(meva.title())
# 
# =============================================================================

# =============================================================================
# bozorlik = ['anor', 'behi', 'olma', 'uzum']
# 
# for meva in mevalar:
#     if meva in bozorlik:
#         print(f"{meva.title()} {mevalar[meva]} so'm")
#         
# for mahsulot in bozorlik:
#     if mahsulot not in mevalar:
#         print(f"Iltimos do'koningizga {mahsulot} ham olib keling!")
# =============================================================================

# sorted() methodi orqali ro'yxatni alifbo boyicha taxlash =============================================================================
# mevalar = {
#         'olma': 10000,
#         'anjir': 20000,
#         'gilos': 25000,
#         'uzum': 32000,
#         'anor': 15000
#         }
# 
# 
# print("Do'koningizdagi mahsulotlar")
# 
# for meva in sorted(mevalar):
#     print(meva.title())
# =============================================================================


#values() methodi =============================================================================
# mevalar = {
#         'olma': 10000,
#         'anjir': 20000,
#         'gilos': 25000,
#         'uzum': 32000,
#         'anor': 15000
#         }
# 
# print(mevalar.values() )
# =============================================================================



# =============================================================================
# telefonlar = {
#       'ali': 'iphone x',
#       'vali': 'samsung',
#       'olim': 'redmi',
#       'anvar': 'nokia'
#       }
# 
# print("Foydalanuvchilar quyidagi telefonlarni ishlatadi")
# 
# for tel in telefonlar.values():
#     print(tel)
# =============================================================================

#set funksiyasi set bu ro'yxatda takrorlangan so'zlarni takror chiqarmaydi SETS ma'lumot turi  =============================================================================
# telefonlar = {
#       'ali': 'iphone x',
#       'vali': 'samsung',
#       'olim': 'redmi',
#       'anvar': 'nokia',
#       'hayot': 'iphone x',
#       'doston': 'samsung',
#       'jalol': 'honor',
#       'sherzod': 'huawei',
#       'begzod': 'apple'
#       } 
# print("Foydalanuvchilar quyidagi telefonlarni ishlatadi")
# for tel in sorted(set(telefonlar.values())):
#     print(tel)
# =============================================================================















