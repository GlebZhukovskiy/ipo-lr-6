#Gleb Zhukovskiy

i = 0
spisok = []
a = "kuzma cherni"
c = 0
while i <6:
    a = str(input("Введите элемнт в список "))
    spisok.append(a)
    i += 1
for i in spisok:
   if 'а' in i.lower():
       c +=1
print(f"в списке {spisok} есть {c} строк содержащих букву а")


