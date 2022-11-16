import easygui
import view
import modul_complex
import modul_rational
import data_processing

msg = 'Выберите действие'
title = 'Меню выбора дальнейшего действия'
options = ['Калькулятор', 'Получить лог', 'Выход из программы']
user_choice = easygui.buttonbox(msg, title, options)

if user_choice == options[0]:  ## функция запрашивает у пользователя выражение для решения на калькуляторе, сразу убирает пробел и возвращает переменную как строку
    expression = view.get_numeric_expression()
    check = data_processing.str_check(expression) # функция проводит проверку выражения пользователя на ошибки
    if check:  # если введенное выражение прошло проверку программа выбирает калькулятор комплексных или рациональных чисел
        if 'j' in expression or 'i' in expression:
            result = modul_complex.complex(expression)  # фукнкция производит расчет выражения в калькуляторе комплексных чисел
            view.show_result(expression, result)  # функция выводит результат расчета калькулятора пользователю
        else:
            result = modul_rational.Calcus(expression)  # фукнкция производит расчет выражения в калькуляторе рациональных чисел
            view.show_result(expression, result)  # функция выводит результат расчета калькулятора пользователю
    ## если выражение введено не правильно запускается функция ввода выражения до тех пор пока пользователь не введет без ошибок
    
    
elif user_choice == options[1]: ##  функция открывает пользователю лог. 
    print('log')
#     with open('log.cvs', 'r') as file:   
#         for line in file:
#             print(line)

elif user_choice == options[2]: ## функция вывода на экран ссообщения и выход из программы
    view.exit()
    exit()
    
    
    
## До исправления ===================================================================================

a = input('Выберите команду от 1 до 3 ')

while True:
    if a == '1':  # Вызов калькулятора
        view.get_value()
    elif a == '2':
        continue
        # вызывает Логи
    elif a == '3':
        continue
        # Выход
