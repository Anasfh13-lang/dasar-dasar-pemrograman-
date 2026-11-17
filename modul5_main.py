print('--------gunakan modul-----------')
import modul2_luas_datar
import modul1_keliling_datar
modul2_luas_datar.luas_lingkaran(10)
modul1_keliling_datar.keliling_persegi(15)
modul2_luas_datar.luas_segitiga(13, 6)

print('\n--gunakan modul dengan alias--')
import modul3_volume_ruang as hitung
import modul4_luas_ruang as ruang
hitung.volume_kubus(3)
ruang.luas_bola(7)

print('\n--gunakan modul dgn memanggil sebagian fungsinya--')
from modul1_keliling_datar import keliling_lingkaran
from modul4_luas_ruang import luas_tabung
keliling_lingkaran(10)
luas_tabung(7, 10)

print('\n--gunakan modul dgn memanggil seluruh fungsinya--')
from modul2_luas_datar import *
from modul1_keliling_datar import *
from modul3_volume_ruang import *
luas_persegi(5)
keliling_segitiga(3, 4, 5)
volume_tabung(7, 10)
volume_bola(7)

print('\n--gunakan modul dgn memanggil sebagian fungsinya dengan alias--')
from modul4_luas_ruang import luas_kubus as lk, luas_bola as lb
lk(3)
lb(5)