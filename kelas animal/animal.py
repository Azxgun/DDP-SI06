class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak (self):
        print(f'Binatang ini adalah : { self.nama}')
        print(f'Makananya yaitu  : { self.makanan}')
        print(f'hidup di temoat : { self.hidup}')
        print(f'Berkembang biak di  : { self.berkembang_biak}')

buaya = Animal("buaya", "daging", "amphibi", "bertelur" )
buaya.cetak()