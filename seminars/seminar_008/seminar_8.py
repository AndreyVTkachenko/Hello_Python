# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций.
# Ваша программа не должна быть линейной







# with open('directory.txt', 'w') as data:
#     data.write('Ivanov, Ivan, 123456789 \n')
#     data.write('Petrov, Petr, 234567891 \n')


# def added_cont():





# Внесение данных в справочник
def write_person(second_name, first_name, phone):
    with open('directory.txt', 'a') as f:
        f.write(f'\n{second_name}, {first_name}, {phone}')

def write_data():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    write_person(second_name, first_name, phone)

write_data()

def find_person():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    data = open('directory.txt', 'r')
    for line in data:
        if second_name or first_name or phone:
            print(data.readline())
    data.close()

find_person()

def find_person_correct():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    data = open('directory.txt', 'r')
    for line in data:
        if second_name or first_name or phone:
            print(data.readline())
    data.close()

path = 'directory.txt'













# добавлено изменение контакта и его удаление
def update_contact():
    search_name = input('Введите фамилию контакта, который хотите изменить: ')
    with open("directory.txt", "r") as f:
        lines = f.readlines()
    with open("directory.txt", "w") as f:
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.lower() not in contact[0].lower():
                print('Контакт не найден.')
            else:    
                new_second_name = input('Введите новую фамилию: ')
                new_first_name = input('Введите новое имя: ')
                new_phone = input('Введите новый номер телефона: ')
                f.write(f'{new_second_name}, {new_first_name}, {new_phone}\n')
                print('Контакт успешно изменен!')                        
                f.write(line)




def delete_contact():
    search_name = input('Введите фамилию контакта, который хотите удалить: ')
    with open("directory.txt", "r") as f:
        lines = f.readlines()
    with open("directory.txt", "w") as f:
        contact_found = False
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.title() not in contact[0].title():
                f.write(line)
            else:
                contact_found = True
        if contact_found:
            print('Контакт успешно удален!')
        else:
            print('Контакт не найден.')







            # семинар тестировщиков####################################################################################







def readall(nm):
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())


def write_1(nm):
    str_new1 = input('Фамилия: ')
    str_new2 = input('Имя: ')
    str_new3 = input('Отчество: ')
    str_new4 = input('Телефон: ')
    str_new = '\n' + str_new1 + ', ' + str_new2+ ', ' + str_new3+ ', ' + str_new4
    with open(nm, 'a', encoding='utf8') as txt_file:
        txt_file.write(str_new)


def find_item(nm):
    item = input('Характеристика: ')
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if item.lower() in line.lower():
                print(line.strip())
                
                
def find_item_2(nm):
    item = input('Что ищем: ')
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)
            

def sort_data(nm):
    list_1 = []
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file: line = line.split(', ')
        list_1.append(line)
        list_1.sort(key=lambda person: person[item_type])
        with open(nm, 'w', encoding='utf8') as txt_file:
            for line in list_1: line = ', '.join(line)
            txt_file.write(line)





# write_1('data.txt')
# readall('data.txt')
# find_item('data.txt')
# find_item_2('data.txt') sort_data('data.txt')



###############################################################################################################################
###############################################################################################################################
###############################################################################################################################



def add_person():
    name_first = input('Введите имя: ')
    name_last = input('Введите фамилию: ')
    phone_num = input('Введите телефон: ')
    with open('phone_book.txt', 'a', encoding='utf-8') as book:
        book.write(f'{name_first} {name_last} {phone_num}\n')
        
        
def create_file():
    with open('phone_book.txt', 'w', encoding='utf-8') as book:
        book.write('Имя Фамилия Телефон\n')
        
        
def search_name():
    name_search = input('Введите имя для поиска: ')
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        for line in book:
            if name_search.lower() == (note:=line.strip('\n').split())[0].lower():
                return note
    return "Запись не найдена"


def search_surname():
    surname_search = input('Введите фамилию для поиска: ')
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        for line in book:
            if surname_search.lower() == (note:=line.strip('\n').split())[1].lower():
                return note
    return "Запись не найдена"


def search_phone():
    phone_search = input('Введите фамилию для поиска: ')
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        for line in book:
            if phone_search.lower() == (note:=line.strip('\n').split())[2].lower():
                return note
    return "Запись не найдена"


def main():
    print('1) Создать файл телефонной книги ', '2) Добавить запись в телефонную книгу', '3) Найти запись по имени', '4) Найти запись по фамилии', '5) Найти запись по телефону', '6) Выход' , sep='\n', end='\n')

    match input():
        case '1':
            create_file()
        case '2':
            add_person()
        case '3':
            print(search_name())
        case '4':
            print(search_surname())
        case '5':
            print(search_phone())
        case '6':
            print("Good bye")
            
main()
