# Membuat fungsi
def salam():
	print("Hallo Programmer, Salam Kenal")

# Memanggil fungi
salam()
salam()

# fungsi dengan parameter
# def tambah(a,b):
# 	print("hasil pertambahannya adalah", a+b)

# # memanggil fungsi dengan parameter
# tambah(2,3)
# tambah(4,4)

# fungsi dengan nilai balik
def tambah(a,b):
	return a+b

# memanggil fungsi dengan parameter
hasil=tambah(4,4)

print("Hasil dari fungsi adalah ", hasil)