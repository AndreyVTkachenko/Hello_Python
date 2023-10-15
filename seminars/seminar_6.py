# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива (каждое число вводится с новой строки).

def func(first_list, second_list):
    answer = []
    for value in first_list:
        if value not in second_list:
            answer.append(value)
    return answer

first = int(input("Введите количество элементов первого массива: "))
first_list = list()

for i in range(first):
    value = int(input("Введите элемент первого  массива: "))
    first_list.append(value)

second = int(input("Введите количество элементов второго массива: "))
second_list = list()

for i in range(second):
    value = int(input("Введите элемент второго массива: "))
    second_list.append(value)


print(func(first_list, second_list))





# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


def func(array):
    count = 0
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i+1] < array[i]:
            count += 1
    return count

num = int(input("Введите количество элементов: "))
array = list()

for i in range(num):
    value = int(input(f'Введите {i + 1} элемент: '))
    array.append(value)


print(func(array))





# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.


def func(numbers):
    count = 0
    for i in range(len(numbers)):
        if i in range(len(numbers)):
            count += 1
    if count >= 2:
        count = count // 2
    return count

n = int(input("Введите количество элементов: "))
numbers = list()
for i in range(n):
    value = int(input(f'Введите {i + 1} элемент: '))
    numbers.append(value)


print(f"Количество пар элементов, равных друг другу: {func(numbers)}")






# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).


# def my_func(n):
#     sum_div = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum_div += i
#     return sum_div

# def yours_func(k):
#     friendly_couple = []
#     for n in range(1, k):
#         m = my_func(n)
#         if m > n and my_func(m) == n:
#             friend_pair = (n, m)
#             friendly_couple.append(friend_pair)
#     return friendly_couple


# k = int(input("Введите число: "))
# pairs = yours_func(k)

# print("Пары дружественных чисел:")
# for pair in pairs:
#     print(pair[0], pair[1])


# def func(a=[]):
#     a.append(1)
#     print(a)

# func()
# func()
# func()


# def func(a=None):
#     if a is None:
#         a = []
#     a.append(1)
#     print(a)

# func()
# func()
# func([4, 5, 6])


# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

def func(my_list, yours_list):
    answer = list()
    for value in my_list:
        if value not in yours_list:
            answer.append(value)
    return answer

def generation(n):
    my_list = list()
    for i in range(n):
        value = int(input("Введите элемент первого  множества: "))
        my_list.append(value)
    return my_list


m = int(input("Введите количество элементов первого множества: "))
my_list = generation(m)

k = int(input("Введите количество элементов второго множества: "))
yours_list = generation(k)


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 
# 1 5 1 5 1
# Вывод: Вывод:
# 0 2

def func(array):
    count = 0
    for i in range(1, len(array)-1):
        if array[i - 1] < array[i] > array[i + 1]:
            count += 1
    return count

array  = [1, 5, 1, 5, 1, 5, 2]
print(func(array))


# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 1 2 3 2 3 Вывод:2


# def func(numbers):
#     count = 0
#     for i in range(len(numbers)):
#         if numbers[i] in (numbers[i+1:]):
#             count += 1
#         if count > 2:
#             count // 2
#         return count
    
# # if i in range(i+1,len(numbers)):

# numbers = [1, 2, 3, 2, 3]
# print(func(numbers))



def search_dbl(start_list):
    count = 0
    for i in range(len(start_list) - 1):
        for j in range(i+1, len(start_list)):
            if start_list[i] == start_list[j]:
                count += 1
    return count

start_list = [1, 2, 1, 2, 2, 3, 4]
print(search_dbl(start_list))


# count = 0
# for i in range(len(list_n)-1):
#     count +=  list_n[i+1:].count(list_n[i])
# print(count)


# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300 Вывод:220 284


# def my_func(n):
#     sum_dif = 0
#     for i in range(1, n//2 + 1):
#         if n % i == 0:
#             sum_dif += i
#     return sum_dif
# # print(my_func(n))


# k = 300
# for i in range(2, k):
#     n_1 = my_func(i)
#     n_2 = my_func(n_1)
#     if (n_2 == i) and (n_1 != n_2) and (n_2 < n_1):
#         print(n_2, n_1)

        
def get_summ(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += i
    return count


k = 300
for num_1 in range(1, k):
    num_2 = get_summ(num_1)
    sum_del_num_2 = get_summ(num_2)
    
    if (num_1 == sum_del_num_2) and (num_1 != num_2) and (num_1 < num_2):
        print(num_1, num_2)


