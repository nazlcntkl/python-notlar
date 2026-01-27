my_list = [1,2,3]
my_tuple = 1,2,3,1    #değiştirilemez

print(type(my_list))
print(type(my_tuple))


my_list[0] = 2
# my_tuple[0] = 2

my_list.append(3)
sonuc = my_tuple.count(1)


# sonuc = my_tuple
# sonuc = my_list

my_tuple2 = tuple([2,3,4])

print(type(my_tuple2))