from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError ("Имя не может быть пустым")
        self.__name = value.strip()

    @abstractmethod
    def get_role(self) -> str:
        pass

    @abstractmethod
    def show_menu(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.get_role()}: {self.name}"