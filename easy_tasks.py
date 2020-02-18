from math import sqrt
import datetime
import itertools

def arithmetic(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        return "Неизвестная операция"


def is_year_leap(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False


def squaare(a):
    P = a * 4
    S = a*a
    D = sqrt(2)*a
    return P, S, D


def season(month):
    if month < 3 or month == 12:
        return "зима"
    elif month > 2 and month < 6:
        return "весна"
    elif month > 5 and month < 9:
        return "лето"
    elif month > 8 and month < 12:
        return "осень"
    else:
        return "такого месяца нет"


def bank(a, years):
    for num in range(years):
        a = a*1.1
    return a


def is_prime(num):
    if num == 1:
        return False
    d = 2
    while num % d != 0:
        d += 1
    if d == num:
        return True
    else:
        return False


def date(day, month, year):
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True


def XOR_cipher(str, key):
    answer = []
    for s in str:
        answer.append(chr(ord(s) ^ ord(key)))
    return ''.join(answer)

XOR_uncipher = XOR_cipher

print(XOR_uncipher("рќъ", "й"))


