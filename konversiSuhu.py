## Latihan

print(
'''APLIKASI KONVERSI SUHU
======================
Pilih satuan suhu yang anda ingin ubah dari:
1. Celcius
2. Fahrenheit
3. Reamur
4. Kelvin''')

kondisi = True

while kondisi:
    try:
        pilihan = int(input('>> '))
        if(pilihan<1 or pilihan>4):
            kondisi = True
            print('Masukkan angka hanya dari 1-4')
        else:
            kondisi = False
    except ValueError:
        print("Yang anda masukkan bukan angka")

match(pilihan):
    case 1:
        celcius = float(input("Masukkan suhu dalam celcius : "))
        print(f"Suhu adalah {celcius:.2f} Celcius")
        #reamur
        reamur = (4/5)*celcius
        print(f"Suhu dalam reamur adalah {reamur:.2f} Reamur")
        #fahrenheit
        fahrenheit = ((9/5)*celcius)+32
        print(f"Suhu dalam fahrenheit adalah {fahrenheit:.2f} Fahrenheit")
        #kelvin
        kelvin = celcius + 273
        print(f"Suhu dalam kelvin adalah {kelvin:.2f} Kelvin")

    case 2:
        fahrenheit = float(input('Masukkan suhu dalam fahrenheit :'))
        print(f"Suhu adalah {fahrenheit:.2f} Fahrenheit")
        #celcius
        celcius = (fahrenheit-32)*5/9
        print(f'Suhu dalam celcius adalah {celcius:.2f} Celcius')
        #reamur
        reamur = (fahrenheit-32)*4/9
        print(f'Suhu dalam reamur adalah {reamur:.2f} Reamur')
        #kelvin
        kelvin = ((fahrenheit-32)*5/9)+273
        print(f"Suhu dalam kelvin adalah {kelvin:.2f} Kelvin")

    case 3:
        reamur = float(input('Masukkan suhu dalam reamur :'))
        print(f'Suhu adalah {reamur:.2f} Reamur')
        #celcius
        celcius = reamur*5/4
        print(f'Suhu dalam celcius adalah {celcius:.2f} Celcius')
        #fahrenheit
        fahrenheit = (reamur*9/4)+32
        print(f"Suhu dalam fahrenheit adalah {fahrenheit:.2f} Fahrenheit")
        #kelvin
        kelvin = (reamur*5/4)+273
        print(f"Suhu dalam kelvin adalah {kelvin:.2f} Kelvin")

    case 4:
        kelvin = float(input('Masukkan suhu dalam kelvin :'))
        print(f'Suhu adalah {kelvin:.2f} Kelvin')
        #celcius
        celcius = kelvin-273
        print(f'Suhu dalam celcius adalah {celcius:.2f} Celcius')
        #fahrenheit
        fahrenheit = ((kelvin-273)*9/5)+32
        print(f"Suhu dalam fahrenheit adalah {fahrenheit:.2f} Fahrenheit")
        #reamur
        reamur = (kelvin-273)*4/5
        print(f'Suhu dalam reamur adalah {reamur:.2f} Reamur')

    case _:
        print('Terjadi kesalahan, mohon laporkan ke nomor 082246584822')

print('Terima kasih telah menggunakan aplikasi kami :D')
