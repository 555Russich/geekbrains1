# HARD
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys

print('sys.argv = ', sys.argv)

# def print_help():
#     print('help')
#     print('mkdir <dir_name>')
#     print('ping - тестовый ключ')
#     ###
#     print('cp <file_name> - copy')
#     print('rm <file_name> - delete (need get acception of this operation)')
#     print('cd <full_path or relative_path> - меняет текущую дерикторию на указанную')
#     print('ls - отображение полного пути текущей директории')
#
#
# def make_dir():
#     if not dir_name:
#         print('Необходимо указать имя директории вторым параметром')
#         return
#     try:
#         os.mkdir(dir_name)
#         print('директория {} создана'.format(dir_name))
#     except FileExistsError:
#         print('директория {} уже существует'.format(dir_name))
#
#
# def ping():
#     print('pong')
#
#
#
# def ls():
print(os.getcwd()) # Полный путь к папке без файла