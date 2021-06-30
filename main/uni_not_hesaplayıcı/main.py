print("""
Vize 1 ve Final notlarınızı "10,20,30" gibi girin ve size ortalamanızı söylesin.

Dikkat: Doğru sonuç elde etmek için "ilk notlar:" ve "ikinci notlar:" inputlarına
aynı sayıda argüman girmelisiniz ve sonuncu argümandan sonra virgül koymamalısınız.

Örnek:
ilk notlar:10,20,30
ikinci notlar:40,50,60
100 üzerinden: 38.0
4 üzerinden: 1.52
------------------------
""")

while True:
    bir = input("ilk notlar:").split(",")
    iki = input("ikinci notlar:").split(",")
    result = []
    for i in bir:
        for j in iki:
            if bir.index(i) == iki.index(j):
                result.append( ((int(i)*4)/10) +((int(j)*6)/10) )
    result_number = 0
    for i in result:
        result_number += i
    print("100 üzerinden:", result_number/len(result))
    print("4 üzerinden:", (4*result_number/len(result))/100)
    print("-"*40)