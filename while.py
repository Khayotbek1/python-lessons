# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:13:40 2024

@author: khayotbek
"""

# input() =============================================================================
# ism = input("Ismingiz nima? ")
# savol = f"Salom {ism.title()}. Yoshingiz nechida? "
# 
# yosh = int(input(savol))
# height = float(input("Bo'yingiz necha metr"))
# =============================================================================

#while =============================================================================
# son = 1
# while son<= 5:
#     print(son, end=' ')
#     son = son + 1
# =============================================================================


#while and input() =============================================================================
# print("Kiritilgan sonni kubini hisoblaydi")
# savol = "Istalgan son kiriting "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing!)\n>>> "
# qiymat = ''
# 
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**3)
# 
# print("Dastur tugadi!")
# =============================================================================



#Ishora
# =============================================================================
# print("Kiritilgan sonni kubini hisoblaydi")
# savol = "Istalgan son kiriting "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing!)\n>>> "
# 
# qiymat = ''
# ishora = True
# 
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**3)
# print("Dastur tugadi!")
# =============================================================================


#break for
# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")
# =============================================================================


# =============================================================================
# son = 0
# while son < 10:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
#         
#         
#         
# =============================================================================
       

#Ro'yxat bilan ishlash  
# =============================================================================
# print("Kerakli harajatlarni ro'yxatini tuzish.")
# mahsulotlar = []
# n = 1
# 
# while True:
#     savol = f"{n}-mahsulot nomini kiriting: "
#     mahsulot = input(savol)
#     mahsulotlar.append(mahsulot)
#     takror = input("Yana mahsulot kiritasizmi? ha/yo'q: ")
#     n += 1
#     if takror != 'ha':
#         break
#     
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())    
# =============================================================================
         

#True and false bilan ishlash
# =============================================================================
# print("Mahsulotlar ro'yxatini kiriting.")
# 
# mahsulotlar = {}
# foo = True
# 
# while foo:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narx = input(f"{mahsulot.title()}ni narxini kiriting: ")
#     mahsulotlar[mahsulot] = int(narx)
#     takror = input("Yana mahsulot qo'shasizmi ha/yo'q: ") 
#     if takror != 'ha':
#         foo = False
#         
# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot.title()}ning narxi: {narx}")
#         
# =============================================================================
        

# =============================================================================
# cars = ['nexia', 'tico', 'lacetti', 'matiz', 'nexia', 'audi', 'malibu', 'nexia']    
# car = 'nexia'     
# while car in cars:
#     cars.remove(car)
# print(cars)     
# =============================================================================
        
talabalar = ['Razzoqov Hayotbek', 'Xoshimova Mavluda', 'Eminova Maftuna', 'Rahimova Xilola', 'Husanov Umid']

baholangan_talabalar = {}

while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba}ning bahosini kriting: ")
    print(f"{talaba} baholandi!\n")
    baholangan_talabalar[talaba] = int(baho)
    
for talaba, baho in baholangan_talabalar.items():
    print(f"{talaba}ning bahosi {baho}")
        
        
        
        
        
        
        

