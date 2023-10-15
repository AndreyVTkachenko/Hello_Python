# СПИСКИ

list_1 = [] # пустой
list_1 = list() # через функцию
print(list_1)
list_1 = [1, 2, 3, 4, 5, 10]
print(list_1)
print(*list_1) # вывод без скобок и разделителей


for i in list_1:
    print(i)

print(len(list_1)) # размер списка

print(list_1[0]) # обращение к нулевому элементу
print(list_1[5]) # обращение к пятому элементу
print(list_1[-1]) # обращение к первому элементу списка С КОНЦА


print(list_1)
list_1.append(77) # добавление значения в список
print(list_1)


list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)

list_1 = [2, 5, 9, 7, 26, 14, 49]
print(list_1)
a = list_1.pop()
print(a)
print(list_1.pop()) #  удаление последнего элемента списка, также функция возвращает его.
print(list_1)


list_1 = [2, 5, 9, 7, 26, 14, 49]
print(list_1.pop(0)) # удаление конкретного элемента списка
print(list_1)


list_1 = [2, 5, 9, 7, 26, 14, 49]
print(list_1.insert(2, -55)) # добавление элемента (555) на нужную позицию (2)
print(list_1)


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])                        # 1
print(list_1[1])                        # 2
print(list_1[-1])                       # 10
print(list_1[-5])                       # 6
print(list_1[:])                        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])                       # [1, 2]
print(list_1[len(list_1)-2:])           # [9, 10]                
print(list_1[2:9])                      # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])                    # []
print(list_1[0:len(list_1):6])          # [1, 7] с шагом 6
print(list_1[::6])                      # [1, 7] с шагом 6

##################################################################################################

# КОРТЕЖИ

t = ()
print(type(t))
r = (1)
t = (1, 2, 3, ) # в кортеже в конце ВСЕГДА стоит запятая
print(type(r))
print(type(t))

v = [1, 5, 9]
print(type(v))
print(v)
v = tuple(v)
print(type(v))
print(v)

# a, b = 1, 2
# a = b = 1

a, b, c = v
print(a, b, c)


t = (1, 2, 3, 5)
for i in range(len(t)):
    print(t[i])
# t[0] = 7 ошибка!!!, т.к. кортеж неизменяем

#####################################################################################

# СЛОВАРИ

d = {}      # создание словаря
d = dict()  # создание словаря

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)

d['e'] = 'erty'
print(d)

print(d['q']) # вывод по ключу


dictionary = {}
dictionary = {'up': '|\|', 'left': '<-', 'down': '|/|', 'regth': '->'}
print(dictionary)
dictionary[895] = 65496
print(dictionary)
del dictionary['left'] # удаление элемента
print(dictionary)

# вывод ключей:
for item in dictionary:
    print(item)

# вывод ключей и их значений
for items in dictionary:
    print('{}: {}'.format(items, dictionary[items]))

for (k, v) in dictionary.items(): # k - ключ, v - значение
    print(k, v)
print(dictionary.items())


###################################################################################

# МНОЖЕСТВА (содержат только уникальные значения)
q = set()                           # создание пустого множества
colors = {'red', 'green', 'blue'}
print(colors)

colors.add('grey') # добавление элемента
print(colors)

colors.remove('red') # удаление элемента
print(colors)
colors.discard('red') # удаление элемента. если он отсутствует - не выдаёт ошибку
print(colors)

colors.clear() # удаление всех элементов
print(colors)


##############################  Операции со множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy()                                        # c = {1, 2, 3, 5, 8}
print(c)
u = a.union(b)                                      # u = {1, 2, 3, 5, 8, 13, 21} объединение / только уникальные значения
print(u)
i = a.intersection(b)                               # i = {8, 2, 5} пересечение / совпадающие элементы
print(i)
dl = a.difference(b)                                # dl = {1, 3} разность / из а убираем совпадающие элементы с b
print(dl)
dr = b.difference(a)                                # dr = {13, 21} разность / из b убираем совпадающие элементы с a
print(dr)
q = a.union(b).difference(a.intersection(b))        # {1, 21, 3, 13}
print(q)

#################################   Замороженные множества

a = {1, 8, 6}
b = frozenset(a) # множество b нельзя изменить
print(b)









