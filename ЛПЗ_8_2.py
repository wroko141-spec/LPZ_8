# ЛПЗ-8. OOP. Наследование и полиморфизм
# Фамилия Имя Группа

# ==============================================
# ЗАДАЧА 1: Иерархия сотрудников
# ==============================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} выполняет базовую работу"
    
    def get_info(self):
        return f"Сотрудник: {self.name}, зарплата: {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def work(self):
        return f"{self.name} пишет код на {self.programming_language}"
    
    def write_code(self):
        return f"{self.name} пишет код"
    
    def get_info(self):
        return f"{super().get_info()}, язык: {self.programming_language}"


class Designer(Employee):
    def __init__(self, name, salary, software):
        super().__init__(name, salary)
        self.software = software
    
    def work(self):
        return f"{self.name} создает дизайн в {self.software}"
    
    def design(self):
        return f"{self.name} рисует интерфейс"
    
    def get_info(self):
        return f"{super().get_info()}, ПО: {self.software}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def work(self):
        return f"{self.name} управляет командой из {self.team_size} человек"
    
    def manage(self):
        return f"{self.name} проводит совещание"
    
    def get_info(self):
        return f"{super().get_info()}, размер команды: {self.team_size}"


# ==============================================
# ЗАДАЧА 2: Иерархия животных
# ==============================================

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return f"{self.name} издаёт звук"
    
    def move(self):
        return f"{self.name} перемещается"


class Mammal(Animal):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color
    
    def feed_milk(self):
        return f"{self.name} кормит детёнышей"
    
    def make_sound(self):
        return f"{self.name} мычит/мяукает"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span
    
    def fly(self):
        return f"{self.name} летит"
    
    def make_sound(self):
        return f"{self.name} чирикает"


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type
    
    def swim(self):
        return f"{self.name} плавает"
    
    def make_sound(self):
        return f"{self.name} булькает"


# ==============================================
# ЗАДАЧА 3: Система уведомлений
# ==============================================

class Notifier:
    def send(self, message):
        raise NotImplementedError("Метод send() должен быть переопределен")


class EmailNotifier(Notifier):
    def __init__(self, email_address):
        self.email_address = email_address
    
    def send(self, message):
        return f"📧 Email на {self.email_address}: {message}"


class SMSNotifier(Notifier):
    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def send(self, message):
        return f"📱 SMS на {self.phone_number}: {message}"


class PushNotifier(Notifier):
    def __init__(self, device_token):
        self.device_token = device_token
    
    def send(self, message):
        return f"🔔 Push на {self.device_token}: {message}"


def notify_all(notifiers, message):
    """Полиморфная функция: вызывает send() у всех уведомителей"""
    for notifier in notifiers:
        print(notifier.send(message))


# ==============================================
# ТЕСТИРОВАНИЕ
# ==============================================

print("=== ЗАДАЧА 1: Сотрудники ===")
dev = Developer("Иван", 100000, "Python")
des = Designer("Мария", 80000, "Figma")
mgr = Manager("Петр", 150000, 10)

employees = [dev, des, mgr]

for emp in employees:
    print(emp.get_info())
    print(emp.work())
    print()

print("=== ЗАДАЧА 2: Животные (ПОЛИМОРФИЗМ) ===")
animals = [
    Mammal("Лев", 5, "коричневый"),
    Bird("Орёл", 3, "2м"),
    Fish("Акула", 10, "солёная")
]

for animal in animals:
    print(animal.make_sound())  # Полиморфизм!
    print(animal.move())
    print()

print("=== ЗАДАЧА 3: Уведомления (ПОЛИМОРФИЗМ) ===")
notifiers = [
    EmailNotifier("user@mail.ru"),
    SMSNotifier("+7-999-123-45-67"),
    PushNotifier("abc123device")
]

message = "Ваше уведомление!"
notify_all(notifiers, message)