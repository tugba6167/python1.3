def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif islem == '-':
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif islem == '*':
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif islem == '/':
        if sayi2 == 0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:
            print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Geçersiz işlem türü!")

# Kullanıcıdan giriş alalım
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("İşlem türünü girin (+, -, *, /): ")

hesap_makinesi(sayi1, sayi2, islem)
