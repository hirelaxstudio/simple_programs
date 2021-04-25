from math import fabs
from os import system
t_degerler_sin = {0: 0, 
                  30: 1/2,
                  45: (2**(1/2))/2, 
                  60: (3**(1/2))/2, 
                  90: 1, 
                  120: (3**(1/2))/2, 
                  135: (2**(1/2))/2, 
                  150: 1/2, 
                  180: 0
}
t_degerler_cos = {0: 1,
                  30: (3**(1/2))/2,
                  45: (2**(1/2))/2,
                  60: 1/2,
                  90: 0,
                  120: -(1/2),
                  135: -((2**(1/2))/2),
                  150: -((3**(1/2))/2),
                  180: -1
}

# Coulomb Yasası (Fe = ke/(q1*q2/r^2))
def cou ():
    ke = input("ke: ")
    if ke == "xxx":
        return "xxx"
    q1 = input("q1: ")
    if q1 == "xxx":
        return "xxx"
    q1_ten = input("q1 x 10^?: ")
    if q1_ten == "xxx":
        return "xxx"
    q2 = input("q2: ")
    if q2 == "xxx":
        return "xxx"
    q2_ten = input("q2 x 10^?: ")
    if q2_ten == "xxx":
        return "xxx"
    r = input("r: ")
    if r == "xxx":
        return "xxx"
    try:
        ke = float(ke)
    except ValueError:
        ke = float(9)
    try:
        q1 = float(q1)
        q1_ten = float(q1_ten)
        q2 = float(q2)
        q2_ten = float(q2_ten)
        r = float(r)            
    except ValueError:
        return False
    ke = ke*(10**9)
    a1 = q1*(10**q1_ten)
    a1 = fabs(a1)
    a2 = q2*(10**q2_ten)
    a2 = fabs(a2)
    return ke*((a1*a2)/r**2)
    

# Evrensel kütle çekim yasası (Fg = g*(m1*m2/r^2))
def ecy ():
    g = input("g: ")
    if g == "xxx":
        return "xxx"
    m1 = input("m1: ")
    if m1 == "xxx":
        return "xxx"
    m1_ten = input("m1 x 10^?: ")
    if m1_ten == "xxx":
        return "xxx"
    m2 = input("m2: ")
    if m2 == "xxx":
        return "xxx"
    m2_ten = input("m2 x 10^?: ")
    if m2_ten == "xxx":
        return "xxx"
    r = input("r: ")
    if r == "xxx":
        return "xxx"
    try:
        g = float(g)
    except ValueError:
        g = float(9)
    try:
        m1 = float(m1)
        m1_ten = float(m1_ten)
        m2 = float(m2)
        m2_ten = float(m2_ten)
        r = float(r)
    except ValueError:
        return False

    g = g*(10**-11)
    a1 = m1*(10**m1_ten)
    a2 = m2*(10**m2_ten)
    return g*((a1*a2)/r**2)

# Fxy'nin eksenlere göre değerini bulmak
def fxy (kuvvet, derece):
    global t_degerler_cos
    global t_degerler_sin
    kuvvet = input("Fxy: ")
    if kuvvet == "xxx":
        return "xxx"
    derece = input("Fxy'nin X ekseni ile arasındaki açı: ")
    if derece == "xxx":
        return "xxx"
    try:
        kuvvet = float(kuvvet)
        derece = int(derece)
    except ValueError:
        return False

    fxy_x = kuvvet*t_degerler_cos[derece]
    fxy_y = kuvvet*t_degerler_sin[derece]
    return fxy_x, "\n", "fxy_y = ", fxy_y

# Bileşke kuvvet (R^2 = A^2 + B^2 - 2AB*cos(180-(kuvvetler aradaki açı)))
def bv (k1, k2, derece):
    global t_degerler_cos
    global t_degerler_sin
    k1 = input("k1: ")
    if k1 == "xxx":
        return "xxx"
    k2 = input("k2: ")
    if k2 == "xxx":
        return "xxx"
    derece = input("cos(180 - ?): ")
    if derece == "xxx":
        return "xxx"
    try:
        k1 = float(k1)
        k2 = float(k2)
        derece = int(derece)
    except ValueError:
        return False
    
    R = (k1**2) + (k2**2) - (2*k1*k2*t_degerler_cos[180-derece])
    return R

# Elektrik alan (ke*(q/r^2))
def ea ():
    ke = input("ke: ")
    if ke == "xxx":
        return "xxx"
    q1 = input("q1: ")
    if q1 == "xxx":
        return "xxx"
    q1_ten = input("q1 x 10^?: ")
    if q1_ten == "xxx":
        return "xxx"
    r = input("r: ")
    if r == "xxx":
        return "xxx"
    try:
        ke = float(ke)
    except ValueError:
        ke = float(9)
    try:
        q1 = float(q1)
        q1_ten = float(q1_ten)
        r = float(r)
    except ValueError:
        return False

    ke = ke*(10**9)
    a1 = q1*(10**q1_ten)
    a1 = fabs(a1)
    return ke*(a1/(r**2))

