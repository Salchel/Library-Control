import os
from models.book import Book
from models.user import User


class FileService:
    def __init__(self, data_dir: str = "data"):
        self.__data_dir = data_dir
        self.__books_file = os.path.join(data_dir, "books.txt")
        self.__users_file = os.path.join(data_dir, "users.txt")
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        if not os.path.exists(self.__data_dir):
            os.makedirs(self.__data_dir)
        # Создаём файлы, если не существуют
        for filepath in [self.__books_file, self.__users_file]:
            if not os.path.exists(filepath):
                with open(filepath, "w", encoding="utf-8"):
                    pass

    # Загрузка книг из файла
    def load_books(self) -> list[Book]:
        books = []
        try:
            with open(self.__books_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            books.append(Book.from_file_string(line))
                        except ValueError as e:
                            print(f"Ошибка чтения книги: {e}")
        except FileNotFoundError:
            pass
        return books

    # Загрузка пользователей из файла
    def load_users(self) -> list[User]:
        users = []
        try:
            with open(self.__users_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            users.append(User.from_file_string(line))
                        except ValueError as e:
                            print(f"Ошибка чтения пользователя: {e}")
        except FileNotFoundError:
            pass
        return users

    # Сохранение книг в файл
    def save_books(self, books: list[Book]):
        with open(self.__books_file, "w", encoding="utf-8") as f:
            for book in books:
                f.write(book.to_file_string() + "\n")

    # Сохранение пользователей в файл
    def save_users(self, users: list[User]):
        with open(self.__users_file, "w", encoding="utf-8") as f:
            for user in users:
                f.write(user.to_file_string() + "\n")

    def save_all(self, books: list[Book], users: list[User]):
        self.save_books(books)
        self.save_users(users)
        print("Данные сохранены.")