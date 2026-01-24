memur1 = 1845
memur2 = 53684
oran = 0.9786758678575
print(memur1 + memur1 * oran)
print(memur2 * memur1 + memur2 * oran * oran)

# **** değişkenlerin tanımlanma kuralları ****

# değişkenler rakamla başlamaz
# değişkenler büyük-küçük harfe duyarlıdır
age = 23
AGE = 4656
print(age)
print(AGE)


# örnek: name = "xxx"

a = 10
b = 20
print(a + b)  # 30

a = "10"
b = "20"
print(a + b)  # 1020
print(type(a + b))  # str

sayi1 = 1
sayi2 = 2
toplam = sayi1 + sayi2
print(toplam)  # Sonuc: 3
