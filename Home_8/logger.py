from os import path

from Data_create import name_data, surname_data, phone_data, adress_data, patronymic_data


def input_data():
    name = name_data()
    patronymic = patronymic_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
        
    with open('phone.txt', 'a', encoding='utf-8') as file:
        text_info = file.write(int(input(f'{surname} {name} {patronymic}, {phone}, {adress}')))
        return text_info

def print_data():
    with open('phone.txt', 'r', encoding='utf-8') as text:
        text.readlines()

def change_data():
    change_num = int(input('Введите номер записи для изменения: '))
    change_num -= 1
    change_list = print_data()

    print(f'Внести изменения в запись\n{change_list[change_num]}')

    name = name_data()
    patronymic = patronymic_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()

    change_list = (change_list[:change_num] + [f'{surname} {name} {patronymic}, {phone}, {adress}\n'] + 
                    change_list[change_num + 1:])
    
    with open('phone.txt', 'w', encoding='utf-8') as text:
        text.write(''.join(change_list))

        print('Изменения сохранены')