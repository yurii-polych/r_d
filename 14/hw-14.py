# 1. До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx.
#    Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX
#
# 2. (необов'язкове виконання) Написати програму, яка буде:
#    -зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
#    -знаходити всі email в тексті і змінювати їх на *@*.
#
# 3. (необов'язкове виконання) Написати програму, яка буде:
#   -зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
#   -знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери
#    справжньої адреси, а весь інший текст має бути замінений на *. Кількість * необовʼязково має відповідати кількості
#    замінених символів
# ======================================

import json
from re import fullmatch, sub


# =============== Task 1. ===============
def validate_phonenumber(phonenumber):
    return fullmatch(r'(\+?380|0)\d{9}$', phonenumber)


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
            if name_add not in phonebook and validate_phonenumber(phone_number):
                phonebook[name_add] = phone_number
            else:
                print("It's not allowed to rewrite a contact.")
        case 'delete':
            name_del = input('Enter the name you want to delete: ')
            if phonebook.get(name_del):
                del phonebook[name_del]
            else:
                print('This contact does not exist.')
        case 'list':
            print(list(phonebook.keys()))
        case 'show':
            name_show = input('Enter the name you want to see: ')
            if phonebook.get(name_show):
                print(f'Name: {name_show}. Phone number: {phonebook[name_show]}.')
            else:
                print('This contact does not exist.')
        case 'exit':
            with open('phonebook_data.json', 'w') as contacts:
                json.dump(phonebook, contacts)
            break
        case _:
            print('Please enter correct command.')


# =============== Task 2. ===============
def change_email():
    file_name = input('Enter file name: ')
    replaced_email = '*@*'
    pattern = r'[\w\-\.]+@[a-zA-Z]+[\.a-z]+'
    with open(file_name, 'r') as file:
        content = file.read()
        result = sub(pattern, replaced_email, content)
        print(result)


try:
    change_email()
except FileNotFoundError as error:
    print(error)


# =============== Task 3. ===============
def change_email_3():
    file_name = input('Enter file name: ')
    replaced_email = r'\g<start>***@***\g<end>'
    pattern_ua = r'(?P<start>\w)[\w\-\.]+@[a-zA-Z]+\.com\.u(?P<end>[a])'
    pattern_com = r'(?P<start>\w)[\w\-\.]+@[a-zA-Z]+\.co(?P<end>m)'
    with open(file_name, 'r') as file:
        content = file.read()
        result_ua = sub(pattern_ua, replaced_email, content)
        result = sub(pattern_com, replaced_email, result_ua)
        print(result)


try:
    change_email_3()
except FileNotFoundError as error:
    print(error)
