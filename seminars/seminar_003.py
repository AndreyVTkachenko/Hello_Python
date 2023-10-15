# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Вариант_1

my_list = [1, 1, 2, 0, -1, 3, 4, 4]

count = 0
for i in range(len(my_list)):
    if (my_list[i]) not in my_list[:i]:
        count += 1
print(count)

# Вариант_2

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(my_list)))

# Вариант_3

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
your_list = []

for item in my_list:

    if item not in your_list:
        your_list.append(item)
print(f'Различных чисел в списке: {len(your_list)}')

# Вариант_4

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# already_seen = []

# for i in range(len(my_list)):
#     for j in range(len(already_seen)):
#         if my_list[i] == already_seen[j]:
#             break
#         else:
#             already_seen.append(my_list[i])
# print(len(already_seen))

#                                                              Срезы
# arr = [1, 2, 3, 4, 5]
# arr[1:3] -> [2, 3]
# arr[:3] -> [1, 2, 3]
# arr[2:] -> [3, 4, 5]
# arr[:] -> [1, 2, 3, 4, 5]
# arr[::2] -> [1, 3, 5]


# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

# Вариант_1

my_list = [1, 2, 3, 4, 5]
q = 7
k = q % len(my_list)
print(my_list[k + 1:] + my_list[:k + 1])

# Вариант_2

# my_list = [1, 2, 3, 4, 5]
# your_list = []
# q = 3
# j = 0
# for i in range(len(my_list)):
#     if i + k <= len(my_list):
#         your_list.append(my_list[i + q - 1])
#     else:
#         your_list.append(my_list[j])
# print(your_list)

# Вариант_3

my_list = [1, 2, 3, 4, 5]
q = 7
k = q % len(my_list)
for i in range(k):
    temp = my_list.pop()
    my_list.insert(0, temp)
print(my_list)


#                                           Словари

my_dict = {
    142342: 'Стол',
    534534: 'Диван',
    149342: {
        'name': 'Кресло',
        'count': 10,
        'color': 'Зеленое',
        'info': [1, 4, 2]
    }
}

for key, val in my_dict.items():
    print(key, '---', val)


# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_items = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
    "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

new_list = []
for i in range(len(list_items)):
    for value in list_items[i].values():
        if value not in new_list:
            new_list.append(value)
print(new_list)


# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

list_1 = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(list_1)):
    if list_1[i] > list_1[i-1]:
        count += 1
print(count)
