customers = ["ali","ahmet","ayşe","azra"]
orders_totals = [12,13,5,15]

# 'ali' kullanıcı adıyla yapılan 5 liralık siparişi listeye ekleyiniz.

# customers.append("ali")
# orders_totals.append("5")

# sonuc = customers
# sonuc = orders_totals

# Son eklenen siparişi siliniz.

# customers.pop()
# orders_totals.pop()

# sonuc = customers
# sonuc =orders_totals

# Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
   #'<username>' isimli müşterinin sipariş toplamı '<10>' liradır.

# sonuc= f"{customers[0]} isimli müşterinin sipariş toplamı {orders_totals[0]} liradır"


# Müşterileri alfabetik olarak sıralayınız. 

# customers.sort()
# sonuc = customers

# Sipariş toplamlarını azalan şekilde sıralayınız.

# order_totals.sort()
# order_totals.reverse()
# sonuc = order_totals

# En düşük sipariş hangisidir?

# sonuc = min(orders_totals)

# 'ali' isimli kullanıcının kaç tane siparişi vardır?

# sonuc = customers.count('ali')

# customers listesinden 'ahmet' isimli kullanıcıyı siliniz.

# customers.pop(1)  yada customers.remove('ahmet')
# sonuc = customers


# Listelerdeki tüm içerikleri siliniz.

# customers.clear()
# orders_totals.clear()
# sonuc = customers
# sonuc = orders_totals


# Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

username =input('musteri adi: ')
toplam = input('toplam: ')

customers.append(username)
orders_totals.append(toplam)

print(customers)
print(orders_totals)