# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:58:32 2021

@author: galih-hermawan
"""

angkaAcak = [2,3,4,6,4,5,2,7,9,7,2]
angkaCari = 2
print(angkaAcak.index(angkaCari))
#print(angkaAcak.index(10)) # ValueError: 10 is not in list
print(angkaAcak.index(angkaCari,1))
print(angkaAcak.index(angkaCari,7))

# pencarian via looping
for idx,angka in enumerate(angkaAcak):
    if angka == angkaCari:
        print(idx)

# looping versi pendek - list comprehension
lstCari = [idx for idx,angka in enumerate(angkaAcak) if angka == angkaCari]
print(lstCari)

lstCari = [[idx,angka] for idx,angka in enumerate(angkaAcak) if angka % 2 == 1]
print(lstCari)

