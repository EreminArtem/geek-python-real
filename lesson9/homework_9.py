"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния
(красный) составляет 7 секунд,
второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
from itertools import cycle


class TrafficLight:
    __color: str

    def __init__(self):
        self.__color = ''

    def running(self):
        colors_cycles = {'красный': 7, 'жёлтый': 2, 'зелёный': 14}
        for i in cycle(colors_cycles.keys()):
            self.__color = i
            time.sleep(colors_cycles[i])
            print(f'c = {i}')

    def color(self):
        return self.__color


"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    __length: int
    __width: int

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_mass(self, meters, mass_per_meter):
        return meters * self.__width * mass_per_meter * self.__length


# print(Road(10, 100).calculate_mass(100, 100))

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    __income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.position = position
        self.surname = surname
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_total_income(self):
        return sum(self.__income.values())


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'


# pos = Position('n', 's', 'p', 100, 42)
# print(pos.get_total_income())
# print(pos.get_full_name())

"""
4.Реализуйте базовый класс Car. 
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return 'Машина проехала'

    def stop(self):
        return 'Машина машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print('Превышена скорость')
            return
        return self.speed


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print('Превышена скорость')
            return
        return self.speed


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(speed, color, name, True)


"""
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отирисовки')
        return


class Pen(Stationery):
    def draw(self):
        print('Запуск отирисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отирисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отирисовки маркером')

# Stationery('').draw()
# Pen('').draw()
# Pencil('').draw()
# Handle('').draw()
