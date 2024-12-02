# Базовый класс Animal
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} издает звук: {self.sound}")

# Подкласс Cat с наследованием от Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Мяу!")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} ({self.color}) мяукает: Мяу-мяу!")

# Подкласс Dog с наследованием от Animal
class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Гав!")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} ({self.color}) лает: Гав-гав!")

# Пример использования классов
def main():
    cat = Cat("Барсик", "серый")
    dog = Dog("Шарик", "коричневый")
    
    cat.make_sound()
    dog.make_sound()

if __name__ == "__main__":
    main()