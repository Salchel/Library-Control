from models.person import Person

class User(Person):
    def __init__(self, name: str, borrowed_books: list = None):
        super().__init__(name)
        self.__borrowed_books: list[str] = borrowed_books if borrowed_books else []

    @property
    def borrowed_books(self) -> list[str]:
        return list(self.__borrowed_books)
    
    def add_borrowed_book(self, title: str): # Добавление книги в список взятых у пользователя
        self.__borrowed_books.append(title)

    def remove_borrowed_book(self, title: str): # Удаление книги из взятх у пользователя
        if title in self.__borrowed_books:
            self.__borrowed_books.remove(title)
        else:
            raise ValueError(f"Книга '{title}' не найдена в списке взятых книг.")
        
    def get_role(self) -> str: # Показать роль
        return "Пользователь"
    
    def show_menu(self) -> str: # Показать меню
        return ("Меню пользователя:\n1. Посмотреть доступные книги \n2. Взять книгу\n3. Вернуть книгу\n4. Мои книги\n0. Выход")
    
    def __str__(self) -> str: # Вывод книг пользователю
        books_info = ", ".join(self.__borrowed_books) if self.__borrowed_books else "нет книг"
        return f"Пользователь: {self.name} | Взятые книги: {books_info}"

    def to_file_string(self) -> str: # Запись в файл пользователя и взятые им книги
        books = ",".join(self.__borrowed_books) if self.__borrowed_books else ""
        return f"{self.name}|{books}"

    @staticmethod
    def from_file_string(line: str) -> "User":
        parts = line.strip().split("|")
        name = parts[0]
        borrowed = parts[1].split(",") if len(parts) > 1 and parts[1] else []
        return User(name, borrowed)