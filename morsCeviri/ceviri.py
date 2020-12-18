from morsHarfleri import harfler

while True:
    def morsAlfabe(cevir):
        kelime = ""
        for x in cevir:
            kelime += harfler[x.lower()] + " "
        return kelime
    cevir = input("Kelime: ")
    print(morsAlfabe(cevir))




