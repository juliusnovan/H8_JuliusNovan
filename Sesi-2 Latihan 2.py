# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:35:02 2022

@author: 082793
"""

"""
nilai_akhir > 80 <100		--> A
nilai_akhir > 70 <79		--> B
nilai_akhir > 60 <69		--> C
nilai_akhir > 50 <59		--> D
	    0 < 49		--> E

nilai_absen * 10%
nilai_tugas * 20%
nilai_uts * 30%
nilai_uas * 40%

nilai_total = akumulasi semua nilai
"""

nilai_absen = int(input("masukkan nilai absen :"))
nilai_tugas = int(input("masukkan nilai tugas :"))
nilai_uts = int(input("masukkan nilai uts :"))
nilai_uas = int(input("masukkan nilai uas :"))

nilai_total = (nilai_absen*0.1) + (nilai_tugas*0.2) + (nilai_uts*0.3) + (nilai_uas*0.4)

print("nilai total :",nilai_total)

if nilai_total >=80 <=100:
    print("nilai akhir : A")
elif nilai_total >=70 <=79:
    print("nilai akhir : B")
elif nilai_total >=60 <=69:
    print("nilai akhir : C")
elif nilai_total >=50 <=59:
    print("nilai akhir : D")
else:
    print("nilai akhir : E")
    