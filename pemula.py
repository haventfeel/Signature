print('Keterangann :')
bensin      = int(input('Masukkan Harga Bensin:'))
solar       = int(input('Masukkan Harga Solar:'))
pertamax    = int(input('Masukkan Harga Pertamax:'))

liter       = int(input('Masukkan Liter:'))

print('Harga Bensin: Rp.', bensin)
print('Harga Solar: Rp.', solar)
print('Harga Pertamax: Rp.', pertamax)

nm_variabel = int(input("Masukkan Pilihan :"))

match nm_variabel:
    case minyak if nm_variabel == 1: harga = bensin
    case minyak if nm_variabel == 2: harga = solar
    case minyak if nm_variabel == 3: harga = pertamax
    case _:print('Tidak ada harga')

if harga != 0 :
    jumlah = liter
    for i in range (jumlah) :
        jumlah += harga

        print("Total Pembayaran : Rp.", jumlah)
    
