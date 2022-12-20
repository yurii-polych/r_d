# 1. Створити телефонну книгу, яка матиме наступні команди:
#   stats: кількість записів
#   add: додати запис
#   delete <name>: видалити запис за іменем (ключем)
#   list: список всіх імен в книзі
#   show <name>: детальна інформація по імені
# =============================================================

phonebook = {}
while True:
    user_input = input('Enter your command: ')  # stats, add, delete, list or show
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
        case _:
            print('Please enter correct command.')

