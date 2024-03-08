# *a - раскрывание итерируемого объекта
# Создать множество(set)
#
# 1) Первый Способ:
#
# m={1,2,3}  - множество не содержит дублей
# элементы хранятся в случайном порядке, как и в словаре
# Множество состоит только из неизменяемых объектов (словари и списки не могут содержаться в множестве)
#
# 2) Второй Способ:
#
# m=set('moskva')
# m=set(['m','o','s','k','v','a'])
# m=set(range(5))
# m=set() - пустое множество
# m={} - не множество, а словарь
#
#
# m=[1,2,3,4,5,3,2,1]
# m=list(set(a)) - делает список без дублей
#
# Добавление элементов:
# m.add() - добавляет элемент вконце множества(не нужно писать m=m.add())
# m.update([5,6,7]) - добавляет несколько элементов
# m.update('567') - добавляет несколько элементов
# m.update({2,3,5,4}) - добавляет несколько элементов
# m.update(range(5)   - добавляет несколько элементов
#
# Удаление элементов:
# m.discard(4) - удалит 4 из множества
# m.pop() - удалит случайный элемент
# m.clear - очистит множество
#
#
# ОПЕРАЦИИ:
# len(m) - длина
# if in  или  if not in- есть ли элемент в множестве
# print(a & b) - выведет пересечение двух множеств, т.е те элементы которые есть в обоих множествах
# a&=b - множество a станет равным пересечению этих множеств
# print(a.intersection(b)) - выведет пересечение двух множеств не изменяя их
# a.intersection_update(b) - множество a станет равным пересечению этих множеств  = тоже что и a&=b
# c=(a | b) -  объединяет два множества в одно
# c=a.union(b) -  объединяет два множества в одно
# a|=b - объединяет два множества в одно и присваивает его переменной а
# с=a-b либо a-=b - вычетает из а пересечение двух множеств
# print(a^b) - выводит два множества a и b  за исключением их пересечения
# сравнение:
# a==b
# a<b или a>b - если все элементы хотя бы одного из множеств есть в другом, иначе False
# Индексирование не поддерживается в множествах, как и в словарях
