input_angka = int(input("masukkan batas angka : "))

angka1 = 0
angka2 = 1
fib_arr = []
angka_terakhir = angka1 + angka2

while angka1 < input_angka:
    fib_arr.append(angka1)
    angka_terakhir = angka1 + angka2
    angka1 = angka2
    angka2 = angka_terakhir
    
print(fib_arr)