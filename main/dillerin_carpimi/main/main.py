def carpim (p1, p2):
    p3 = list()
    for i in p1:
        for j in p2:
            p3.append(i+j)
    return p3

def karsilastirma (p1,p2):
    for i in p1:
        if i in p2:
            continue
        else:
            return "\nBu listeler aynı değil!"
    return "\nBu listeler birbiriyle aynı!"


while True:
    print("1) İki Dil'i Birbiriyle Çarp\n2) Dil Listelerini Karşılaştır")
    
    try:
        secim = int(input("\nSane ne lazım? 1'mi 2'mi: "))
    except ValueError:
        print("\n--------------------------------")
        print("Lütfen geçerli bir sayi giriniz1.")
        print("--------------------------------\n")
        continue

    if secim != 1 and secim !=2:
        print("\n--------------------------------")
        print("Lütfen geçerli bir sayi giriniz2.")
        print("--------------------------------\n")
        continue

    if secim == 1:
        print("\n----------------------------------------------------------------------------------\n\n-----------------------------------------")
        print("Çıkmak için herhangi bir listeye xxx yazın.")
        print("-----------------------------------------\n")
        while True:
            liste1 = input("Liste1'i girin: ").split(",")
            if "xxx" in liste1:
                print("\n----------------------------------------------------------------------------------\n")
                break
            liste2 = input("Liste2'i girin: ").split(",")
            if "xxx" in liste2:
                print("\n----------------------------------------------------------------------------------\n")
                break
            carpma = carpim(liste1, liste2)
            print("Sonuç: ", carpma, "\n")
            print("-----------------------------------------")

    if secim == 2:
        print("\n----------------------------------------------------------------------------------\n\n-----------------------------------------")
        print("Çıkmak için herhangi bir listeye xxx yazın.")
        print("-----------------------------------------\n")
        while True:
            liste1 = input("Liste1'i girin: ").split(",")
            if "xxx" in liste1:
                print("\n----------------------------------------------------------------------------------\n")
                break
            liste2 = input("Liste2'i girin: ").split(",")
            if "xxx" in liste2:
                print("\n----------------------------------------------------------------------------------\n")
                break
            aynimi = karsilastirma(liste1,liste2)
            print(aynimi, "\n")
            print("-----------------------------------------")

    