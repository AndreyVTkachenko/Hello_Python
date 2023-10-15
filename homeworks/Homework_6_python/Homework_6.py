# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15




def func(array, a_0, d, count):
    if count == 0:
        return array
    array.append(a_0)
    return func(array, a_0 + d, d, count - 1)

a_0 = int(input('Введите первый член арифметической прогрессии: '))
d = int(input('Введите разность арифметической прогрессии: '))
n = int(input('Введите количество элементов арифметической прогрессии: '))

progression = func([], a_0, d, n)

list_progression = list()
for i in progression:
    list_progression.append(i)
print(*list_progression)


# Решение на коленке
arithmetic_progression = list()

for i in range(n):
    print(a_0 + i*d, end=' ')




# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]



def func(your_list, minn, maxx, index = 0, my_list_index = []):
    if my_list_index is None:
        my_list_index = []

    if index == len(your_list):
        return my_list_index

    if minn <= your_list[index] <= maxx:
        my_list_index.append(index)

    return func(your_list, minn, maxx, index + 1, my_list_index)


your_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minn = int(input('Введите минимальное ограничение: '))
maxx = int(input('Введите максимальное ограничение: '))

print(your_list)
print(f'Диапазон от {minn} до {maxx}')
print(f'Индексы элементов в заданном диапазоне: {func(your_list, minn, maxx, index = 0, my_list_index = [])}')



# Решение на коленке
my_list_index_2 = list()

for i in range(len(your_list)):
    if minn <= (your_list[i]) <= maxx:
        my_list_index_2.append(i)
print(my_list_index_2)


