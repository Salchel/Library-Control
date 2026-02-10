class Book:

    STATUS_AVAILABLE = "Доступна"
    STATUS_BORROWED = "Выдана"

    def __init__(self, title: str, author: str, status: str = None, borrowed_by: str = None):
        self.__title = title.strip()
        self.__author = author.strip()
        self.__status = status if status else self.STATUS_AVAILABLE
        self.__borrowed_by = borrowed_by

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def author(self) -> str:
        return self.__author
    
    @property
    def status(self) -> str:
        return self.__status
    
    @property
    def borrowed_by(self) -> str:
        return self.__borrowed_by
    
    def is_available(self) -> bool:
        return self.__status == self.STATUS_AVAILABLE

    def borrow(self, user_name: str): #Взять книгу из библиотеки
        if not self.is_available():
            raise Exception(f"Книга '{self.__title}' уже выдана пользователю '{self.__borrowed_by}'.")
        self.__status = self.STATUS_BORROWED
        self.__borrowed_by = user_name

    def return_book(self): #Вернуть книгу в библиотеку
        if self.is_available():
            raise Exception(f"Книга '{self.__title}' и так находится в библиотеке.")
        self.__status = self.STATUS_AVAILABLE
        self.__borrowed_by = None

    def __str__(self) -> str: # Добавление владельца книги если та занята
        status_info = f"[{self.__status}]"
        if self.__borrowed_by:
            status_info += f" (у {self.__borrowed_by})"
        return f"«{self.__title}» — {self.__author} {status_info}"
    
    def to_file_string(self) -> str: # Добавление в файл
        if self.__borrowed_by:
            borrowed = self.__borrowed_by 
        else:
            borrowed = ""
        return f"{self.__title}|{self.__author}|{self.__status}|{borrowed}"
    
    @staticmethod
    def from_file_string(line: str) -> "Book": # Выво из файла
        parts = line.strip().split("|")
        if len(parts) < 3:
            raise ValueError(f"Некорректная строка книги: {line}")
        title = parts[0]
        author = parts[1]
        status = parts[2]
        if len(parts) > 3 and parts[3]:
            borrowed_by = parts[3]
        else:
            borrowed_by = None
        return Book(title, author, status, borrowed_by)