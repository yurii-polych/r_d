# 1.Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
#   Декоратор має працювати для різних функцій однаково.
#
# 2.Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
#
# 3.Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед виконанням
#   коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.
#
#   У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити
#   своєї роботи.
#
# 4.Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що і менеджер контексту
#   із попереднього завдання.
#
# - Додати обробку помилок до коду із попередніх домашніх завдань (необов'язкове виконання).
# ==========================================================

# Task 1.
import time


def print_name_time_deco(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        call_time = time.strftime("%H:%M:%S", time.localtime())
        result = func(*args, **kwargs)
        print(f'The function {func_name} was called at {call_time}.')
        return result

    return wrapper


# ==========================================================
# Task 2.
class MyCustomException(Exception):
    def __init__(self):
        self.message = 'Custom exception is occurred.'
        super().__init__(self.message)


# ==========================================================
# Task 3.
class MyContextManager:
    def __init__(self):
        print('=' * 10)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('=' * 10)


with MyContextManager() as manager:
    try:
        print('Some code here.')
    except Exception as error:
        print(error)


# ==========================================================
# Task 4.
try:
    print('=' * 10)
    print('Some code here.')
except Exception as error:
    print(error)
    print('=' * 10)
else:
    print('=' * 10)
