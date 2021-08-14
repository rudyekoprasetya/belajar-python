# Membuat Class
class kendaraan:

	#method utama dalam class
	def __init__(self, jenis, roda, warna):
		#membuat properti class
		self.jenis = jenis
		self.roda = roda
		self.warna = warna

	#method untuk class kendaraan
	def maju(self):
		print('kendaraan jenis', self.jenis , 'Bergerak maju')

	def mundur(self):
		print('kendaraan jenis', self.jenis , 'Bergerak mundur')

	def belok(self, arah):
		print('kendaraan jenis', self.jenis , 'Belok ke arah ',arah)

	def berhenti(self):
		print('kendaraan jenis', self.jenis , 'berhenti')

	def tampil(self):
		print('kendaraan jenis', self.jenis , 'Beroda', self.roda , 'dan memiliki warna', self.warna)


# membuat instance object
sedan = kendaraan('sedan',4,'hitam')
motor = kendaraan('sepeda motor',2,'putih')

# memanggil fungsi dari instance object
sedan.tampil()
sedan.belok('kiri')
motor.tampil()
motor.maju()
motor.berhenti()

