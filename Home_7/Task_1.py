'''Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе
несколько слов, то они разделяются дефисами.

Фразы отделяются друг от друга пробелами.
Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
и “Пам парам”, если с ритмом все не в порядке

Ввод: пара-ра-рам рам-паМ-папаМ па-ра-па-даМ
Вывод: Парам пам-пам

https://www.cyberforum.ru/python-tasks/thread2820456.html
'''
import os

os.system('cls')

# вариант с all

alp = "аеёиоуыэюя"
word_sug = input().split()
vowel_letters = [sum([True for j in word if j.lower() in alp]) for word in word_sug]

if all(vowel_letters) and len(set(vowel_letters)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")



"""
часть правильного варианта

song = input('Винни, пой! ').lower().split(' ')
print(song) # ['пара-ра-рам', 'рам-пам-папам', 'па-ра-па-дам']
print(len(song)) # 3
temp = set()

list_glas = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
for i in range(len(song)):
    count = 0
    
    for j in range(len(song[i])):
        for k in range(len(list_glas)):
            if song[i][j] == list_glas[k]:
                count +=1
    temp.add(count)
print(temp)


мой неправильный вариант

song = input('Винни, пой! ').lower().split(' ')
print(song) # ['пара-ра-рам', 'рам-пам-папам', 'па-ра-па-дам']
print(len(song)) # 3
temp = set()


list_glas = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
for i in range(len(song)):
    count = 0
    # print(song[i]) # пара-ра-рам
    for j in range(len(song[i])):
        # print(f'{song[i][j]} ', end='') # п а р а - р а - р а м
        for k in range(len(list_glas)):
            if song[i][j] == list_glas[k]:
                count +=1
    temp.add(count)
print(temp)"""

"""
вариант Александра
def vowels_counter(S):
    vowels = list('а е ё и о у ы э ю я'.split())
    vowels_counter = list()
    for i in S:
        counter = 0
        for ch in i:
            if ch in vowels:
                counter += 1
        vowels_counter.append(counter)
    return vowels_counter

# пара-ра-рам рам-пам-папам па-ра-па-дам
s = list("ff ff ff".split())  # можно заменить на input().split()

print("Парам пам-пам" if len(set(r := vowels_counter(s))) == 1 and r[0] != 0 else "Пам парам")
"""