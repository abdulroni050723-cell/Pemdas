# input
nama_barang = input("Nama barang: ")
harga_satuan = int(input("Harga satuan: "))
jumlah_beli = int(input("jumlah_beli: "))
persen = float(input("Diskon (%): "))

# proses
total = harga_satuan * jumlah_beli
diskon = total * persen / 100
bayar = total - diskon

# output
print(f"{nama_barang} x{jumlah_beli}")
print(f"total : Rp{total:,.0f}")
print(f"diskon : Rp{diskon:,.0f}")
print(f"bayar : Rp{bayar:,.0f}")
