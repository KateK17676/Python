"""Поменять queternary на ternary_sym"""


def from_quaternary(number):
    """
    Функция преобразует строку с числом из
    троичной симметричной систнмы счисления в десятичную
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


def to_quaternary(decimal):
    """
    Функция преобразует десятичное число в
    строку в троичной симметричной системе счисления
    Принимает: decimal: intstr()
    Возвращает: quaternary: str()  в троичной симметричной системе
    """
    if decimal == 0:
        return '0'
    quaternary = ''
    n = 0
    k = 0
    if decimal > 0:
        while decimal > n:
            n += 3**k
        quaternary = '+'
        sum = 3**k
        for i in range(k-1, 0):
            if sum + 3**i <= decimal:
                sum += 3**i
                quaternary = quaternary + '+'
            elif sum - 3**i >= decimal:
                sum -= 3 ** i
                quaternary = quaternary + '-'
            else:
                quaternary = quaternary + '0'
        return quaternary
    if decemial < 0:


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
