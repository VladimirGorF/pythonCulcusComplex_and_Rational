import easygui
import view

msg = 'Выберите действие'
title = 'Меню выбора дальнейшего действия'
options = ['Калькулятор', 'Получить лог', 'Выход из программы']
user_choice = easygui.buttonbox(msg, title, options)

if user_choice == options[0]:  ## функция запрашивает у пользователя выражение для решения на калькуляторе, сразу убирает пробел и возвращает переменную как строку
    example_expression = view.get_numeric_expression()
    print(example_expression)
elif user_choice == options[1]: ##  функция открывает пользователю лог. Не готово
    print('log')
#     with open('log.cvs', 'r') as file:   
#         for line in file:
#             print(line)
elif user_choice == options[2]: ## функция вывода на экран ссообщения и выход из программы
    view.exit()
    quit()
    
    
    
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
