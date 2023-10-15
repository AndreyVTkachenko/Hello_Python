
# def f(x):
#     return x*x

# print(f(5))
# print(type(f))
# a = f
# print(a(5))
# print(type(a))

# def calc_1(a, b):
#     return a + b

# def calc_2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calc_1, 5, 45)
# math(calc_2, 5, 45)


# calc_1 = lambda a,b: a + b

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)


# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

# data = '15 156 96 3 5 8 52 5'
# print(data)
# data_1 = data.split()
# print(data_1)
# value = list(map(int, data.split()))
# print(value)

# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)



# data = [16, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)



# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)



# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]


#################Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]



# ############################Функция enumerate() позволяет пронумеровать набор данных.
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]


#################################################################################

# colors = ['red', '789654', 'blue']
# data = open('file.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()


################################################################################













