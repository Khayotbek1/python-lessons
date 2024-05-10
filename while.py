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


son = 0
while son < 10:
    son += 1
    if son%2 != 0:
        continue
    else:
        print(son)

