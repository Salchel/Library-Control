from models.person import Person

class Librarian(Person):
    def __init__(self, name: str):
        super().__init__(name)

    def get_role(self) -> str:
        return "Библиотекарь"
    
    def show_menu(self) -> str:
        return ("Меню библиотекаря:\n1. Добавить новую книгу \n2. Удалить книгу\n3. Зарегестрировать нового пользователя\n4. Список всех пользователей\n5. Список всех книг\n0. Выход")
    
    def __str__(self):
        return f"Библиотекарь: {self.name}"