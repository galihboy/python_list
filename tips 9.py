# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 01:30:35 2021

@author: galih-hermawan
"""

angkaAcak = [2,3,4,6,4,5,2,7,9,7,2]

dataUrutAsc = sorted(angkaAcak)
dataUrutDesc = sorted(angkaAcak,reverse=True)
print(dataUrutAsc)
print(dataUrutDesc)
print(angkaAcak)

angkaAcak.sort()
print(angkaAcak)

angkaAcakDua = [2,3,4,6,4,5,2,7,9,7,2]
dataUrutUnik = list(set(angkaAcakDua))
print(dataUrutUnik)