class Gempa:
    #konstruktor inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    # method penentu skala gempa
    def dampak(self):
        #logika/statment
        if self.skala < 2:
            print("gempa tidak berasa")
        elif 2 <= self.skala <= 4 :
            print("dampak gempa bangunan retak retak")
        elif 4 <= self.skala <= 6 :
            print("dampak gempa bangunan roboh")
        elif self.skala > 6 :
            print("dampak gempa banunan roboh dan berpotensi tsunami") 
        
        # menmpilkan hasil dari lokasi dan skala gempa
        print(f"lokasi gempa: {self.lokasi}")
        print(f"skala gempa: {self.skala}")