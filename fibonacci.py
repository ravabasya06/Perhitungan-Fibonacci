def ulang():
    
    input_angka = int(input("masukkan batas angka : "))
    
    angka1 = 0
    angka2 = 1
    fib_arr = []
    
    while angka1 <= input_angka:
        fib_arr.append(angka1)
        angka_terakhir = angka1 + angka2
        angka1 = angka2
        angka2 = angka_terakhir
        
    print(fib_arr)
    pengulangan = input("Lakukan perhitungan lagi? ya / tidak : ")
    if pengulangan == "ya":
        ulang()
    elif pengulangan == "tidak":
        print("ok")
    else:
        print("Saya tidak mengerti perintah tersebut, saya akan mengira anda menjawab tidak.")
ulang()
