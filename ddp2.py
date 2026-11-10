def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

# Contoh penggunaan sesuai permintaan:
print(celcius_ke_fahrenheit(0))   # Output: 32.0
print(celcius_ke_fahrenheit(100)) # Output: 212.0


def is_genap(bilangan):
  return bilangan % 2 == 0


# Pengujian
print(is_genap(4))  # Output: True
print(is_genap(7))  # Output: False


def nilai(skor):
  if skor > 60:
    print("lulus")
  else:
    print("gagal")

# Pengujian
nilai(80)  # Output: lulus
nilai(60)  # Output: gagal

def bilangan(batas):
  ganjil = []
  for i in range(1, batas, 2):
    if i % 2 != 0:
      print(i, end=',')
    
# Pengujian
bilangan(20)  # Output: 1,3,5,7,9,11,13,15,17,19
