# Easy
# Опишите несколько классов Towncar, Sportcar, Workcar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - булевое значение
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
# о том, что машниа поехала, остановилась, повернула(куда)


# class TownCar:
#
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}!'.format(self.name, direction))
#
#
# class SportCar:
#
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}!'.format(self.name, direction))
#
#
# class WorkCar:
#
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}!'.format(self.name, direction))
#
#
# class PoliceCar:
#
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = True
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}!'.format(self.name, direction))


# Задача - 2
# Посмотрите задачу 1 и подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него


# class Car:
#
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def go(self):
#         print('{} is going!'.format(self.name))
#
#     def stop(self):
#         print('{} is stopping!'.format(self.name))
#
#     def turn(self, direction):
#         print('{} is turning to {}!'.format(self.name, direction))
#
#
# class TownCar(Car):
#     pass
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, has_turbo=True):
#         super().__init__(speed, color, name)
#         self.has_turbo = has_turbo
#
#
# class WorkCar(Car):
#     pass
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name):
#         super().__init__(speed, color, name)
#         self.is_police = True
#
#
# sport_car = SportCar(240, 'red', 'sport car')
# town_car = TownCar(140, 'gray', 'city car')
# work_car = WorkCar(90, 'Yellow', 'work car')
# police_car = PoliceCar(210, 'Blue', 'police car')
#
#
# print(sport_car)


# NORMAL
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


# class Person:
#     def __init__(self, name, health=100, armor=2, damage=10):
#         self._name = name
#         self._health = health
#         self._armor = armor
#         self._damage = damage
#         self._lvl = 1
#
#     def get_health(self):
#
#         return self._health
#
#     def get_armor(self):
#
#         return self._armor
#
#     def get_damage(self):
#         return self._damage
#
#     def _set_health(self, value):
#         self._health = value
#
#     def hit(self, damage):
#         self._set_health(self._health - damage)
#
#     def _calculate_damage(self, enemy):
#         return self._damage / enemy.get_armor()
#
#     def attack(self, enemy):
#         damage = self._calculate_damage(enemy)
#         enemy.hit(damage)
#
#
# class Player(Person):
#
#     def __init__(self, name, health, armor, damage):
#         super().__init__(name, health, armor, damage)
#         self._experience = 1
#         self._exp_to_next_lvl = 100
#
#     def get_experience(self):
#         return self._experience
#
#     def _is_next_level(self):
#         if self._experience >= self._exp_to_next_lvl:
#             self._lvl += 1
#             self._exp_to_next_lvl *= 2
#
#     def increase_experience(self, value):
#         if value > 0:
#             self._experience += value
#             self._is_next_level()
#
#
# class Enemy(Person):
#
#     def __init__(self, name, lvl):
#         super().__init__(name)
#         self._lvl = lvl
#         self._health *= lvl
#         self._armor *= lvl
#         self._damage *= lvl
#
#
# class Game:
#     def __init__(self, player, enemy):
#         self._player = player
#         self._enemy = enemy
#
#     def start(self):
#         last_attacker = self._player
#         while self._player.get_health() > 0 and self._enemy.get_health() > 0:
#             if last_attacker == self._player:
#                 self._enemy.attack(self._player)
#                 last_attacker = self._enemy
#             else:
#                 self._player.attack(self._enemy)
#                 last_attacker = self._player
#         if self._player.get_health() > 0:
#             print('You win')
#         else:
#             print('You lose')
#
#
#
# player = Player('Igor', 300, 1.2, 10)
# enemy = Enemy('Vasya', 1)
# game = Game(player, enemy)
# game.start()


# HARD
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:

    def __init__(self, name, color):
        self.name = name
        self.color = color


class ToyAnimal(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Animal'


class ToyMult(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Multfilm'


class ToyToxic(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Toxic'


class ToyFactory:

    def create_toy(self, name, color, toy_type):
        self._buy_raw_materials()
        self._sewing()
        self._set_color()
        if toy_type == 'Animal':
            return ToyAnimal(name, color)
        elif toy_type == 'Multfilm':
            return ToyMult(name, color)
        else:
            return ToyToxic(name, color)

    def _buy_raw_materials(self):
        print('Buying materials')

    def _sewing(self):
        print('toy creating(sewing)')

    def _set_color(self):
        print('painting toy')


factory = ToyFactory()
toy = factory.create_toy('Vasya', 'blue', 'Animal')

print(isinstance(toy, ToyMult))
print(isinstance(toy, ToyAnimal))
print(isinstance(toy, Toy))

if isinstance(toy, ToyToxic):
    print('dangerous for kids')
else:
    print('play ')