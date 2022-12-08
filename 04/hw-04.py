# 1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти — чи є введений текст “числом”
#    чи “словом”.
# 2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
# 3. Якщо це “слово”, програма має вказати його довжину.

common_text = input('Type here your number or word and press "Enter": ')
if common_text.isdigit():
    print('This is a number.')
    get_number = int(common_text)
    if get_number % 2:
        print('The number is odd.')
    else:
        print('The number is even.')
elif common_text.isalpha():
    print('This is a word.')
    common_text_length = len(common_text)
    print(f'Its length is {common_text_length}.')
else:
    print('You should enter only number or word!')