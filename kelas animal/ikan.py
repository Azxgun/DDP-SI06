from animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah warna {self.warna_ikan} dan hewan ini adalah {self.jenis_ikan}')

mas = ikan('ikan mas', 'plankton', 'air', 'bertelur', 'emas', 'sungai')
mas.cetak_ikan()