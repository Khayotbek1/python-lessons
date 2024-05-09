# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:26:36 2024

@author: khayotbek
"""

mevalar = ['olma', 'gilos', 'anor', 2, 5]
mevalar[0] = 'uzum'

mevalar.append('nok')

mevalar.insert(0, 'ananas')
#print(mevalar)

cars = []
cars.append('Lacetti')
cars.append('Nexia')
cars.append('matiz')
cars.append('spark')
#print(cars)

del cars[0]
cars.insert(0, 'spark')

cars.remove('spark')
#print(cars)


#Amaliyot

ismlar = ['Doston', 'Donyor', 'Jalol']

#print("Salom", ismlar[0], "bugun choyxona bormi?")
#print(ismlar[1], "choyxonaga boramizmi?")
#print(ismlar[2], "sen bormaysanmi?")


sonlar = [1, 5, 6, -7, -5]

kvadrat = sonlar[1]**2

sonlar[2] = 2**3

sonlar.insert(4, 100)
sonlar.remove(-5)
sonlar.pop(3)


friends = []

friends.append('Doston')
friends.append('Jalol')
friends.append('Qosim')

friends.remove('Qosim')
#print(friends)

friends.insert(0, 'Rasul')
friends.insert(3, 'Juma')

keladiganlar = friends


mehmonlar = []

mehmonlar.append(keladiganlar.pop(1))
mehmonlar.append(keladiganlar.pop(-1
                                  ))
print(mehmonlar)
























