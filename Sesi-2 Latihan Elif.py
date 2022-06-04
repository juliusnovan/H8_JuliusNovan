# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:09:21 2022

@author: 082793
"""



harga = int(input("harga buku :"))
j_beli = int(input("jumlah beli :"))
uang = int(input("jumlah uang :"))

t_beli = harga * j_beli

print("total beli :",t_beli)

if uang < t_beli:
    print("uang tidak cukup")
elif uang == t_beli:
    print("dapat",j_beli,"buku")
else:
    print("dapat",j_beli,"buku"),print("uang kembali :",uang-t_beli)

