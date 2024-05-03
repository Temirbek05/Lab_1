from insert_from_csv import insert_from_csv
from insert_record import insert_record
from update_record import update_record
from query_with_filter import query_with_filter
from delete_record import delete_record

if __name__ == "__main__":
    while True:
        print("Выберите действие:")
        print("1. Добавить запись из CSV файла")
        print("2. Добавить запись из консоли")
        print("3. Обновить запись")
        print("4. Запросить данные с фильтрами")
        print("5. Удалить запись по имени или номеру телефона")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            file_path = input("Введите путь к CSV файлу: ")
            insert_from_csv(file_path)
        elif choice == "2":
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            insert_record(name, phone_number)
        elif choice == "3":
            name = input("Введите имя пользователя, которого хотите обновить: ")
            new_phone_number = input("Введите новый номер телефона: ")
            update_record(name, new_phone_number)
        elif choice == "4":
            filter_type = input("Выберите тип фильтра (name, phone_number): ")
            filter_value = input(f"Введите значение для фильтра {filter_type}: ")
            query_with_filter(filter_type, filter_value)
        elif choice == "5":
            criteria = input("Введите имя или номер телефона для удаления: ")
            delete_record(criteria)
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор.")
