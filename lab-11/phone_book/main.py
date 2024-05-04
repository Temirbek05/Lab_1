# from insert_from_csv import insert_from_csv
# from phone_book.insert_or_update_record import insert_record
# from update_record import update_record
# from query_with_filter import query_with_filter
# from delete_record import delete_record
# from find_records import get_all_records

# def find_records_by_pattern(pattern):
#     matching_records = []
#     for record in get_all_records:  # Assuming all_records is a list of dictionaries where each dictionary represents a record
#         if pattern.lower() in record['name'].lower() or pattern.lower() in record['surname'].lower() or pattern in record['phone_number']:
#             matching_records.append(record)
#     return matching_records

# if __name__ == "__main__":
#     while True:
#         print("Выберите действие:")
#         print("1. Добавить запись из CSV файла")
#         print("2. Добавить запись из консоли")
#         print("3. Обновить запись")
#         print("4. Запросить данные с фильтрами")
#         print("5. Удалить запись по имени или номеру телефона")
#         print("6. Поиск записей по паттерну")
#         print("7. Выйти")

#         choice = input("Введите номер действия: ")

#         if choice == "1":
#             file_path = input("Введите путь к CSV файлу: ")
#             insert_from_csv(file_path)
#         elif choice == "2":
#             name = input("Введите имя: ")
#             phone_number = input("Введите номер телефона: ")
#             insert_record(name, phone_number)
#         elif choice == "3":
#             name = input("Введите имя пользователя, которого хотите обновить: ")
#             new_phone_number = input("Введите новый номер телефона: ")
#             update_record(name, new_phone_number)
#         elif choice == "4":
#             filter_type = input("Выберите тип фильтра (name, phone_number): ")
#             filter_value = input(f"Введите значение для фильтра {filter_type}: ")
#             query_with_filter(filter_type, filter_value)
#         elif choice == "5":
#             criteria = input("Введите имя или номер телефона для удаления: ")
#             delete_record(criteria)
#         elif choice == "6":
#             pattern = input("Введите паттерн для поиска: ")
#             matching_records = find_records_by_pattern(pattern)
#             if matching_records:
#                 print("Найдены следующие записи:")
#                 for record in matching_records:
#                     print(f"Имя: {record['name']}, Номер телефона: {record['phone_number']}")
#             else:
#                 print("Нет записей, соответствующих заданному паттерну.")
#         elif choice == "7":
#             print("Программа завершена.")
#             break
#         else:
#             print("Некорректный выбор.")

from insert_from_csv import insert_from_csv
from insert_or_update_record import insert_or_update_record
from update_record import update_record
from query_with_filter import query_with_filter
from delete_record import delete_record
from find_records import get_all_records, find_records_by_pattern

def find_records_by_pattern(all_records, pattern, search_type):
    matching_records = []
    for record in all_records:
        name, surname, phone_number = record[1], record[2], record[3]
        if search_type == "name" and pattern.lower() in name.lower():
            matching_records.append(record)
        elif search_type == "surname" and pattern.lower() in surname.lower():
            matching_records.append(record)
    return matching_records

if __name__ == "__main__":
    while True:
        print("Choose an action:")
        print("1. Add record from CSV file")
        print("2. Add record from console")
        print("3. Update record")
        print("4. Query data with filters")
        print("5. Delete record by name/surname or phone number")
        print("6. Search records by pattern (name/surname)")
        print("7. Exit")

        choice = input("Enter the action number: ")

        if choice == "1":
            file_path = input("Enter the path to the CSV file: ")
            insert_from_csv(file_path)
        elif choice == "2":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            phone_number = input("Enter phone number: ")
            insert_or_update_record(name, surname, phone_number)
        elif choice == "3":
            name = input("Enter the user's name you want to update: ")
            surname = input("Enter the user's surname you want to update: ")
            new_phone_number = input("Enter the new phone number: ")
            update_record(name, surname, new_phone_number)
        elif choice == "4":
            filter_type = input("Choose the filter type (name, surname, phone_number): ")
            filter_value = input(f"Enter value for the filter {filter_type}: ")
            query_with_filter(filter_type, filter_value)
        elif choice == "5":
            choice = input("Choose criteria for deletion (name_surname/phone_number): ")
            if choice == "name_surname":
                name = input("Enter the name: ")
                surname = input("Enter the surname: ")
                delete_record(name=name, surname=surname)
            elif choice == "phone_number":
                phone_number = input("Enter the phone number for deletion: ")
                delete_record(phone_number=phone_number)
            else:
                print("Invalid choice.")
        elif choice == "6":
            all_records = get_all_records()
            search_type = input("Do you want to search by name or surname? ")
            pattern = input(f"Enter the pattern to search for {search_type}: ")
            matching_records = find_records_by_pattern(all_records, pattern, search_type)
            if matching_records:
                print("Matching records found:")
                for record in matching_records:
                    print(f"Name: {record[1]}, Surname: {record[2]}, Phone number: {record[3]}")
            else:
                print("No records matching the pattern.")
        elif choice == "7":
            print("Program exited.")
            break
        else:
            print("Invalid choice.")
