# Базовый класс
class BaseClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привет, я базовый класс и мое имя {self.name}"

    def info(self):
        return "Это метод базового класса."


# Производный класс
class ProyzvodClass(BaseClass):
    def __init__(self, name, age):
        # Вызов конструктора базового класса
        super().__init__(name)
        self.age = age

    def greet(self):
        # Переопределение метода greet
        return f"Привет, я производный класс. Меня зовут {self.name} и мне {self.age} лет."

    def info(self):
        # Переопределение метода info
        return f"Это метод производного класса. Мне {self.age} лет."


# Тестирование
if __name__ == "__main__":
    # Создаем экземпляр базового класса
    base_obj = BaseClass("Иван")
    print(base_obj.greet())  # Вызов метода базового класса
    print(base_obj.info())  # Вызов метода базового класса

    # Создаем экземпляр производного класса
    derived_obj = ProyzvodClass("Мария", 25)
    print(derived_obj.greet())  # Вызов переопределенного метода производного класса
    print(derived_obj.info())  # Вызов переопределенного метода производного класса
