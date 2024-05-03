import math

# Toplama işlemi
def toplama(x, y):
    return x + y

# Çıkarma işlemi
def cikarma(x, y):
    return x - y

# Çarpma işlemi
def carpma(x, y):
    return x * y

# Bölme işlemi
def bolme(x, y):
    if y == 0:
        return "Hata! Sıfıra bölme hatası."
    else:
        return x / y

# Karekök alma işlemi
def karekok(x):
    return math.sqrt(x)

# Üs alma işlemi
def kuvvet(x, y):
    return x ** y

# Faktöriyel hesaplama işlemi
def faktoriyel(x):
    return math.factorial(x)

# Kare alma işlemi
def kare(x):
    return x ** 2

# Mod alma işlemi
def mod(x, y):
    return x % y

# Sinüs hesaplama işlemi
def sin(x):
    return math.sin(x)

# Kosinüs hesaplama işlemi
def cos(x):
    return math.cos(x)

# Tanjant hesaplama işlemi
def tan(x):
    return math.tan(x)

# Logaritma alma işlemi
def log(x, base):
    if base == 1:
        return "Hata! Taban 1 olamaz."
    return math.log(x, base)

# Kullanıcıya seçenekler sunma
print("Kullanılabilir işlemler:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("5. Karekök")
print("6. Üs alma")
print("7. Faktöriyel")
print("8. Sayının karesini bulma")
print("9. Mod alma")
print("10. Sinüs")
print("11. Kosinüs")
print("12. Tanjant")
print("13. Logaritma")

# Kullanıcıya seçim yapma ve işlem yapma döngüsü
while True:
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    if secim in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'):
        if secim in ('1', '2', '3', '4', '6', '9'):
            sayi1 = float(input("Birinci sayıyı girin: "))
            if secim == '6':
                kuvvet_degeri = float(input("Üssü girin: "))
                print("Sonuç:", kuvvet(sayi1, kuvvet_degeri))
            else:
                sayi2 = float(input("İkinci sayıyı girin: "))
                if secim == '1':
                    print("Sonuç:", toplama(sayi1, sayi2))
                elif secim == '2':
                    print("Sonuç:", cikarma(sayi1, sayi2))
                elif secim == '3':
                    print("Sonuç:", carpma(sayi1, sayi2))
                elif secim == '4':
                    print("Sonuç:", bolme(sayi1, sayi2))
                elif secim == '9':
                    print("Sonuç:", mod(sayi1, sayi2))
        elif secim == '5':
            sayi = float(input("Karekök almak istediğiniz sayıyı girin: "))
            print("Sonuç:", karekok(sayi))
        elif secim == '7':
            sayi = float(input("Faktöriyelini almak istediğiniz sayıyı girin: "))
            print("Sonuç:", faktoriyel(int(sayi)))
        elif secim == '8':
            sayi = float(input("Karesini almak istediğiniz sayıyı girin: "))
            print("Sonuç:", kare(sayi))
        elif secim in ('10', '11', '12'):
            aci = float(input("Açıyı derece cinsinden girin: "))
            aci_rad = math.radians(aci)
            if secim == '10':
                print("Sonuç:", sin(aci_rad))
            elif secim == '11':
                print("Sonuç:", cos(aci_rad))
            elif secim == '12':
                print("Sonuç:", tan(aci_rad))
        elif secim == '13':
            sayi = float(input("Logaritma almak istediğiniz sayıyı girin: "))
            taban = float(input("Logaritmanın tabanını girin: "))
            print("Sonuç:", log(sayi, taban))
    else:
        print("Geçersiz giriş!")

    devam = input("Başka bir işlem yapmak istiyor musunuz? (E/H): ")
    if devam.upper() != 'E':
        break
