from models.librarian import Librarian
from models.user import User
from models.person import Person
from services.library_service import LibraryService

def librarian_session(library: LibraryService):
    name = input("Введите имя библиотекаря: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return

    librarian = Librarian(name)
    print(f"\nДобро пожаловать, {librarian}!")

    while True:
        print(librarian.show_menu())
        choise = input("Выберите операцию: ").strip()

        match choise:
            case "1":
                title = input("Название книги: ").strip()
                author = input("Автор: ").strip()
                if title and author:
                    library.add_book(title, author)
                else:
                    print("Название и автор не могут быть пустыми.")

            case "2":
                library.show_all_books()
                title = input("Название книги для удаления: ").strip()
                if title:
                    library.remove_book(title)

            case "3":
                user_name = input("Имя нового пользователя: ").strip()
                if user_name:
                    library.register_user(user_name)
                else:
                    print("Имя не может быть пустым.")

            case "4":
                library.show_all_users()

            case "5":
                library.show_all_books()

            case "0":
                print("До свидания!")
                break

            case _:
                print("Неверный ввод. Попробуйте снова.")

def user_session(library: LibraryService):
    name = input("Введите ваше имя: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return

    if not library.user_exists(name):
        print(f"Пользователь «{name}» не зарегистрирован. Обратитесь к библиотекарю для регистрации.")
        return

    user = User(name)
    print(f"\nДобро пожаловать, {user.get_role()} «{user.name}»!")

    while True:
        print(user.show_menu())
        choice = input("Ваш выбор: ").strip()

        match choice:
            case "1":
                library.show_available_books()

            case "2":
                library.show_available_books()
                title = input("Название книги для взятия: ").strip()
                if title:
                    library.borrow_book(name, title)

            case "3":
                library.show_user_books(name)
                title = input("Название книги для возврата: ").strip()
                if title:
                    library.return_book(name, title)

            case "4":
                library.show_user_books(name)

            case "0":
                print("До свидания!")
                break

            case _:
                print("Неверный ввод. Попробуйте снова.")


def main():
    print("Система управления библиотекой")

    library = LibraryService()
    library.load_data()

    while True:
        print("\nВыберите роль: \n1. Библиотекарь \n2. Пользователь \n0. Выход")

        role_choice = input("Ваш выбор: ").strip()

        match role_choice:
            case "1":
                librarian_session(library)

            case "2":
                user_session(library)

            case "0":
                library.save_data()
                print("До свидания!")
                break

            case _:
                print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()