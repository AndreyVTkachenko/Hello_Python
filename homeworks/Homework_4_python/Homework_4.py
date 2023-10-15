# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6 - ввод размера множеств
# 2 4 6 8 10 12 10 8 6 4 2 - ввод элементов 1-го множества
# 3 6 9 12 15 18 - ввод элементов второго множества
# 6 12 - вывод повторяющихся элементов из двух множеств

first = int(input("Введите количество элементов первого множества: "))
first_set = set()

for i in range(first):
    value = int(input("Введите элемент первого  множества: "))
    first_set.add(value)

second = int(input("Введите количество элементов второго множества: "))
second_set = set()
for i in range(second):
    value = int(input("Введите элемент второго  множества: "))
    second_set.add(value)

print(first_set)
print(second_set)

result = first_set.intersection(second_set)
result = list(result)
print(f'Совпадающие элементы множеств: {sorted(result)}')




# Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# Пример
# 4 - ввод количества кустов
# 1 2 3 4 - ввод количества ягод на каждом кусту
# 9 - вывод максимально возможного количества ягод с трёх рядомстоящих кустов

bushes = int(input("Введите количество кустов: "))
berries = list()

for i in range(bushes):
    value = int(input("Введите количество ягод на кусте: "))
    berries.append(value)

counter = list()
for i in range(len(berries)):
    counter.append(berries[i-2] + berries[i-1] + berries[i])
print(f'Максимально возможное количество ягод с трёх рядомстоящих кустов: {max(counter)}')

