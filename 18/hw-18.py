# 1. Створити клас Bot з атрибутом name та методами say_name та send_message.
#    send_message має приймати параметри self і message і має друкувати message.
#    Метод say_name має друкувати значення атрибуту name.
#
# 2. Створити клас TelegramBot, який має бути унаслідуваний від Bot та має містити:
#    власні атрибути url, chat_id (None за замовчуванням)
#    методи send_message, set_url та set_chat_id.
#
#    Ці методи, крім self,  мають приймати 1 параметр (url та chat_id відповідно) та присвоювати значення цього
#    параметру атрибутам url та chat_id відповідно.
#
#    Також TelegramBot має перевизначити метод send_message – друкувати значення параметру message з будь-яким
#    допоміжним текстом. Цей текст також має містити в собі значення url та chat_id
#
#    Результатом має бути:
#
# some_bot = Bot('Marvin')
# some_bot.say_name()
# >> > "Marvin"
#
# some_bot.send_message("Hello")
# >> > "Hello"
#
# telegram_bot = TelegramBot("TG")
# telegram_bot.say_name()
# >> > "TG"
#
# telegram_bot.send_message('Hello')
# >> > "TG bot says Hello to chat None using None"
#
# telegram_bot.set_chat_id(1)
# telegram_bot.send_message('Hello')
# >> > "TG bot says Hello to chat 1 using None"
#
# 3. (необов'язкове виконання) Створити клас MyStr(str), який має перевизначтити метод str таким чином, щоб замість
#    друку реального значення всі літери були переведені в верхній регістр:
#
# my_str = MyStr('test')
# print(my_str)
# >>> "TEST"
#
#
# 4. (необов'язкове виконання) Створити клас User, який в конструкторі має приймати параметр name і ініціалізувати
#    його у відповідний атрибут.
#
#    Перевизначити метод eq таким чином, щоб при порівнянні 2 обʼєктів типу User у який співпадають атрибути name,
#    ми отримали True. При цьому не враховувати регістр, в якому записані кожен із атрибутів.
#
# first_user = User('OLEKSII')
# second_user = User('Oleksii')
# print(first_user == second_user)
# >>> True
#
#
# 5. (необов'язкове виконання) Створити клас Bot та TelegramBot із першого завдання за допомогою функції type
# ==============================================================

# Task 1.
class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


# Task 2. ====================================
class TelegramBot(Bot):
    def __init__(self, name):
        self.url = None
        self.chat_id = None
        super().__init__(name)

    def send_message(self, message):
        print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


# Task 3. ====================================
class MyStr(str):
    def __init__(self, text):
        self.text = text
        super().__init__()

    def __str__(self):
        return self.text.upper()


# Task 4. ====================================
class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        name_lower = self.name.lower()
        return name_lower == other.lower()


# Task 5. ====================================
def init_function(self, name):
    self.name = name


def say_name_function(self):
    print(self.name)


def send_message_function(self, message):
    print(message)


bot_class = type(
    'Bot',
    (),
    {
        '__init__': init_function,
        'say_name': say_name_function,
        'send_message': send_message_function
    }
)


def init_telegram_function(self, name):
    self.url = None
    self.chat_id = None
    self.__class__.__bases__[0].__init__(self, name)


def set_url_function(self, url):
    self.url = url


def set_chat_id_function(self, chat_id):
    self.chat_id = chat_id


def send_message_tg_function(self, message):
    print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')


telegram_bot_class = type(
    'TelegramBot',
    (bot_class,),
    {
        '__init__': init_telegram_function,
        'send_message': send_message_tg_function,
        'set_url': set_url_function,
        'set_chat_id': set_chat_id_function,
    }
)
