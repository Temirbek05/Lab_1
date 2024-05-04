# import psycopg2
# from config import load_config

# def get_all_records():
#     config = load_config()
#     all_records = []
#     try:
#         with psycopg2.connect(**config) as connect:
#             with connect.cursor() as cursor:
#                 cursor.execute("SELECT * FROM updated_phone_book")
#                 all_records = cursor.fetchall()
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)
#     return all_records

# def find_records_by_pattern(all_records, pattern):
#     matching_records = []
#     for record in all_records:
#         if pattern.lower() in record['name'].lower() or pattern.lower() in record['surname'].lower() or pattern in record['phone_number']:
#             matching_records.append(record)
#     return matching_records

# if __name__ == "__main__":
#     all_records = get_all_records()
#     # Now you can use all_records in your main logic, for example:
#     pattern = input("Enter the search pattern: ")
#     matching_records = find_records_by_pattern(all_records, pattern)
#     print("Matching records:", matching_records)


import psycopg2
from config import load_config

def get_all_records():
    config = load_config()
    all_records = []
    try:
        with psycopg2.connect(**config) as connect:
            with connect.cursor() as cursor:
                cursor.execute("SELECT * FROM updated_phone_book")
                all_records = cursor.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching records:", error)
    return all_records

def find_records_by_pattern(all_records, pattern):
    matching_records = []
    for record in all_records:
        name, surname, phone_number = record[1], record[2], record[3]
        if pattern.lower() in name.lower() or pattern.lower() in surname.lower() or pattern in phone_number:
            matching_records.append(record)
    return matching_records

if __name__ == "__main__":
    all_records = get_all_records()
    pattern = input("Enter the search pattern: ")
    matching_records = find_records_by_pattern(all_records, pattern)
    print("Matching records:", matching_records)
