# Programı Nasıl Çalıştıracağım?
**main** adındaki klasörünün içinde **dist** adındaki klasörün içinde **main.exe** adlı exe dosyasına ulaşabilirsiniz. Bu dosyaya çift tıklayarak açabilirsiniz. programın çalışma mantığına alışmak için programı çalıştırıp denemeler yapmayı unutmayın.

# Nasıl Çalışır?
Bu programın 2 fonksiyonu vardır. İlk fonksiyonu, 2 dil'i birbiri ile çarpıp sonucu verir. Örneğin:

    Liste1'i girin: a,ab
    Liste2'i girin: a,b
    Sonuç:  ['aa', 'ab', 'aba', 'abb']

İkinci fonksiyonu ise, girdiğiniz iki liste farklımı aynımı size söyler. Örnek:

    Liste1'i girin: aa,bb,cc
    Liste2'i girin: cc,aa,bb
    
    Bu listeler birbiriyle aynı!
    -----------------------------------------
    Liste1'i girin: aa,bb,cc
	Liste2'i girin: cc,xx,aa

	Bu listeler aynı değil!

Dil'leri (Listeleri) girerken, hangi dil'i hangi listeye girdiğinize dikkat ediniz.
## İki Dil'i Birbiriyle Çarp Nasıl Çalışır?
Program sizden 2 input değeri isteyecektir. Bu değerlerden ilki 1. listeye, ikincisi 2. listeye aittir. `L = { a, ab }` gibi bir dil'i, `a,ab` şeklinde yazmalısınız. Her bir dizeyi virgülle ayırmayı unutmayın ve virgülden sonra boşluk bırakmamaya dikkat edin. İki input değerini de girdikten sonra program sizin için iki dil'i çarpacak ve sonucu ekrana bastıracak. Örneğin:

    Liste1'i girin: a,ab
    Liste2'i girin: a,b
    Sonuç:  ['aa', 'ab', 'aba', 'abb']
Burada dikkat edilmesi gereken şey, boş dizeyi ifade eden `Λ` işaretini nasıl tanımlayacağınız. Bu ifade boş dizeyi ifade ettiği için input olarak girmenize gerek yoktur. Yani:

    Liste1'i girin: a,ab,
    Liste2'i girin: b,a
    Sonuç:  ['ab', 'aa', 'abb', 'aba', 'b', 'a']
Liste1 inputunda görüldüğü gibi `a` ve `ab` dizelerini girdikten sonra bir adet virgül daha koyuyoruz ve sonra bir şey yazmıyoruz. Bu işlem, programa, `ab` dizesinden sonra bir `Λ` olduğunu söylemiş oluyor. Bu işareti, dil'in ortasında kullanabilmek için tek yapmanız gereken iki virgül arasını boş bırakmak. Örnek:

    Liste1'i girin: a,,b
    Liste2'i girin: ab,bab
    Sonuç:  ['aab', 'abab', 'ab', 'bab', 'bab', 'bbab']
Gördüğünüz gibi `ab` ve `bab` dizeleri basıldı. `Λ` işaretini listenin başında kullanmak istiyorsanız `,b,ab` gibi bir tanımlama yapmanız yeterlidir.

İki dil'de de `Λ` işareti varsa ve bu dil'leri çarparsak, çıkan sonuçta da `Λ` işareti olması gerekir. Bunu anlayabilmek için boş stringlere bakacağız. yani `''` bunlara:

    Liste1'i girin: ,a,ba
    Liste2'i girin: b,,a
    Sonuç:  ['b', '', 'a', 'ab', 'a', 'aa', 'bab', 'ba', 'baa']
Yukarıdaki çıktıda 2. eleman `''` şeklindedir. Bunun anlamı orada `Λ` vardır.
## Dil Listelerini Karşılaştır Nasıl Çalışır?
Basit bir kullanımı var. Liste1 ve Liste2'ye dil'leri giriyorsunuz ve program size aynı olup olmadığını söylüyor. Bu kısım, işlemlerinizin doğru olup olmadığını kontrol etmenize yardımcı olur. Örnek:

    Liste1'i girin: aa,bb,cc
	Liste2'i girin: cc,aa,bb
        
    Bu listeler birbiriyle aynı!
    -----------------------------------------
    Liste1'i girin: aa,bb,cc
	Liste2'i girin: cc,xx,aa
    
	Bu listeler aynı değil!

**Unutmayın, siz programı kapatmadan program çalışmayı sonlandırmaz.**
