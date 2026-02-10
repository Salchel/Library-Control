from models.book import Book
from models.user import User
from models.librarian import Librarian
from services.file_service import FileService


class LibraryService:
    def __init__(self):
        self.__file_service = FileService()
        self.__books: list[Book] = []
        self.__users: list[User] = []

    def load_data(self):
        self.__books = self.__file_service.load_books()
        self.__users = self.__file_service.load_users()
        print(f"Загружено книг: {len(self.__books)}")
        print(f"Загружено пользователей: {len(self.__users)}")

    def save_data(self):
        self.__file_service.save_all(self.__books, self.__users)


    #         ФУНКЦИИ БИБЛИОТЕКАРЯ


    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.__books.append(book)
        self.save_data()
        print(f"Книга «{title}» добавлена в библиотеку.")

    def remove_book(self, title: str):
        for book in self.__books:
            if book.title.lower() == title.lower():
                if not book.is_available():
                    print(f"Книга «{title}» сейчас на руках у {book.borrowed_by}. "
                          f"Сначала верните её.")
                    return
                self.__books.remove(book)
                self.save_data()
                print(f"Книга «{title}» удалена из библиотеки.")
                return
        print(f"Книга «{title}» не найдена.")

    def register_user(self, name: str):
        for user in self.__users:
            if user.name.lower() == name.lower():
                print(f"Пользователь «{name}» уже зарегистрирован.")
                return
        new_user = User(name)
        self.__users.append(new_user)
        self.save_data()
        print(f"Пользователь «{name}» зарегистрирован.")

    def show_all_users(self):
        if not self.__users:
            print("Нет зарегистрированных пользователей.")
            return
        print("Список пользователей")
        for i, user in enumerate(self.__users, 1):
            print(f"  {i}. {user}")

    def show_all_books(self):
        if not self.__books:
            print("В библиотеке нет книг.")
            return
        print("Список всех книг")
        for i, book in enumerate(self.__books, 1):
            print(f"  {i}. {book}")

    
# ФУНКЦИИ ПОЛЬЗОВАТЕЛЯ
    
    
    def show_available_books(self):
        available = []
        for b in self.__books:
             if b.is_available():      # если книга свободна
                 available.append(b)
        if not available:
            print("Нет доступных книг.")
            return
        print("Доступные книги:")
        for i, book in enumerate(available, 1):
            print(f"  {i}. «{book.title}» — {book.author}")

    def borrow_book(self, user_name: str, book_title: str):
        user = self.__find_user(user_name)
        if not user:
            print(f"Пользователь «{user_name}» не найден.")
            return

        # Находим книгу
        book = self.__find_book(book_title)
        if not book:
            print(f"Книга «{book_title}» не найдена в библиотеке.")
            return

        # Пытаемся взять
        try:
            book.borrow(user_name)
            user.add_borrowed_book(book.title)
            self.save_data()
            print(f"Книга «{book.title}» выдана пользователю «{user_name}».")
        except Exception as e:
            print(f"{e}")

    def return_book(self, user_name: str, book_title: str):
        user = self.__find_user(user_name)
        if not user:
            print(f"Пользователь «{user_name}» не найден.")
            return

        book = self.__find_book(book_title)
        if not book:
            print(f"Книга «{book_title}» не найдена в библиотеке.")
            return

        # Проверяем, что именно этот пользователь брал книгу
        if book.borrowed_by != user_name:
            print(f"Книга «{book_title}» не была взята пользователем «{user_name}».")
            return

        try:
            book.return_book()
            user.remove_borrowed_book(book.title)
            self.save_data()
            print(f"Книга «{book.title}» возвращена в библиотеку.")
        except Exception as e:
            print(f"{e}")

    def show_user_books(self, user_name: str):
        user = self.__find_user(user_name)
        if not user:
            print(f"Пользователь «{user_name}» не найден.")
            return

        books = user.borrowed_books
        if not books:
            print(f"У пользователя «{user_name}» нет взятых книг.")
            return

        print(f"\nКниги пользователя «{user_name}»:")
        for i, title in enumerate(books, 1):
            print(f"  {i}. «{title}»")

    def user_exists(self, name: str) -> bool:
        return self.__find_user(name) is not None

    def find_user(self, name: str) -> User | None:
        for user in self.__users:
            if user.name.lower() == name.lower():
                return user
        return None

    def find_book(self, title: str) -> Book | None:
        for book in self.__books:
            if book.title.lower() == title.lower():
                return book
        return None