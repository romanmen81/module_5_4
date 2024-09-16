class House:
    houses_history = []  # Атрибут класса для хранения истории названий домов

    def __new__(cls, *args, **kwargs):
        # Создаем новый объект и добавляем название дома в список истории
        instance = super(House, cls).__new__(cls)
        if args:
            cls.houses_history.append(args[0])  # Добавляем название дома из аргументов
        return instance

    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name  # Имя дома
        self.number_of_floors = number_of_floors  # Количество этажей в доме

    def __del__(self):
        # Метод для удаления объекта
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
            if self.number_of_floors < 0:
                self.number_of_floors = 0  # Не допускаем отрицательное количество этажей
            return self
        return NotImplemented

    def __isub__(self, value):
        return self.__sub__(value)

    def is_multistory(self):
        return self.number_of_floors > 1

    def info(self):
        return {
            "name": self.name,
            "number_of_floors": self.number_of_floors
        }

# Пример использования класса House
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
del h1