from animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_ular, warna_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_ular = jenis_ular
        self.warna_ular = warna_ular

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini adalah warna {self.warna_ular} dan hewan ini adalah {self.jenis_ular}')

ular = ular('ular konda', 'Hewan', 'amfibi', 'bertelur', 'hitam and coklat', 'rawa-rawa')
ular.cetak_ular()