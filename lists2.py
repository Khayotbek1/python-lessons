# -*- coding: utf-8 -*-
"""
Created on Tue May  7 116:47:24 2024

@author: user
"""


cars = ['bmw', 'mercedes benz', 'volvo', 'tesla', 'audi']

#cars.sort()
#cars.reverse()
#print(cars)

#print(sorted(cars, reverse=True))


sonlar = [1, 5, 2, 7, 9, 6]

sonlar.sort()
#print(sonlar)


#len(sonlar)

sonlar = list(range(0,10))

sanash = list(range(0,11,2))
max_qiymat = max(sanash)
#print(max_qiymat)


narhlar = [10500, 50000, 12_250_000, 150000, 35_25_350_000]

qimmat = max(narhlar)
arzon = min(narhlar)
jami = sum(narhlar)

#print("Eng arzon narh ", arzon, "Eng qimmat narh ", qimmat, "Jami ", jami)


#print(cars[0:3])

my_cars = cars
my_cars.remove('volvo')
my_cars[0] = 'Lacetti'
cars.append('bmw')
#print(my_cars)
#print(cars)
#bu yerda cars ham my_cars ham bir xil qiymat olyapdi my_cars carsdan copy olgani yo'q copy olish u.n biz buning uchun: [:] belgidan foyd. kerak : esa barchasi belgilaydi
    
your_cars = cars[:]

your_cars.remove('bmw')
your_cars.append('nexia')
#print(your_cars)
#print(cars)

#tuple

toys = ('bear', 'bus', 'car', 'snake', 'teddy')

#toys.append('bee')
#print(toys) #toys type tuple turiga kiradi uni  o'zgartirib bolmaydi

#uni mana bunday ozgartirsa boladi

toys = list(toys) #bunda toys type list o'zgaradi

toys.append('shark')
print(toys)

toys = tuple(toys)









































