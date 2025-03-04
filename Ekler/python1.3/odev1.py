def asal_mi(sayi):
    if sayi < 2:
        print(f"{sayi} bir asal sayı değildir.")
        return

    for i in range(2, int(sayi ** 0.5) + 1):  # Sayının kareköküne kadar bölme işlemi yaparız.
        if sayi % i == 0:
            print(f"{sayi} bir asal sayı değildir.")
            return
    
    print(f"{sayi} bir asal sayıdır.")

# Kullanıcıdan giriş alalım
sayi = int(input("Bir sayı girin: "))
asal_mi(sayi)
