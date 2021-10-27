# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:12:57 2021

@author: galih-hermawan
"""

listBenda = ["Daun", "Rambut", "Langit"]
listWarna = ["Hijau", "Hitam", "Biru"]

listGabungan = listBenda + listWarna

print(listGabungan)

listGabungan2 = zip(listBenda, listWarna)
for benda, warna in listGabungan2:
    print(benda,warna)

listGabungan3 = list(zip(listBenda, listWarna))
print(listGabungan3)

kamus = dict(zip(listBenda, listWarna))
print(kamus)


listGabungan4 = []
for benda, warna in zip(listBenda, listWarna):
    listGabungan4.extend((benda, warna))
    
print(listGabungan4)