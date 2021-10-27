# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:38:15 2021

@author: galih-hermawan
"""

angkaAcak = [2,3,4,6,4,5,2,7,9,7,2]
angkaCari = 2

jml = angkaAcak.count(angkaCari)
print(f"Angka {angkaCari} ditemukan sejumlah {jml} kali")

angkaGanjil = [angka for angka in angkaAcak if angka % 2 == 1]
print(angkaGanjil)
print(f"Jumlah: {len(angkaGanjil)}")
