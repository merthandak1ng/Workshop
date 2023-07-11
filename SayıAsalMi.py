



sayi = int(input(" Sayı Giriniz : "))

asalMi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalMi = False
        break



if asalMi:
    print("ASALDIR")
    
else:
    print("ASAL DEĞİLDİR")