def from_sym_ternary(number):
    """
    Функция преобразует строку с числом из
    троичной симметричной системы счисления в десятичную
    Принимает: number: str()
    Возвращает: decimal: int() в десятичной системе
    """
    decimal = 0
    for digit in number:
        if digit == '+':
            decimal = decimal * 3 + 1
        if digit == '-':
            decimal = decimal * 3 - 1
        if digit == '0':
            decimal = decimal * 3
    return decimal


def to_sym_ternary(decimal):
    """
    Функция преобразует десятичное число в
    строку в троичной симметричной системе счисления
    Принимает: decimal: int()
    Возвращает: to_sym_ternary: str() в троичной симметричной системе
    """
    if decimal == 0:
        return '0'
    quaternary = ''
    while decimal > 0:
        r = decimal % 3
        if r == 2:
            r = -1
            decimal += 1
        if r == 1:
            quaternary = '+' + quaternary
        if r == -1:
            quaternary = '-' + quaternary
        if r == 0:
            quaternary = '0' + quaternary
        decimal //= 3
    return quaternary


def add_sym_ternary(num1, num2):
    """Функция выполняет сложение чисел в четверичной системе счисления"""
    decimal_sum = from_sym_ternary(num1) + from_sym_ternary(num2)
    return to_sym_ternary(decimal_sum)


def sub_sym_ternary(num1, num2):
    """Получаем десятичные значения чисел"""
    decimal_num1 = from_sym_ternary(num1)
    decimal_num2 = from_sym_ternary(num2)

    # Вычисляем разность десятичных значений
    decimal_diff = decimal_num1 - decimal_num2

    # Преобразуем разность в четверичную систему с сохранением знака
    if decimal_diff >= 0:
        return to_sym_ternary(decimal_diff)
    else:
        return '-' + to_sym_ternary(abs(decimal_diff))


def is_valid_sym_ternary(n1, n2):
    """Проверка существует ли такое число, которое написал пользователь
    в четверичной системе счисления"""
    v = set('0+-')
    return all(char in v for char in n1) and all(char in v for char in n2)
