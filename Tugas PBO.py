print("Menghitung luas persegi")
p = float(input("Masukan panjang :"))
l = float(input("Masukan lebar :"))
persegi = p*l
print("Luas persegi adalah :" + str(persegi))

print("==============================================")

print("Menghitung luas lingkaran")
r = int(input('masukan jari-jari lingkaran:'))
phi = 3.14
L = phi * (r*r)
print('Luas lingkaran dengan jari-jari {} adalah {}'.format(r,L))

print("==================================================")

print("Menghitung luas Segitiga")
a = float(input("Masukan panjang alas: "))
t = float(input("Masukan tinggi segitiga: "))
luas = 0.5*a*t
print("Luas segitiga adalah :"+str(luas))
