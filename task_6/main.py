import random #импортируем библиотеку случайнх элементов
random_list = [tuple(random.randint(-10, 10) for _ in range(4)) for _ in range(20)] #создание случайного списка из 20 значений по 4 случайных целых числа от -10 до 10
print("Случайный список: ", random_list) #выводим случайных список

unique_pairs = [] #инициализируем пустой список
for i in range (len(random_list)): #цикл для выбора первого кортежа пары
    for j in range(i + 1, len(random_list)): #цикл для выбора второго кортежа 
        unique_pairs.append((random_list[i], random_list[j])) #добавляем текущую уникальную пару кортежей в список
print("Уникальные пары: ", unique_pairs) #выводим уникальные пары

user_input = int(input("Введите целое число: ")) #запрашиваем ввод целого числа
count = 0 #иницалицируем счетчик пар
for pair in unique_pairs: #цикл перебора каждой пары
    total_sum = sum(pair[0]) + sum(pair[1]) #суммируем все элементы в паре
    if total_sum < user_input: #проверяем меньше ли общая сумма введенного значения
        count += 1 #увеличиваем счетчик
print(f"Количество пар, сумма которых меньше {user_input}: {count}") #выводим итоговое количесво пар