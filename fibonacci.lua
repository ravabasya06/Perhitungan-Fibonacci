function ulang()
  
  angka1 = 0
  angka2 = 1
  
  fib_table = {}
  
  io.write("Masukkan batas angka : ")
  input_angka = tonumber(io.read())
  
  while angka1 <= input_angka do
      table.insert (fib_table, angka1)
      angka_terakhir = angka1 + angka2
      angka1 = angka2
      angka2 = angka_terakhir
  end
  
  for i=1, #fib_table, 1 do
    print(fib_table[i])
  end
  io.write("Lakukan perhitungan lagi? ya / tidak : ")
  pengulangan = io.read()
  
  if pengulangan == "ya" then
    ulang()
  elseif pengulangan == "tidak" then
    print("ok")
  else
    print("Saya tidak mengerti perintah tersebut, saya akan mengira anda menjawab tidak.")
  end
end
ulang()
