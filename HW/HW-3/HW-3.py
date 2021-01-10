import math
import string
import random
import re
from datetime import datetime

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
    for _ in ticket[:3]:
        total1 += int(_)
    for _ in ticket[3:]:
        total2 += int(_)
    return total1 == total2

print('03. lucky_number:', lucky_number('123322'))


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
        return 'Пароль нормальный'
    return ("Пароль не надежный! : "+
            "добавь маленькие буквы, "*(result[0] is None) +
            "добавь большие буквы, "*(result[1] is None) +
            "добавь цифры, "*(result[2] is None) +
            "добавь спец. символы, "*(result[3] is None) +
            "увелич длину, "*(result[4] is None) +
             "после чего, попробуйте еще!")

# в задании возврат boll, если очень критично перепешу

print('05. PW_is_Strong:', password_is_strong('qw;112e!Q3'))



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

def volume_of_sphere(radius: float) -> float:
    """
    Volume of a Sphere
    на вход принимаем радиус сферы.
    Необходимо рассчитать объем сферы и округлить результат до двух знаков после точки
    round to 2 places
    """
    r = radius
    pi = math.pi
    result = (4 / 3) * pi * r ** 3
    return float('%.2f' % result)
    # return f"V сферы, с r={r} Будет = {result:.{2}f}

print('08. V-sphere:',volume_of_sphere(10))

def days_diff(start_date: str, end_date: str) -> int:
    """
    calculate number of days between two dates.
    найти разницу между двумя датами
    """
    format_mask = "%d-%m-%Y"
    sdt = datetime.strptime(start_date, format_mask)
    edt = datetime.strptime(end_date, format_mask)
    return (edt - sdt).days

sdt = '01-01-2020'
edt = '1-01-2021'
print('09 Days:', days_diff(sdt, edt))

def prs(client_choice: str) -> bool:
    """
    paper rock scissors
    принимаем значение от клиента из списка значений (например ['p', 'r', 's'])
    сгенерировать случайный выбор на сервере
    реализовать игру в камень-ножницы-бумага между клиент-сервер
    """

    chosen = random.randint(1, 3)
    if chosen == 1:
        computer = 1 #'Камень'
    elif chosen == 2:
        computer = 2 #'Ножницы'
    else:
        computer = 3 #'Бумага'

    if client_choice == computer:
        result_return = 'Ничья!'
    elif client_choice == 1 and computer == 2:
        result_return = 'Вы Выиграли!'
    elif client_choice == 1 and computer == 3:
        result_return = 'Вы проиграли!'
    elif client_choice == 2 and computer == 3:
        result_return = 'Вы Выиграли!'
    elif client_choice == 2 and computer == 1:
        result_return = 'Вы проиграли!'
    elif client_choice == 3 and computer == 1:
        result_return = 'Вы выиграли!'
    elif client_choice == 3 and computer == 2:
        result_return = 'Вы проиграли!'
    else:
        return 'Выберите правельный вариант\n' \
               '(1)Камень\n' \
               '(2)Ножницы\n' \
               '(3)Бумага\n'

    return result_return

    # chosen = random.randint(1, 3)
    # if chosen == 1:
    #     computer = 'Камень'
    # elif chosen == 2:
    #     computer = 'Ножницы'
    # else:
    #     computer = 'Бумага'
    #
    # if client_choice == computer:
    #     result_return = 'Ничья!'
    # elif client_choice == 'Камень' and computer == 'Ножницы':
    #     result_return = 'Вы Выиграли!'
    # elif client_choice == 'Камень' and computer == 'Бумага':
    #     result_return = 'Вы проиграли!'
    # elif client_choice == 'Ножницы' and computer == 'Бумага':
    #     result_return = 'Вы Выиграли!'
    # elif client_choice == 'Ножницы' and computer == 'Камень':
    #     result_return = 'Вы проиграли!'
    # elif client_choice == 'Бумага' and computer == 'Камень':
    #     result_return = 'Вы выиграли!'
    # elif client_choice == 'Бумага' and computer == 'Ножницы':
    #     result_return = 'Вы проиграли!'
    # else:
    #     return 'Выберите правельный вариант\n' \
    #            '(S)Камень\n' \
    #            '(K)Ножницы\n' \
    #            '(P)Бумага\n'
    #
    # return f'{result_return} \n' \
    #        f'Игрок: {client_choice}\n' \
    #        f'       VS\n' \
    #        f'Компьютер: {computer}'



