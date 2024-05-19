# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:22:08 2024

@author: Khayotbek
"""


#NESTING
# =============================================================================
# car0 = {
#         'model': 'nexia',
#         'color': 'black',
#         'year' : 2016,
#         'price': 9000
#         }
# 
# car1 = {
#         'model': 'gentra',
#         'color': 'white',
#         'year' : 2020,
#         'price': 13000
#         }
# 
# car2 = {
#         'model': 'onix',
#         'color': 'grey',
#         'year' : 2023,
#         'price': 14000
#         }
# 
# cars = [car0, car1, car2]
# 
# 
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['color']}, "
#           f"{car['year']}, "
#           f"{car['price']}$"
#           )
# 
# =============================================================================



#
# =============================================================================
# malibus = []
# 
# for n in range(10):
#     new_car = {
#         'model': 'malibu',
#         'color' : 'black',
#         'year': 2024,
#         'price' : None,
#         'km': 0,
#         'karobka': 'avto'
#         }
# 
#     malibus.append(new_car)
#     
# for malibu in malibus:
#     if malibu['karobka'] != 'avto':
#         malibu['price'] = 16000
#     
#     else:
#         malibu['price'] = 18000
# 
# 
# for malibu in malibus[:3]:
#     malibu['color'] = 'white'
#     malibu['karobka'] = 'mexanika'
#     
# for malibu in malibus[3:6]:
#     malibu['color'] = 'grey'
#     malibu['karobka'] = 'mexanika'
#     
# for malibu in malibus[6:]:
#     malibu['color'] = 'blue'
#     
# for malibu in malibus:
#     if malibu['karobka'] != 'avto':
#         malibu['price'] = 16000
#     
#     else:
#         malibu['price'] = 18000
#     
#  
# for malibu in malibus:
#     print(malibu)
# =============================================================================


dasturchilar = {
    'ali' : ['python', 'c++'],
    'vali' : ['html', 'css', 'js'],
    'hasan' : ['php', 'sql'],
    'husan' : ['pyhton', 'php'],
    'maryam' : ['c#', 'c']
    }  


for ism, tillar in dasturchilar.items():
    print(f"\n {ism.title()}, quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(til.upper())
        
#bir qatorga chiqarish
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()}, quyidagi dasturlash tillarini biladi: ")
    for til in tillar:
        print(f'{til.upper()} ', end='')



























