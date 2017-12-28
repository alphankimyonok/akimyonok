from random import randint
UST = input("Üst limit giriniz: "
RNDNB = randint(0, int(UST))
YANLIS = True
SAYAC = 0
TAHMIN = 1
while YANLIS:
    TAHMIN = int(input("Tahmininizi Giriniz: "))
    if TAHMIN==RNDNB :
        YANLIS = False
    elif TAHMIN > RNDNB :
        print ("Tahminiz sayıdan büyük!")
    elif TAHMIN < RNDNB :
        print ("Tahminiz sayıdan küçük!")
    SAYAC = SAYAC + 1

print(str(SAYAC) + " tahminde bildiniz!")
