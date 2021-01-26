import math
import string
import random
import re
import datetime

def generate_password(length: int) -> str:
    """
    generate password with given length
    Homework
    функция должна возвращать строку из случайных символов заданной длины.
    """
    alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase +string.punctuation
    return str("".join(["".join(random.choice(alphabet)) for _ in range(length)]))
print('01. Gen_pass:', generate_password(50))

def encrypt_message(message: str) -> str:
    """
    encrypt message
    зашифровать сообщение по алгоритму.
    Сместить каждый символ по ASCII таблице на заданное рассояние.
    """
    key = 2
    return ''.join(
        chr(num + key)
        for num in map(ord, message)
    )
print('02. Encrypt_m:',encrypt_message('Hello'))

def lucky_number(ticket: str) -> bool:
    """
    lucky number (tram ticket)
    667766 - is lucky (6 + 6 + 7 == 7 + 6 + 6)
    сумма первых трех числе должна равняться сумме последних трех чисел
    """
    total1 = 0
    total2 = 0
    part_1 = ticket[:3]
    part_2 = ticket[3:]
    for _ in range(0, len(part_1)):
        total1 = total1 + int(part_1[_])
    for _ in range(0, len(part_2)):
        total2 = total2 + int(part_2[_])
    return True if total1 == total2 else False

print('03. lucky_number:', lucky_number('113321'))


def fizz_buzz(num: int) -> str:
    """
    fizz buzz
    усли число, кратно трем, программа должна выводить слово «Fizz»,
    а вместо чисел, кратных пяти — слово «Buzz».
    Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
    в остальных случаях число как строку
    """
    if (num % 3 == 0 and num % 5 == 0):
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)
print('04. Fizz_buzz:',fizz_buzz(10))

def password_is_strong(password) -> bool:
    """
    is password is strong
    (has number, char, lowercase, uppercase, at least length is 10)
    вернуть True если пароль надежный
    Праметры:
        1. Пароль должен содержать как минимум одну цифру
        2. Пароль должен содержать как минимум один сивол в нижнем регистре
        3. Пароль должен содержать как минимум один сивол в верхнем регистре
        4. Пароль должен быть как минимум 10 символов
    """
    pw = password
    len_pass = True if len(pw) > 10 else None
    result = [re.search('[a-z]', pw),
              re.search('[A-Z]', pw),
              re.search('[0-9]', pw),
              re.search('[\W]', pw),
              len_pass]
    if all(result):
        return 'Pass is Strong'
    return ("Пароль не надежный! : "+
            "добавь маленькие буквы, "*(result[0] is None) +
            "добавь большие буквы, "*(result[1] is None) +
            "добавь цифры, "*(result[2] is None) +
            "добавь спец. символы, "*(result[3] is None) +
            "увелич длины, "*(result[4] is None) +
             "после чего, попробуйте еще!")
print('05. PW_is_Strong:', password_is_strong('qwe!Q3'))



def number_is_prime(num: int) -> bool:
    """
    number is prime
    на вход принимаем число
    вернуть True если число является простым
    https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE#:~:text=2%2C%203%2C%205%2C%207,%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%B1%D1%8B%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D0%BC%20%D0%BD%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D1%82%D0%BE%D0%B9.
    """
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num

print('06. Prime num: ', number_is_prime(47))

def decrypt_message(message: str) -> str:
    """
    decrypt message
    функция обратная encrypt_message
    Расшифровать сообщение по заданному ключу
    """
    key = 2
    return ''.join(
        chr(num - key)
        for num in map(ord, message)
    )

print('07. Decryp_message:', decrypt_message('Jgnnq'))

def volume_of_sphere(radius: float) -> str:
    """
    Volume of a Sphere
    на вход принимаем радиус сферы.
    Необходимо рассчитать объем сферы и округлить результат до двух знаков после точки
    round to 2 places
    """
    r = radius
    pi = math.pi
    result = (4 / 3) * pi * r ** 3

    return f"V сферы, с r={r} Будет = {result:.{2}f}"

print('08. V-sphere:',volume_of_sphere(10))

def days_diff(start_date: ..., end_date: ...) -> int:
    """
    calculate number of days between two dates.
    найти разницу между двумя датами
    """
    return 0

print('09 Days:')

def prs(client_choice: str) -> bool:
    """
    paper rock scissors
    принимаем значение от клиента из списка значений (например ['p', 'r', 's'])
    сгенерировать случайный выбор на сервере
    реализовать игру в камень-ножницы-бумага между клиент-сервер
    """
    chosen = random.randint(1,3)
    if chosen == 1:
        computer = 'Камень'
        # computer = 'S'
    elif chosen == 2:
        computer = 'Ножницы'
        # computer = 'K'
    else:
        computer = 'Бумага'
        # computer = 'P'

    if client_choice == computer:
        result_return = 'Ничья!'
    elif client_choice == 'Камень' and computer == 'Ножницы':
        result_return = 'Вы Выиграли!'
    elif client_choice == 'Камень' and computer == 'Бумага':
        result_return = 'Вы проиграли!'
    elif client_choice == 'Ножницы' and computer == 'Бумага':
        result_return = 'Вы Выиграли!'
    elif client_choice == 'Ножницы' and computer == 'Камень':
        result_return = 'Вы проиграли!'
    elif client_choice == 'Бумага' and computer == 'Камень':
        result_return = 'Вы выиграли!'
    elif client_choice == 'Бумага' and computer == 'Ножницы':
        result_return = 'Вы проиграли!'
    else:
        return 'Выберите правельный вариант\n' \
               '(S)Камень\n' \
               '(K)Ножницы\n' \
               '(P)Бумага\n'

    return f'{result_return} \n' \
           f'Игрок: {client_choice}\n' \
           f'       VS\n' \
           f'Компьютер: {computer}'
print('10. КНБ:',prs('Камень'))


def integer_as_roman(integer: int) -> str:
    """
    ***
    integer to Roman Number
    вывести значение в виде римского числа
    """
    return ''
print('11. Roman Num:')
#
# if name == 'main':
#     assert encrypt_message('Dima') == 'Fkoc'