# здесть тоже на выходе bool если нужно перепишу,
# и как определить True or False если результат ничья?
print('10. КНБ:', prs(2))


def integer_as_roman(integer: int) -> str:
    """
    ***
    integer to Roman Number
    вывести значение в виде римского числа
    """
    i = integer
    i = "I" * i

    i = i.replace("I" * 5, "V") # 5
    i = i.replace("V" * 2, "X") # 10
    i = i.replace("X" * 5, "L") # 50
    i = i.replace("L" * 2, "C") # 100
    i = i.replace("C" * 5, "D") # 500
    i = i.replace("D" * 2, "M") # 1000

    i = i.replace("DCCCC", "CM") #900
    i = i.replace("CCCC", "CD") #400
    i = i.replace("LXXXX", "XC") #80
    i = i.replace("XXXX", "XL") #40
    i = i.replace("VIIII", "IX") #9
    i = i.replace("IIII", "IV") #4

    return i
print('11. Roman Num:', integer_as_roman(874))

if __name__ == '__main__':
    assert type(generate_password(1)) == str
    assert len(generate_password(2)) == 2
    assert len(generate_password(7)) == 7
    assert len(generate_password(50)) == 50

    assert type(encrypt_message('String')) == str
    assert encrypt_message('Hello') == 'Jgnnq'
    assert encrypt_message('World') == 'Yqtnf'
    assert encrypt_message('Smile') == 'Uokng'
    assert encrypt_message('Life') == 'Nkhg'
    assert encrypt_message('Book') == 'Dqqm'

    assert type(lucky_number("123456")) == bool
    assert lucky_number("123321") == True
    assert lucky_number("494980") == True
    assert lucky_number("345544") == False
    assert lucky_number("234264") == False

    assert type(fizz_buzz(13)) == str
    assert fizz_buzz(13) == '13'
    assert fizz_buzz(25) == 'Buzz'
    assert fizz_buzz(33) == 'Fizz'
    assert fizz_buzz(15) == 'FizzBuzz'

    assert number_is_prime(97) == True
    assert number_is_prime(89) == True
    assert number_is_prime(83) == True
    assert number_is_prime(36) == False
    assert number_is_prime(55) == False

    assert type(decrypt_message('dfhgs')) == str
    assert decrypt_message('Jgnnq') == 'Hello'
    assert decrypt_message('Yqtnf') == 'World'
    assert decrypt_message('Uokng') == 'Smile'
    assert decrypt_message('Nkhg') == 'Life'
    assert decrypt_message('Dqqm') == 'Book'

    assert volume_of_sphere(10) == 4188.79
    assert volume_of_sphere(12) == 7238.23
    assert volume_of_sphere(3) == 113.1
    assert volume_of_sphere(2.45) == 61.6
    assert volume_of_sphere(1.13) == 6.04

    assert days_diff('01-02-2009', '01-02-2010') == 365
    assert days_diff('1-2-2009', '01-02-2010') == 365
    assert days_diff('02-04-2009', '11-01-2021') == 4302
    assert days_diff('01-01-2020', '01-01-2021') == 366
    assert days_diff('02-04-2009', '02-04-2009') == 0

    assert integer_as_roman(1) == 'I'
    assert integer_as_roman(1986) == 'MCMLXXXVI'
    assert integer_as_roman(99) == 'XCIX'
    assert integer_as_roman(564) == 'DLXIV'
    assert integer_as_roman(333) == 'CCCXXXIII'


