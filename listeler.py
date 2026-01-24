#max-min değeri bulma

sayilar= [1,2,3,4,5,6,7]
isimler= ['betül','tosbik','nazli','x']

sonuc=min(sayilar)
print(sonuc)
sonuc=max(sayilar) 
print(sonuc)
sonuc=min(isimler)
print(sonuc)
sonuc=max(isimler)
print(sonuc)

# ekleme yapma .append() ile

sayilar.append(12)
isimler.append("ahmet")
sonuc=isimler
sonuc2=sayilar
print(sonuc) 
print(sonuc2)

# ekleme yapma .insert() ile

sayilar.insert(-2,60)

sonuc= sayilar

print(sonuc)

#listenin sonuna eklmek için

sayilar= [1,2,3,4,5,6,7]

sayilar.insert(len(sayilar),60)

sonuc= sayilar

print(sonuc)

# pop() ile silme 

sayilar= [1,2,3,4,5,6,7]

sayilar.pop()   # sonuncu (yani -1.) elemanı siler
sonuc = sayilar
print(sonuc)

sayilar= [1,2,3,4,5,6,7]

sayilar.pop(5)
sonuc = sayilar
print(sonuc)

#remove() ile silme
isimler.remove('x')
sonuc=isimler
print(sonuc)

#sıralama

sayilar= [1,2,3,4,5,6,7]

isimler.sort()
sonuc=isimler

print(sonuc)

# .count() ile verilen listenin içinde aradığımız değerden kaç tane olduğunu yazdırılır.
#mesela sayılar.count(4) sonucu 1 olur. çünkü içerisinde 1 adet 4 var.
