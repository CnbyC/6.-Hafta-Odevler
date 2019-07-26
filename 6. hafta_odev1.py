print("SAYI TAHMIN OYUNU")                                          # imza sablonumuzun ilk satirini yazdik
print("-" * 5, "ZAFER", "-" * 5, end="\n\n")                        # imza sablonumuzun ikinci satirini yazdik

print("""
Sayi tahmin oyunumuza hos geldiniz. 
Lutfen aklinizda 1 - 100 arasi bir sayi tutunuz.
Programimiz aklinizda tuttugunuz sayiyi bulmaya calisacaktir.

Programimizin yaptigi tahmin aklinizdaki sayidan buyukse    -
Programimizin yaptigi tahmin aklinizdaki sayidan kucukse    + 
Programimizin yaptigi tahmin aklinizdaki sayi ise           E 

tusuna basiniz.
""")

baslama=input("Hazirsaniz B tusuna basin ve heyecan baslasin. Oyundan cikmak istiyorsaniz Q tusuna basin, severek ayrilalim : ")

if baslama == "Q":
    print("Oyundan cikmayi istediniz. Size yasaminizda mutluluklar :(")
    quit()

if baslama == "B":
    altsinir=0
    ustsinir=101
    import random
    tahmin=random.randint(altsinir, ustsinir)
    print("1. tahmin : ", tahmin)
    deneme=1
    while True:
        deneme+=1
        degerlendirme=input("Bu tahmine yonelik degerlendirmeniz (-, +, E) nedir : ")
        if degerlendirme == "-":
            ustsinir=tahmin
            tahmin=int((ustsinir+altsinir)/2)
            print(deneme,".", "tahmin :", tahmin)
        elif degerlendirme == "+":
            altsinir=tahmin
            tahmin=int((ustsinir+altsinir)/2)
            print(deneme,".", "tahmin :", tahmin)
        elif degerlendirme == "E":
            print("Tebrikler. Aklimdaki sayiyi {}. denemede bildiniz.".format(deneme))
            break