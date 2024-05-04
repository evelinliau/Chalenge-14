import fisika
import time

def batas():
    print("_"*15)

waktu_awal = time.time()
print(f"Massa Jenis = {fisika.MassaJenis.Massajenis(10,2)}")
print(f"Massa = {fisika.MassaJenis.Massa(10,2)}")
print(f"Volume = {fisika.MassaJenis.Volume(10,2)}")

waktu_akhir = time.time()
#untuk liat wsktu without pycache
print(f"waktu yang dibutuhin = {waktu_akhir - waktu_awal}")

batas()

print(f"Usaha = {fisika.U(10,5)}")
print(f"Gaya = {fisika.G(10,5)}")
print(f"Jarak = {fisika.J(10,5)}")

batas()
print(f"Energi Potensial = {fisika.Ep(2,5,8)}")
