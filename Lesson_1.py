# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут
# длиной m километров? При решении этой задачи
# нельзя пользоваться условной инструкцией if и циклами.
# округление в меньшую сторону при отрицательны числах происходит фактически в большую сторону

"""n = int(input("Введите количество км  \n"))
m = int(input("Введите количество всех км\n"))
print(-(-m//n))"""

# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрести для них.


# a = int(input())
# b = int(input())
# c = int(input())

# a1 = (-a) // 2
# b1 = (-b) // 2
# c1 = (-c) // 2
# print(-(a1 + b1 +c1))

# class1 = 3
# class2 = 3
# class3 = 3

# numberOfDesks = - ((-class1)//2 + (-class2)//2 + (-class3)//2)
# print (numberOfDesks)

# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон
# от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.

# i = int(input())
# j = int(input)
# if i + j - 1 > 0:
#     print(i + j - 1)
# else:
#     print("Недостаточно данных")

# Дано натуральное число. Требуется определить, является ли
# год с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO. Напомним, что в соответствии
# с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

year = int(input())
if year % 4 == 0 and year % 100 != 100 or year % 400 == 0:
    print("yes")
else:
    print("no")