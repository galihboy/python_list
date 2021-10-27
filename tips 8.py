# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 01:24:06 2021

@author: galih-hermawan
"""

barang1 = ['buku', 'pensil', 'penggaris']
barang2 = ['penghapus', 'kertas', 'buku']

set_barang1 = set(barang1)
set_barang2 = set(barang2)

listBarang = list(set_barang1.symmetric_difference(set_barang2))
print(listBarang)