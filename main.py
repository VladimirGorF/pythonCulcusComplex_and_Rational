import easygui
import view
import modul_complex
import modul_rational
import data_processing
import logging

data = 'Выполнен вход'
logging.common_logger(data)

while True:

    msg = 'Выберите действие'
    title = 'Меню выбора дальнейшего действия'
    options = ['Калькулятор', 'Получить лог расчетов', 'Просмотр истории', 'Выход из программы']
    user_choice = easygui.buttonbox(msg, title, options)

    if user_choice == options[0]:  ## функция запрашивает у пользователя выражение для решения на калькуляторе, сразу убирает пробел и возвращает переменную как строку
        expression = view.get_numeric_expression()
        check = data_processing.str_check(expression) # функция проводит проверку выражения пользователя на ошибки
        while not check:
            expression = view.show_expression_error()
            check = data_processing.str_check(expression)
        if check:  
            if 'j' in expression or 'i' in expression:
                result = modul_complex.complex(expression)  # фукнкция производит расчет выражения в калькуляторе комплексных чисел
                logging.calcus_logger(result)
                view.show_result(expression, result)  # функция выводит результат расчета калькулятора пользователю
            else:
                result = modul_rational.Calcus(expression)  # фукнкция производит расчет выражения в калькуляторе рациональных чисел
                logging.calcus_logger(result)
                view.show_result(expression, result)  # функция выводит результат расчета калькулятора пользователю
                
    elif user_choice == options[1]:  ##  функция открывает пользователю лог.
            view.show_calc_log()

    elif user_choice == options[2]:  ##  функция открывает пользователю лог.
            view.show_general_log()        


    elif user_choice == options[3]: ## функция вывода на экран ссообщения и выход из программы
        view.exit()
        data = 'Выход из программы'
        logging.common_logger(data)
        exit()
    
