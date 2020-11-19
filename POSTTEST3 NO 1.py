stok_v1, stok_v2 = 45, 40
harga_v1, harga_v2 = 2000, 2500

print("===========================")
print("Takoyaki Murah dan Lezat")
print("===========================")
print("Silahkan memilih varian :")

def menu() :
	print("1. Varian 1, Harga = Rp. 2000/pcs (Beli 10 atau lebih dapat potongan 10%!)")
	print("2. Varian 2, Harga = Rp. 2500/pcs (Beli 8 atau lebih dapat potongan 8%!)")
	print("===========================")

menu() 
varian = int(input("Masukkan Varian [1-2] : "))

if varian == 1:
   
    beli = int(input("Stok ada 45 pcs, anda ingin membeli : "))
    if  beli < 10 :
        bayar = beli * harga_v1

        print("Anda membeli :", beli, "pcs")
        print("Anda harus membayar : Rp. " , bayar)
        print("Stok tersisa", stok_v1 - beli)
    
    elif beli <= 45 :
        print('Selamat Anda mendapatkan diskon 10%')

        harga = beli * harga_v1
        diskon = beli * harga_v1 * 10/100
        bayar = beli * harga_v1 - diskon

        print("Anda membeli", beli, "pcs")
        print("Anda harus membayar : Rp. " , harga)
        print("Anda mendapat diskon : Rp. ", diskon)
        print("Anda cukup membayar : Rp. ", bayar)
        print("Stok tersisa", stok_v1 - beli)
    
    elif beli > 45 :
        print("Mohon maaf stok tidak mencukupi")


elif varian == 2 :
    
    beli = int(input("Stok ada 40 pcs, anda ingin membeli : "))
    if  beli < 8 :
        bayar = beli * harga_v2

        print("Anda membeli :", beli, "pcs")
        print("Anda harus membayar : Rp. " , bayar)
        print("Stok tersisa", stok_v2 - beli)
    
    elif beli <= 40 :
        print('Selamat Anda mendapatkan diskon 8%')

        harga = beli * harga_v2
        diskon = beli * harga_v2 * 8/100
        bayar = beli * harga_v2 - diskon

        print("Anda membeli", beli, "pcs")
        print("Anda harus membayar : Rp. " , harga)
        print("Anda mendapat diskon : Rp. ", diskon)
        print("Anda cukup membayar : Rp. ", bayar)
        print("Stok tersisa", stok_v2 - beli)
    
    elif beli > 40 :
        print("Mohon maaf stok tidak mencukupi")
else :
    print("Pilihan tidak tersedia")

print("Terima kasih sudah membeli")
