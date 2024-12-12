from animal import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
     super().__init__(nama, makanan, hidup, berkembang_biak)
     self.jenis_bulu = jenis_bulu
     self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu : {self.jenis_bulu}')
        print(f'hewan ini bersuara: {self.bunyi}')

beo = burung('burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'kamu jelek')
beo.cetak_burung()

print()
dara = burung('burung dara', 'biji-bijian', 'udara', 'bertelur', 'white', 'cukurukuk')
dara.cetak_burung()