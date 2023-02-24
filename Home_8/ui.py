import os

os.system('cls')

from logger import input_data, print_data, change_data 

def interfase():
    print('1. Ввести данные\n'
         '2. Изменить данные\n'
         '3. Удалить данные\n'
         '4. Показать данные\n'
         '5. Выйти из программы\n')
    command = int(input('Введите номер операции: '))

    while command < 1 or command >5:
        print('Вы ошиблись!')
        command = int(input('Введите номер операции: '))

    if command == 1:
        input_data()
    elif command == 2:
        change_data()
    elif command == 3:
        pass
    elif command == 4:
        print_data()
    elif command == 5:
        command = False

# interfase()
