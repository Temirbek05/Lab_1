# import psycopg2
# from config import load_config

# def delete_record(criteria):
#     config = load_config()
#     if choice == "name":
#         command = "DELETE FROM phone_book WHERE name = %s AND phone_number = %s"
#         data = (criteria, criteria)
#     elif choice == "surname":
#         command = "DELETE FROM phone_book WHERE surname = %s AND phone_number = %s"
#         data = (criteria, criteria)
#     else:
#         print("Invalid choice.")
#         return

#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute(command, data)
#                 connect.commit()  # Commit the transaction
#                 print("Запись успешно удалена из базы данных.")
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == "__main__":
#     choice = input("Выберите параметры для удаления (name/surname): ").lower()
#     criteria = input(f"Введите {'имя' if choice == 'name' else 'фамилию'} для удаления: ")
#     phone_number = input("Введите номер телефона для удаления: ")
#     delete_record(criteria)

import psycopg2
from config import load_config

def delete_record(name=None, surname=None, phone_number=None):
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                if name and surname:
                    # Delete by name and surname
                    cursor.execute("DELETE FROM updated_phone_book WHERE name = %s AND surname = %s", (name, surname))
                elif phone_number:
                    # Delete by phone number
                    cursor.execute("DELETE FROM updated_phone_book WHERE phone_number = %s", (phone_number,))
                else:
                    print("No valid criteria provided for deletion.")
                    return
                
                connect.commit()
                print("Record successfully deleted from the database.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)

if __name__ == "__main__":
    # Get user input for deletion criteria
    choice = input("Choose parameters for deletion (name_surname/phone_number): ").strip()
    
    if choice == "name_surname":
        name = input("Enter the user's name: ").strip()
        surname = input("Enter the user's surname: ").strip()
        delete_record(name=name, surname=surname)
    elif choice == "phone_number":
        phone_number = input("Enter the phone number for deletion: ").strip()
        delete_record(phone_number=phone_number)
    else:
        print("Invalid choice.")
