# Nameofperson =
# Ctrl + d - copy
# ctrl+alt+l делает пробелы

# string types?
# name_of_person = 'Анастасия'
# print(name_of_person[-1]) # Вывод последнего элемента
# print(name_of_person[0:5]) # диапазон вывода
# print(name_of_person[:5]) # так же диапазон без нул
# print(name_of_person[2:])# от второго элемента
# print(name_of_person[0:8:2]) # от:до:шаг
# print(name_of_person[::-1]) # от:до(не включая):шаг

# email = 'welcome@mail.ru'
# index = email.find('@')
# print(email[:index]) # обрезает емэйл до собаки\

# name = 'ЖоПа привет новы й год'
# print(name.lower())
# print(name.upper())
# print(name.capitalize()) # первая заглавная строки
# print(name.title()) # первая заглавная слова
# print(len(name)) # кол-во символов
# print(name.count('Ж')) # считает кол-во символа
# print(name.split()) # разделяет по символу
# print(name.ljust(20,'+')) # вставляет символ справа от str
# print(name.rjust(30,'-')) # вставляет символ слева от str
# .center
# .zfill заполняет нулями сохраняя знаком

# name = 'Ivan'
# age = 30
# money = 200.2
# print('hi', name, 'vam', age, 'let', 'u vas', money)
# result = 'Hello {} вам {} лет у вас {}' . format(name, age, money)
# result = f'Hello {name} вам {age} лет у вас {money}' # 3.5 python and upper
# print(result)


# Списки list types?
# name = 'Sergey'
# humans = ['Ivan', 'Alex', 'Olga', name]
# print(humans[::-1])
# humans[0] = 'Nastya' # замена

# humans.append(10) # добавить в конец
# humans.insert(1, 200) # добавить между
# print(humans.index(name))
# humans.remove('Ivan') # удаление 1го элемента слева-направо
# deleted_element = humans.pop(0) # удаление с запоминанием
# print(humans)
# print(deleted_element)
# print('Olga' in humans)
# print('debil' in humans)

# x = [1, 2, 3, ['qwe', 'asd']] # ctrl+alt+l делает пробелы
# print(x[-1][1])


# cartege (неизменяемый тип данных)
# humans = (1, 2, 3, 4, 5,)
# print(humans[1:3])
# print(list('qwe')) #   qwe --> ['q', 'w', 'e'] стринг в лист
# print(list(humans)) # (1, 2, 3, 4, 5,) --> [1, 2, 3, 4, 5] картеж в лист

# Выводим все значения картежа
humans = (1, 2, 3, 4, 5)
# x = 0
# while x < len(humans):
#     print(humans[x])
#     x = x + 1

for name in humans:
    print(name)

# for letter in 'qwerty':
#     print(letter)

# for i in [1, 2, 3, 4, 5]:
#     print(i, 'hi')

# for i in range(11):
#     print(i, 'jopa')

# human = {'name': 'Илья', 'age': 43, 'money': 39.1}
# human['data'] = [1, 2, 3, 4]
# human['input'] = input()
# print(human['name'])
# print(human['age'])
# print(human['money'])
# print(human.get('qwe'))
# print(human.pop('age'))
# print(human.popitem())

# for key in human.keys():
#     print(key)

# for value in human.values():
#     print(value)

# for key, value in human.items():
#     print(key, value)

# my_set = {1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 6}
# print(my_set)

# my_list = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 6]
# print(my_list)
# print(len(set(my_list)))

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b) # объединение
# print(a == b)
# print(a & b) # пересечение. & - shif+7
# print(a - b)
# print(a ^ b) # все, кроме пересечения