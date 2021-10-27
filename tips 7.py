# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 01:09:04 2021

@author: galih-hermawan
"""

barang1 = ['buku', 'pensil', 'penggaris']
barang2 = ['penghapus', 'kertas', 'buku']

barangSama = [b for b in barang1 for b2 in barang2 if b==b2]
print(barangSama)

