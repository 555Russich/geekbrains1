# def print_human_name(human):
#     print(human['name'])
#
# h1 = {'name': 'qwe'}
# h2 = {'name': 'asd'}
# h3 = {'name': 'zxc'}
#
# print_human_name(h1)
# print_human_name(h2)
# print_human_name(h3)

# Когда функция находится внутри класса, она называется методом

class Phone:
    def __init__(self, phone_model):  # Системный метод. dir(phone1) - все методы
        self.model = phone_model
        self._loading()
        self._serial_number = 9519359

    def get_serial_number(self):  # Способ создания функции выдающей серийный номер,
        # чтобы не выдавать инкапсулируемую переменную
        return self._serial_number

    def _loading(self):
        print('loading')

    def call(self):
        print('phone is calling')

# phone1 = Phone('nokia9900')
# # print(dir(phone1))
# phone2 = Phone('sony ericson')
#
# # phone1.call()
# # phone2.call()
#
# phone1._loading()
# print(phone1.get_serial_number())


# Наслдедование
class SmartPhone(Phone):

    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')

# my_smart_phone = SmartPhone('Ivanfon')
# my_smart_phone.sms()
# print(my_smart_phone.get_serial_number())


class Iphone(SmartPhone):

    def __init__(self, phone_model):
        super().__init__(phone_model)  # super() - находит родителя, находит init и передаёт в него phone_model
        print('apple logo')
        # SmartPhone.__init__(self, phone_model)  # 2-ый вариант как унаследовать и модифицировать init (скопировать)
        # print('apple logo')

    def sms(self):  # Чтобы перезаписать метод, просто назвать его также.
        # Например, СМС перешли в аймэссэйдж у айфона, поэтому его необходимо переопределить
        print('iMessage')

    def player(self):
        print('playing music')

    def browser(self):
        print('browser is opening')

# iphone = Iphone('500')
# iphone.player()
# iphone.sms()


class NextGenerationSmartPhone(Iphone):
    def touch_id(self):
        print('scanning finger')

    def pay(self):
        print('paying')


class Samsung(NextGenerationSmartPhone):
    def call(self):
        print('звонилка самсунговская')


class Huawei(NextGenerationSmartPhone):
    def call(self):
        print('звонилка хуавеевская')

samsung = Samsung('s10')
huawei = Huawei('p30')

def my_call(phone):
    phone.call()

my_call(samsung)  # Полиморфизм. Как разные объекты реагируют на одинаковые действия
my_call(huawei)