#######################################################################################

while True:
    print("1) Coulomb Yasası\n2) Evrensel kütle çekim yasası\n3) Fxy'nin eksenlere göre değerini bulmak\n4) Bileşke kuvvet\n5) Elektrik alan")
    
    try:
        secim = int(input("\nSane ne lazım: "))
    except ValueError:
        system("cls")
        print("--------------------------------")
        print("Lütfen geçerli bir sayi giriniz!")
        print("--------------------------------\n")
        continue

    if secim != 1 and secim !=2 and secim !=3 and secim !=4 and secim !=5:
        system("cls")
        print("--------------------------------")
        print("Lütfen geçerli bir sayi giriniz!")
        print("--------------------------------\n")
        continue

    if secim == 1:
        system("cls")
        print("\n-----------------------------------------")
        print("Çıkmak için herhangi bir seçeneğe xxx yazın.")
        print("-----------------------------------------\n")
        print("Coulomb Yasası: Fe = ke x (|q1| x |q2| / r^2)\nNot: ke boş bırakılırsa (9 x 10^9) kabul edilir.\nNot: Kesirli sayıları yazarken virgül değil, nokta kullanın.\n")
        while True:
            gecici = cou()
            if gecici == "xxx":
                system("cls")
                break
            elif gecici == False:
                print("\n-------------------------------------\nEksik veya yanlış bir değer girdiniz.\n-------------------------------------\n")
                continue
            print("Fe = ", gecici)
            print("-----------------------------------------")
    
    elif secim == 2:
        system("cls")
        print("\n-----------------------------------------")
        print("Çıkmak için herhangi bir seçeneğe xxx yazın.")
        print("-----------------------------------------\n")
        print("Evrensel kütle çekim yasası: Fg = g x (m1 x m2 / r^2)\nNot: g boş bırakılırsa (9 x 10^-11) kabul edilir.\nNot: Kesirli sayıları yazarken virgül değil, nokta kullanın.\n")
        while True:
            gecici = ecy()
            if gecici == "xxx":
                system("cls")
                break
            elif gecici == False:
                print("\n-------------------------------------\nEksik veya yanlış bir değer girdiniz.\n-------------------------------------\n")
                continue
            print("Fg = ", gecici)
            print("-----------------------------------------")

    elif secim == 3:
        system("cls")
        print("\n-----------------------------------------")
        print("Çıkmak için herhangi bir seçeneğe xxx yazın.")
        print("-----------------------------------------\n")
        print(f"Fxy'nin eksenlere göre değerini bulmak: Fxy_x = fxy x cos(a)\n{' '*40}Fxy_y = fxy x sin(a)\nNot: Kesirli sayıları yazarken virgül değil, nokta kullanın.\n")
        while True:
            gecici = fxy()
            if gecici == "xxx":
                system("cls")
                break
            elif gecici == False:
                print("\n-------------------------------------\nEksik veya yanlış bir değer girdiniz.\n-------------------------------------\n")
                continue
            print("fxy_x = ", gecici)
            print("-----------------------------------------")

    elif secim == 4:
        system("cls")
        print("\n-----------------------------------------")
        print("Çıkmak için herhangi bir seçeneğe xxx yazın.")
        print("-----------------------------------------\n")
        print("Bileşke kuvvet: R^2 = k1^2 + k2^2 - 2 x k1 x k2 x cos(180-[kuvvetler aradaki açı])\nNot: Kesirli sayıları yazarken virgül değil, nokta kullanın.\n")
        while True:
            gecici = bv()
            if gecici == "xxx":
                system("cls")
                break
            elif gecici == False:
                print("\n-------------------------------------\nEksik veya yanlış bir değer girdiniz.\n-------------------------------------\n")
                continue
            print("Bileşke Kuvvet: ", gecici)
            print("-----------------------------------------")

    elif secim == 5:
        system("cls")
        print("\n-----------------------------------------")
        print("Çıkmak için herhangi bir seçeneğe xxx yazın.")
        print("-----------------------------------------\n")
        print("Elektrik alan: ke x (q / r^2)\nNot: ke boş bırakılırsa (9 x 10^9) kabul edilir.\nNot: Kesirli sayıları yazarken virgül değil, nokta kullanın.\n")
        while True:
            gecici = ea()
            if gecici == "xxx":
                system("cls")
                break
            elif gecici == False:
                print("\n-------------------------------------\nEksik veya yanlış bir değer girdiniz.\n-------------------------------------\n")
                continue
            print("Fe = ", gecici)
            print("-----------------------------------------")