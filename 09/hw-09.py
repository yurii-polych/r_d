# 1. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі,
#    використовуючи генератори.
#
# 2. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі,
#    використовуючи ітератори (необов'язкове виконання).
#
# 3. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі,
#    використовуючи рекурсію (необов'язкове виконання).
#
# 4. Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію (необов'язкове виконання).
# ===============================================================

# Task 1.
def get_number_by_index_from_fibonacci_sequence(index):
    a, b = 0, 1
    for _ in range(index + 1):
        yield a
        a, b = b, a + b


number = int(input('Enter your number: '))
result = list(get_number_by_index_from_fibonacci_sequence(number))[number]
print(f'You got number {result} from Fibonacci sequence.')

# Task 2.
class MyFibonacci:
    value = 0

    def __init__(self, num):
        self.num = num
        self.first_element = 0
        self.second_element = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.num + 1:
            raise StopIteration()
        if self.value == 0:
            self.value += 1
            return self.first_element
        if self.value == 1:
            self.value += 1
            return self.second_element

        next_element = self.first_element + self.second_element
        self.first_element, self.second_element = self.second_element, next_element
        self.value += 1
        return next_element


number = int(input('Enter your number: '))
my_iterator_object = MyFibonacci(number)
print(list(my_iterator_object)[-1])

# Task 3.
def get_fibonacci_using_recursion(index):
    if index <= 1:
        return index
    else:
        return get_fibonacci_using_recursion(index - 1) + get_fibonacci_using_recursion(index - 2)


number = int(input('Enter your number: '))
result = get_fibonacci_using_recursion(number)
print(f'You got number {result} from Fibonacci sequence.')

# Task 4.
def get_factorial_using_recursion(number):
    if number == 0:
        return 1
    return number * (get_factorial_using_recursion(number - 1))
