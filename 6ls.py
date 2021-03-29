# Press 'ctrl' and  to see some description of methods, classes and other
# Press 'alt' to write in many lines in a row
# Right click to Refractor

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
# # + - / *
# # 4 + 3 # __add__
#
# car = Car()
# module = 'condition'
#
# car + module # car + module = car.__add__(module)
# print(car.modules)
# print(dir(car))



# raise ZeroDivisionError # raise "Ошибка" - Поднимает ошибку

# import os
#
#
# class LogReader:  # Считаваем все файлы, как будто один файл
#     def __init__(self):
#         self.files = []  # список открытых файлов
#
#         for file in os.listdir():  # Получаем список всех файлов и папок
#             if os.path.isdir(file):  # если папка, то дальше. Если это файл, то
#                 continue
#             if file.startswith('log'):  # .startswith - стартовый слог на который начинается файл
#                 file_descriptor = open(file, encoding='UTF-8')  # открытый файл в оперативке
#                 self.files.append(file_descriptor)  # добавляем открытые файлы
#
#         self.i = 0  # i - счетчик обращения к файлам
#
#     def __del__(self):  # деструктор. Закрывает каждый файлю. Обратен методу init
#         for file_descriptor in self.files:
#             file_descriptor.close()
#         print('Files closed')
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.i < len(self.files):
#             for line in self.files[self.i]:  # Обращаемся
#                 return line
#             self.i += 1
#         raise StopIteration  # Выбрасываем исключение
#
#
# log_reader = LogReader()
#
# # For запрашивает объект итератор
# # Задача итератора вернуть объект, у которого есть метод __next__
#
# for i in log_reader:
#     print(i.strip())  # .strip() - убирает системные символы(пробелы)



# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# # mnogo koda
#
# human = Human('Ivan', 35, 'm')
# print(human.name, human.age, human.sex)

# Теперь мы хотим каким-то образом изменить возраст, провести проверки и т.п.
# Если добавим def get_age... все сломается
# добавляем _ перед age значит инкапсулируем


# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self._age = age
#         self.sex = sex
#
#     @property
#     def age(self):
#         # some checks
#         return self._age
#
# # mnogo koda
#
# human = Human('Ivan', 35, 'm')
# print(human.name, human.age, human.sex)



# class DataBaseConnection:
#
#     def connect(self):
#         print('connecting')
#
#     def select(self):
#         print('selecting')
#
#     def insert(self):
#         print('inserting')
#
# db = DataBaseConnection()
# db.connect()
# db.select()
# db.insert()

# @staticmethod для того чтобы использовать функцию вне класса

# class DataBaseConnection:
#
#     @staticmethod
#     def connect():
#         print('connecting')
#
#     @staticmethod
#     def select():
#         print('selecting')
#
#     @staticmethod
#     def insert():
#         print('inserting')
#
# DataBaseConnection.connect()
# DataBaseConnection.select()
# DataBaseConnection.insert()



# class MyDict(dict): # Получаем наследование от dict
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value)
#         print('Added in dict key:', key, 'value:', value)
#
#     def __getitem__(self, item):
#         print('Getting value for item key', item)
#         return super().__getitem__(item)
#
# my = MyDict()
# my['qwe'] = 999
# my['zxc'] = 228
# print(my['qwe'])