from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def show_menu(self):
        pass

class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Библиотекарь"

    def show_menu(self):
        return "Меню"

lib = Librarian("Анна")
print(lib.get_role())
print("Всё работает!")