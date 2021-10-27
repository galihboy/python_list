# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 01:50:37 2021

@author: galih-hermawan
"""

angkaAcak = [2,3,4,6,4,5,2,7,9,7,2]

# strAngka = " ".join(angkaAcak) # error
# print(angkaAcak)
print(*angkaAcak)

print(*set(angkaAcak))

buah = ['jeruk', 'mangga', 'nanas', 'apel', 'manggis']

b_satu, *b_sisa = buah
print(b_satu)
print(b_sisa)

b_satu, *b_tengah, b_akhir = buah
print(b_satu)
print(b_tengah)
print(b_akhir)

