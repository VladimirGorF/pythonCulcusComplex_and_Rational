import re


def Calculator(s):
    i = 0
    while i < len(s):  # цикл для умножения и деления
        if s[i] == '*':
            if s[i + 1] == '(':
                newS = []
                memoryI = i - 1
                i += 2
                while s[i] != ')':
                    newS.append(s[i])
                    i += 1
                if s[memoryI - 1] == '-':
                    s[memoryI] = - s[memoryI] * Calculator(newS)
                    s.remove(s[memoryI - 1])
                else:
                    s[memoryI] = s[memoryI] * Calculator(newS)
                i = memoryI + 1
                while s[i] != ')':  # удаление скобкового элемента со знаком перед ним
                    s.remove(s[i])
                s.remove(s[i])
            else:
                s[i - 1] = s[i - 1] * s[i + 1]
                s.remove(s[i])
                s.remove(s[i])
                i -= 1
        elif s[i] == '/':  # деление
            if s[i + 1] == '(':
                newS = []
                memoryI = i - 1
                i += 2
                while s[i] != ')':
                    newS.append(s[i])
                    i += 1
                if s[memoryI - 1] == '-':
                    s[memoryI] = - s[memoryI] // Calculator(newS)
                    s.remove(s[memoryI - 1])
                else:
                    s[memoryI] = s[memoryI] // Calculator(newS)
                i = memoryI + 1
                while s[i] != ')':  # удаление скобкового элемента со знаком перед ним
                    s.remove(s[i])
                s.remove(s[i])
            else:
                s[i - 1] = s[i - 1] // s[i + 1]
                s.remove(s[i])
                s.remove(s[i])
                i -= 1
        i += 1
    i = 0

    while i < len(s):  # меняем знаки на противоположные в скобках если знак перед ней отрицательный
        if s[i] == '(' and s[i - 1] == '-':
            while s[i] != ')':
                if s[i] == '-':
                    s[i] = '+'
                else:
                    if type(s[i]) == int and s[i - 1] == '(':
                        s[i] = -(s[i])
                i += 1
        i += 1
    i = 0

    while i < len(s):  # присвоим числам знаки
        if s[i] == '-' and type(s[i + 1]) == int:
            s[i + 1] = - (s[i + 1])
            s.remove(s[i])
            i -= 1
        i += 1
    res = 0

    for i in range(len(s)):  # вычисляем сумму элементов списка
        if type(s[i]) == int:
            res += s[i]
    return res


def Calcus(s):
    s = re.split('', s)  # разбираем все на элементы массива
    i = 0
    while i < len(s):  # цикл для обработки цифр в строке, чтобы те что рядом воспринмались, как одно число
        if s[i].isdigit() and s[i - 1].isdigit():
            s[i - 1] = int(s[i - 1]) * 10 + int(s[i])
            s[i - 1] = str(s[i - 1])
            s.remove(s[i])
            i -= 1
        i += 1

    for i in range(len(s)):  # переводим цифры в цифры
        if s[i].isdigit():
            s[i] = int(s[i])

    i = 0
    while i < len(s):     # цикл для умножения и деления
        if s[i] == '*':
            if s[i + 1] == '(':
                newS = []
                memoryI = i - 1
                i += 2
                while s[i] != ')':
                    newS.append(s[i])
                    i += 1
                if s[memoryI - 1] == '-':
                    s[memoryI] = - s[memoryI] * Calculator(newS)
                    s.remove(s[memoryI - 1])
                else:
                    s[memoryI] = s[memoryI] * Calculator(newS)
                i = memoryI + 1
                while s[i] != ')':  # удаление скобкового элемента со знаком перед ним
                    s.remove(s[i])
                s.remove(s[i])
            else:
                s[i - 1] = s[i - 1] * s[i + 1]
                s.remove(s[i])
                s.remove(s[i])
                i -= 1
        elif s[i] == '/':    # деление
            if s[i + 1] == '(':
                newS = []
                memoryI = i - 1
                i += 2
                while s[i] != ')':
                    newS.append(s[i])
                    i += 1

                if s[memoryI - 1] == '-':
                    s[memoryI] = - s[memoryI] // Calculator(newS)
                    s.remove(s[memoryI - 1])
                else:
                    s[memoryI] = s[memoryI] // Calculator(newS)
                i = memoryI + 1
                while s[i] != ')':    # удаление скобкового элемента со знаком перед ним
                    s.remove(s[i])
                s.remove(s[i])
            else:
                s[i - 1] = s[i - 1] // s[i + 1]
                s.remove(s[i])
                s.remove(s[i])
                i -= 1
        i += 1
    i = 0

    while i < len(s):  # меняем знаки на противоположные в скобках если знак перед ней отрицательный
        if s[i] == '(' and s[i - 1] == '-':
            while s[i] != ')':
                if s[i] == '-':
                    s[i] = '+'
                else:
                    if type(s[i]) == int and s[i - 1] == '(':
                        s[i] = -(s[i])
                i += 1
        i += 1
    i = 0

    while i < len(s):      # присвоим числам знаки
        if s[i] == '-' and type(s[i + 1]) == int:
            s[i + 1] = - (s[i + 1])
            s.remove(s[i])
            i -= 1
        i += 1
    res = 0

    for i in range(len(s)):   # вычисляем сумму элементов списка
        if type(s[i]) == int:
            res += s[i]
    return res



