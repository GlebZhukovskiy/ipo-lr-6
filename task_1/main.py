#Gleb Zhukovskiy

i = 0
spisok = []
a = "kuzma cherni"
c = 0
while i <6:
    a = str(input("Введите элемнт в список "))
    spisok.append(a)
    i += 1
print(spisok)
for i in spisok:
    if "а" == i:
        c += 1
        print(c)
    else:
        print("Буквы а нет в списке")
