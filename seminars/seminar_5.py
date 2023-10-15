# ПРО ФУНКЦИИ:
# Можно окрыть книгу "Byte of Python" и найти главу про функции, там очень хорошо раскрыта эта тема.
# Можно посмотреть о функциях тут: https://www.youtube.com/watch?v=DJAlfolEv9A
# О переменных количествах аргументов (*args, **kwargs): https://stepik.org/lesson/372076/step/1?unit=359630
# О тайп-хинтингах: https://proglib.io/p/annotacii-tipov-v-python-vse-chto-nuzhno-znat-za-5-minut-2022-01-30
# Всемогущие декораторы: https://www.youtube.com/watch?v=Va-ovLxHmus&t=2s
# Про генераторы: https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-functions/theory_unit
# Декораторы (начинаем с замыканий и дальше по плейлисту до декораторов включительно): https://www.youtube.com/watch?v=lA979PBb0TY









# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


def fibo(n):
    if n in (0, 1):
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(7))

    
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


n = list(map(int, input().split()))
print(*n)

def haker(n):
    maxx = max(n)
    minn = min(n)
    for i in range(len(n)):
        if n[i] == maxx:
            n[i] = minn
    return(n)

print(*haker(n))

#  Второй вариант




n = [1, 3, 3, 3, 4]
print(n)

def func(n):
    maxx = max(n)
    minn = min(n)
    for i in range(len(n)):
        if n[i] == maxx:
            n[i] = minn
    return n

print(func(n))
print(sorted(n))






# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def chek_div(n):
    if n < 4:
        return 'Это простое число'
    for i in range(2, n):
        if n % i == 0:
            return 'Число не является простым'
    return 'Это простое число'

n = int(input('Введите число: '))
print(chek_div(n))


# Второй вариант


def func(n):
    for i in range(2, n):
        if n % i == 0:
            return 'целое'
    return 'простое'


n = int(input())
print(func(n))


# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def sort(n):
    s = input()
    if n != 1:
        sort(n - 1)
    print(s, end=' ')

n = int(input())
sort(n)

# Второй вариант

def func(n):
    number = input()
    if n == 1:
        return number
    return func(n - 1) + " " + number

n = int(input())
print(func(n))



