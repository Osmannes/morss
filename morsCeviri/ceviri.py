from morsHarfleri import harfler

while True:
    def morsAlfabe(cevir):
        sifre = ""
        for x in cevir:
            sifre += harfler[x.lower()] + " "
        return sifre
    cevir = input("Kelime: ")
    print(morsAlfabe(cevir))




