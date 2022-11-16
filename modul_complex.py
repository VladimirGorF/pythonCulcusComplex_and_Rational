# Модуль состоит из 7 функций
# serch_two_elems определяет два элемента которые вычисляться
# creat_list_elements составляет два списка в которых записаны два числа для вычесления
# 4 функции с вычеслениями plus , minus , div , times . В них записаны формулы по которым происходит вычесления
# complex алгоритм выбора последовательности действия

# метод берет выражение и индекс первого действия . На выходе выводит первый элемент , второй элемент
# результат вычисления , индекс начала строки где происходят вычисления и индекс конца строки где проиходят вычисления
def serch_two_elems(data, index_mark):
    # метод разбивает элемент действия на список чисел . Пример 2+2j на выходе будет [2,2,'j']
    def creat_list_elements(elem):
        list_numbers = []
        num = ''
        for i, j in enumerate(elem):
            if j.isdigit() or j == '.':
                num += j
            elif not i:
                num += j
            elif j == '-' or j == '+':
                if num.count('.'):
                    list_numbers.append(float(num))
                    num = ''
                else:
                    list_numbers.append(int(num))
                    num = ''
                    if j == '-':
                        num += '-'
            elif j == 'i' or j == 'j':
                if num.count('.'):
                    list_numbers.append(float(num))
                else:
                    list_numbers.append(int(num))
                list_numbers.append(j)
        return list_numbers

    elem_1 = ''
    elem_2 = ''
    for i in range(index_mark + 2, len(data)):
        if data[i] != ')':
            elem_2 += data[i]
        else:
            index_right = i
            break
    for i in reversed(range(index_mark - 1)):
        if data[i] != '(':
            elem_1 += data[i]
        else:
            index_left = i
            break
    elem_1 = elem_1[::-1]
    data = data[:index_left] + data[index_right + 1:]
    return creat_list_elements(elem_1), creat_list_elements(elem_2), data, index_left, index_right


#


# умножение
def times(list_numbers_1, list_numbers_2):
    # (a + bi) · (c + di) = (ac - bd) + (bc + ad)i
    if list_numbers_1[2] == list_numbers_2[2]:
        result_11 = (list_numbers_1[0] * list_numbers_2[0])
        result_12 = (list_numbers_1[1] * list_numbers_2[1])
        result_1 = result_11 - result_12
        result_2 = (list_numbers_1[1] * list_numbers_2[0]) + (list_numbers_1[0] * list_numbers_2[1])
        if result_2 > 0:
            return f'({str(result_1)}+{str(result_2)}{list_numbers_1[2]})'
        else:
            return f'({str(result_1)}{str(result_2)}{list_numbers_1[2]})'
    else:
        print('неправильная форма комплексного числа')
        return False


# деление
def div(list_numbers_1, list_numbers_2):
    # (a + bi)/(c + di)=(ac + bd)/(c**2 + d**2)+( (bc - ad)/(c**2 + d**2) )i
    if list_numbers_1[2] == list_numbers_2[2]:
        numerator_11 = (list_numbers_1[0] * list_numbers_2[0])
        numerator_12 = (list_numbers_1[1] * list_numbers_2[1])
        numerator_1 = numerator_11 + numerator_12
        denominator = list_numbers_2[0] ** 2 + list_numbers_2[1] ** 2
        number_1 = round(numerator_1 / denominator, 6)

        numerator_21 = list_numbers_1[1] * list_numbers_2[0]
        numerator_22 = list_numbers_1[0] * list_numbers_2[1]
        numerator_2 = numerator_21 - numerator_22
        number_2 = round(numerator_2 / denominator, 6)

        if number_2 > 0:
            return f'({str(number_1)}+{str(number_2)}{list_numbers_1[2]})'
        else:
            return f'({str(number_1)}{str(number_2)}{list_numbers_1[2]})'
    else:
        print('неправильная форма комплексного числа')
        return False


# сложение
def plus(list_numbers_1, list_numbers_2):
    # (a + bi) + (c + di) = (a + c) + (b + d)i
    if list_numbers_1[2] == list_numbers_2[2]:
        number_1 = list_numbers_1[0] + list_numbers_2[0]
        number_2 = list_numbers_1[1] + list_numbers_2[1]
        result = number_1 + number_2
        if int(number_2) > 0:
            return f'({str(number_1)}+{str(number_2)}{list_numbers_1[2]})'
        else:
            return f'({str(number_1)}{str(number_2)}{list_numbers_1[2]})'
    else:
        print('неправильная форма комплексного числа')
        return False


# вычитание
def minus(list_numbers_1, list_numbers_2):
    # (a + bi) - (c + di) = (a - c) + (b - d)i
    if list_numbers_1[2] == list_numbers_2[2]:
        number_1 = list_numbers_1[0] - list_numbers_2[0]
        number_2 = list_numbers_1[1] - list_numbers_2[1]
        result = number_1 + number_2
        if int(number_2) > 0:
            return f'({str(number_1)}+{str(number_2)}{list_numbers_1[2]})'
        else:
            return f'({str(number_1)}{str(number_2)}{list_numbers_1[2]})'
    else:
        print('неправильная форма комплексного числа')
        return False


# алгорит выбора действия
def complex(data):
    while data.count('/') or data.count('*'):
        for i, j in enumerate(data):
            if data[i - 1] == ')':
                if data[i] == '*':
                    list_1, list_2, result_balance, left_index, right_index = serch_two_elems(data, i)
                    result_str = times(list_1, list_2)
                    data = data[:left_index] + result_str + data[right_index + 1:]
                    break
                if data[i] == '/':
                    list_1, list_2, result_balance, left_index, right_index = serch_two_elems(data, i)
                    result_str = div(list_1, list_2)
                    data = data[:left_index] + result_str + data[right_index + 1:]
                    break

    while data.count(')') > 1:
        for i, j in enumerate(data):
            if data[i - 1] == ')':
                if data[i] == '+':
                    list_1, list_2, result_balance, left_index, right_index = serch_two_elems(data, i)
                    result_str = plus(list_1, list_2)
                    data = data[:left_index] + result_str + data[right_index + 1:]
                    break
                if data[i] == '-':
                    list_1, list_2, result_balance, left_index, right_index = serch_two_elems(data, i)
                    result_str = minus(list_1, list_2)
                    data = data[:left_index] + result_str + data[right_index + 1:]
                    break
    return data


print(complex('(-1-2j)+(-2-3j)/(-3-4j)'))
