def from_quaternary(number):
    """
    Функция преобразует строку с числом из
    четверичной системы счисления в десятичную
    Принимает: number: str()
    Возвращает: decimal: int() в десятичной системе
    """
    decimal = 0
    for digit in number:
        decimal = decimal * 4 + int(digit)
    return decimal


def to_quaternary(decimal):
    """
    Функция преобразует десятичное число в
    строку в четверичной системе счисления
    Принимает: decimal: intstr()
    Возвращает: quaternary: str()  в четверичной системе
    """
    if decimal == 0:
        return '0'
    quaternary = ''
    while decimal > 0:
        quaternary = str(decimal % 4) + quaternary
        decimal //= 4
    return quaternary


def add_quaternary(num1, num2):
    """Функция выполняет сложение чисел в четверичной системе счисления"""
    decimal_sum = from_quaternary(num1) + from_quaternary(num2)
    return to_quaternary(decimal_sum)


def subtract_quaternary(num1, num2):
    """Получаем десятичные значения чисел"""
    decimal_num1 = from_quaternary(num1)
    decimal_num2 = from_quaternary(num2)

    # Вычисляем разность десятичных значений
    decimal_diff = decimal_num1 - decimal_num2

    # Преобразуем разность в четверичную систему с сохранением знака
    if decimal_diff >= 0:
        return to_quaternary(decimal_diff)
    else:
        return '-' + to_quaternary(abs(decimal_diff))


def is_valid_quaternary(n1, n2):
    """Проверка сущетвует ли такое число которое написал пользователь
    в четверичной системе счисления"""
    v = set('0123')
    return all(char in v for char in n1) and all(char in v for char in n2)
