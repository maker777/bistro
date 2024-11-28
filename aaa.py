from abc import ABC, abstractmethod

# Интерфейс стратегии
class SoundStrategy(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class FlyStrategy(ABC):
    @abstractmethod
    def fly(self):
        pass

# Конкретные стратегии
class MeowStrategy(SoundStrategy):
    def make_sound(self):
        return "Meow!"

class BarkStrategy(SoundStrategy):
    def make_sound(self):
        return "Woof!"

class CanFly(FlyStrategy):
    def fly(self):
        return "nononononon"

class CannotFly(FlyStrategy):
    def fly(self):
        return "eyes yes yeeeeeeeeees"

# Базовый класс Animal
class Animal(ABC):
    def __init__(self, sound_strategy, fly_strategy):
        self.sound_strategy = sound_strategy
        self.fly_strategy = fly_strategy

    def perform_sound(self):
        return self.sound_strategy.make_sound()

    def perform_fly(self):
        return self.fly_strategy.fly()

# Конкретные виды животных
class Cat(Animal):
    def __init__(self):
        super().__init__(MeowStrategy(), CannotFly())

class Dog(Animal):
    def __init__(self):
        super().__init__(BarkStrategy(), CannotFly())

class Bird(Animal):
    def __init__(self):
        super().__init__(MeowStrategy(), CanFly())

# Пример использования
if __name__ == "__main__":
    cat = Cat()
    dog = Dog()
    bird = Bird()

    print(f"Cat: {cat.perform_sound()} | {cat.perform_fly()}")
    print(f"Dog: {dog.perform_sound()} | {dog.perform_fly()}")
    print(f"Bird: {bird.perform_sound()} | {bird.perform_fly()}")