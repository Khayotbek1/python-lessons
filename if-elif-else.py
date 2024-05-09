# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:24:49 2024

@author: Khayotbek
"""

# =============================================================================
# yosh = int(input("Yoshingiz nechida? \n>>>"))
# 
# if yosh < 4:
#     narh = 0
# 
# elif yosh <= 12:
#     narh = 5000
# 
# elif yosh <= 18:
#     narh = 8000
# 
# else:
#     narh = 10000
# 
# print(f"Sizga kirish narhi {narh} so'm")
# =============================================================================


# or operatori =============================================================================
# kun = input("Bugun kun nima?\n>>>")
# 
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanbaga':
#     print('Bugun dam olish kuni.')
# 
# else:
#     print('Bugun ish kuni)')
# =============================================================================

# and operatori =============================================================================
# kun = input("Bugun kun nima?\n>>>")
# harorat = int(input("harorat qanday?\n>>>"))
# 
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Cho'milgani ketdik")
#     
# else:
#     print("Uyda dam olamiz")
# =============================================================================

# or and operatorlari =============================================================================
# kun = input("Bugun kun nima?\n>>>")
# harorat = int(input("harorat qanday?\n>>>"))
# 
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
#     print("cho'milgani ketdik")
# 
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
#     print("Uyda dam olamiz")
#     
#     
# else:
#     print("Ishla undan ko'ra")
# =============================================================================
    
#Boolean =============================================================================
# jami = 0
# 
# osh = True
# 
# choy = True
# 
# salat = False
# 
# if osh: 
#     jami = jami + 15000 #jami narhga 15000 qo'shamiz
#     
# if choy and salat: #Agar mijoz choy ham salat olgan bo'lsa
#     jami = jami + 10000 #jamiga 10000 qo'shamiz
#     
# elif choy or salat: #Agar choy yoki salat olgan bo'lsa  5000 qo'shamiz
#     jami = jami + 5000
#     
# print(f"Jami {jami} so'm")
# =============================================================================
    
# xar biriga solishtirib chiqish =============================================================================
# jami = 0    
# osh = True 
# choy = True
# salat = False
# assorti = True
# 
# if osh:
#     print("Mijoz osh sotib oldi narhi: 15000")
#     jami = jami + 15000
# 
# if choy:
#     print("Mijoz choy sotib oldi  narhi: 5000")
#     jami = jami + 5000
#     
# if salat:
#     print("Mijoz salat sotib oldi  narhi: 5000")
#     jami = jami + 5000
#     
# if assorti:
#     print("Mijoz assorti sotib oldi  narhi: 20000")
#     jami = jami + 20000
#     
# print(f"Jami {jami} so'm")
# =============================================================================

# in va not in operatori ro'yxat ichidan qidirishga yordam beradi =============================================================================
# menu = ['osh', 'manti', 'shashlik', 'norin']
# 
# ovqat = input("Nima ovqat yeysiz?\n>>> MENU: osh, manti, shashlik, norin \n>>>")
# 
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
#     
# else:
#     print("Afsuski bizda bunday ovqat yo'q")
# =============================================================================

# Ro'yxatlar bilan ishlash algoritm mi =============================================================================
# menu = ['osh', 'manti', 'shashlik', 'norin']
# buyurtmalar = ['osh', 'shashlik', 'lovya', 'norin']
# 
# if buyurtmalar: #Agar ro'yxatda biror element bo'lsa bu True qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menu da bu {taom} bor")
#         else:
#             print(f"Menu da bu {taom} yo'q")
# else: #Agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh")
# =============================================================================


#Amaliyot

# =============================================================================
# son = float(input("Juft son kiriting\n>>> "))
# 
# if son % 2:
#     print("Bu son juft emas")
#     
# else:
#     print("Rahmat")
# =============================================================================

# =============================================================================
# yosh = int(input("Yoshingiz nechida\n>>> "))
# 
# if yosh <= 4 or yosh >= 60:
#     print("Bepul")
#     
# elif yosh < 18:
#     print("10000")
# 
# elif yosh > 18:
#     print("20000")
# =============================================================================

# =============================================================================
# print("ikkita son kiriting")
# son1 = float(input("1- sonni kiriting\n>>> "))
# son2 = float(input("2- sonni kiriting\n>>> "))
# 
# if son1 == son2:
#     print(f"{son1} = {son2}")
# 
# elif son1 > son2:
#     print(f"{son1} > {son2}")
#     
# else:
#     print(f"{son1} < {son2}")
# =============================================================================


# =============================================================================
# mahsulotlar = ['anor', 'behi', 'tarvuz', 'qovun', 'olma', 'nok', 'piyoz', 'anjir', 'uzum']
# 
# savat = []
# 
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower())
#     
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#         
#     else:
#         print(f"Do'konimizda  {mahsulot} yo'q")
# =============================================================================


mahsulotlar = ['anor', 'behi', 'tarvuz', 'qovun', 'olma', 'nok', 'piyoz', 'anjir', 'uzum']

savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower())
    
bor_mahsulotlar = []
mavjud_emas = []
    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
        
    else:
        mavjud_emas.append(mahsulot)
        
if mavjud_emas:
    print("Bizda quyidagi mahsulotlar mavjud emas")
    for mahsulot in mavjud_emas:
            print(mahsulot)
    
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")     




