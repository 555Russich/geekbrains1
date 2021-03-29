# Функции и работа с файлами

# max(1, 2, 3)
# print(max('zz', 'aaa', key=len))
# print(round(1.98754, 3)) # 3 знака после запятой

for index, char in enumerate('qwerty', start=3):
    print(index, char)

# def say_hello(name): # создаем функцию, которую можем вызывать в последствии
#     print('Hello', name)
# say_hello('Ivan')

# def average(numbers):
#     count = len(numbers) # сколько всего значений в листе
#     all_sum = sum(numbers) # считаем сумму значений
#     # print(all_sum / count)
#     answer = all_sum / count
#     return answer
#
# average_number = average([1, 2, 3, 4, 5, 6, 7, 8 ,9])
# print(average_number)

# def print(text): # называем функцию существующей функией и она перестает работать
#     pass
# print('bla')

# x = 100
# def test(x):
#     # global x
#     x += 1
#     return x
# x = test(x)
# print(x)

# def my_func(name, surname='Guest'): # сперва обязательный аргумент. необяз можно не выводить
# print(name, surname)
# my_func('Ivan')

# def func(name, *args): # n кол-во аргументов в args. !!!
#     print(name) # !!! *abc не работает, только *args выдает только tuple(картеж)
#     print(args)
# func('Ivan', 10, 20, 30, 40, 50, 60, 70, 80, 90)

# def func(name, age, surname):
#     print(name, surname, age)
# func(surname='Ivanov', age=99, name='Ivan')

# def func(name, **kwargs): # !!! usefull
#     print(name, kwargs)
# func('Ivan', surname='Popin', age=50, flat=160)

# def func(**kwargs): # !!! usefull
#     print(kwargs)
# func(name='Ivan', surname='Popin', age=50, flat=160)

names = ['Ivan', 'Oleg', 'Sosed']
ages = (35, 45, 80)
#
for name, age in zip(names, ages):
    print(name,'-', age)
# print(list(zip(names, ages)))
# print(dict(zip(names, ages)))

# print(pow(10, 2))  # pow возводит x в степень y


# def my_pow(x):
#     return x ** 2
#
#
# data = [-2, -10, 6, 19]
# result = []
#
#
# # for num in data:
# #     result.append(my_pow(num))
# # print(result)
#
# # result_1 = tuple(map(my_pow, data)) # скобки у функции не ставить, иначе она сразу вызовется. можно list не tuple
# # print(result_1)
#
# def my_filter(x):
#     return x > 0
#
#
# result_2 = list(filter(my_filter, data)) # в отличие от map возвращает либо тру либо фолс
# print(result_2)


# data = [-2, -10, 6, 19]

# result = list(map(lambda x: x ** 2, data))
# print(result)

# result = list(filter(lambda x: x > 0, data))
# print(result)


# РАБОТА С ФАЙЛАМИ

# file = open('1') # r(ead) - читает файл, но можно и без него
# for line in file:
#     # print(line, end='')
#     print(line.strip())

# file = open('2.txt', 'w')
# file.write('1000')
# file.close()

# w(rite) - создает файл и удаляет все прошлые данные в нем...
# a(ppend) - добавить в конец (дозапись)
# a+ и w+ редкие, дозапись и чтение/создание

# file = open('2.txt', 'a+', encoding='utf-8')
# file.write('\na\n')
# file.seek(0)
# print(file.readlines())
# file.close()

# with open('2.txt') as f: #автоматически закрывает файл после qwe
#     for line in f:
#         print(line.strip())
#
# print('qwe')