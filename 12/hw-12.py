# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
#
#    Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
#    При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
#    Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string
#    (при записі в файл) і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної
#    операції add або delete.
#
# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
#
# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.


import time
import json


# Task 1. ===================
try:
    with open('phonebook_data.json', 'r') as contacts:
        phonebook = json.load(contacts)
except FileNotFoundError:
    phonebook = {}
    with open('phonebook_data.json', 'x') as contacts:
        json.dump(phonebook, contacts)

while True:
    user_input = input('Enter your command: ')  # Available commands: stats, add, delete, list, show or exit.
    match user_input:
        case 'stats':
            print(f'Total amount of numbers: {len(phonebook)}')
        case 'add':
            contact = input('Enter name and phone number: ').split()
            name_add = contact[0]
            phone_number = contact[1]
            if name_add not in phonebook:
                phonebook[name_add] = phone_number
            else:
                print("It's not allowed to rewrite a contact.")
        case 'delete':
            name_del = input('Enter the name you want to delete: ')
            if phonebook.get(name_del):
                del phonebook[name_del]
            else:
                print('This contact does not exists.')
        case 'list':
            print(list(phonebook.keys()))
        case 'show':
            name_show = input('Enter the name you want to see: ')
            if phonebook.get(name_show):
                print(f'Name: {name_show}. Phone number: {phonebook[name_show]}.')
            else:
                print('This contact does not exists.')
        case 'exit':
            with open('phonebook_data.json', 'w') as contacts:
                json.dump(phonebook, contacts)
            break
        case _:
            print('Please enter correct command.')


# Task 2. ===================
def write_name_print_time_deco(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        call_time = time.strftime("%H:%M:%S", time.localtime())
        result = func(*args, **kwargs)
        print(f'The function {func_name} was called at {call_time}.')

        try:
            with open('err_log.txt', 'x') as file:
                file.write(f'The function\'s name is {func_name}.')
        except FileExistsError:
            with open('err_log.txt', 'w') as file:
                file.write(f'The function\'s name is {func_name}.')

        return result

    return wrapper


# Task 3. ===================
class MyCustomException(Exception):
    def __init__(self):
        self.message = 'Custom exception was occurred'
        self.call_time = time.strftime("%H:%M:%S", time.localtime())
        super().__init__(self.message)

        try:
            with open('mce_log.txt', 'x') as file:
                file.write(f'{self.message} at {self.call_time}.')
        except FileExistsError:
            with open('mce_log.txt', 'w') as file:
                file.write(f'{self.message} at {self.call_time}.')
