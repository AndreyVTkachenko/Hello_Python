# Необходимо создать функцию sumNumbers(n), которая будет считатьvсумму всех элементов от 1 до n.

def sum_numbers(n, y):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa

a = sum_numbers(5, 'qwerty')
print(a)



# Функция, которая принимает неограниченное количество аргументов

def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res
print(sum_str('q', 'e', 'r'))
print(sum_str('a', 'd', 'g', 'h'))
# print(sum_str(1, 3, 9, 52)) # Ошибка типа данных

############################################### IMPORT 

import modul_1
print(modul_1.max_1(5, 9))
# либо
from modul_1 import max_1
print(max_1(15, 9))

from modul_1 import * # - Для импорта всех функций из modul_1

import modul_1 as m1
print(m1.max_1(10, 25))




##########################################  RECURSION 

# Пользователь вводит число n. Необходимо вывести n - первых членов последовательности Фибоначчи.

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) 


########################################## АЛГОРИТМЫ

# БЫСТРАЯ СОРТИРОВКА


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([14,5,9,6,8,2,3,7,45,2,1,523,235,33,25,25,64,6,5,4,12,3,6,8,9,4]))



def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        rigth = nums[mid:]
        merge_sort(left)
        merge_sort(rigth)
        i = j = k = 0
        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = rigth[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(rigth):
            nums[k] = rigth[j]
            j += 1
            k += 1    
list_1 = [14,5,9,6,8,2,3,7,45,2,1,523,235,33,25,25,64,6,5,4,12,3,6,8,9,4]
merge_sort(list_1)
print(list_1)
