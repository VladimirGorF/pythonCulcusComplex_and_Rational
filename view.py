import easygui

def exit(): # Выводит на экран сообщение о выходе
    easygui.msgbox(msg='До свидания!', title='Завершение работы с программой')

def get_numeric_expression(): # Запрашивает у пользователя ввод строки, убирает пробелы
    # global expression
    user_expression = easygui.enterbox(msg="Введите выражение", title='Калькулятор. Ввод выражения для вычисления')
    expression = user_expression.split()
    expression = ''.join(expression)
    return expression

def show_result(expression, result): # Выводит результат расчета калькулятора пользователю
    ex = expression
    res = result
    msg = f'Результат выражения {ex} :\n\n{res}'
    title = 'Результат расчета калькулятора'
    easygui.msgbox(msg, title)
    
def show_calc_log():
    msg = 'История расчетов калькулятора'
    title = 'Лог калькулятора'
    with open('log_calcus.csv', 'r') as file:
        line = file.read()
    easygui.textbox(msg, title, line)

def show_general_log():
    msg = 'Ваша история использования программы'
    title = 'Общий лог программы'
    with open('log.csv', 'r') as file:
        line = file.read()
    easygui.textbox(msg, title, line)
    
def show_expression_error():
    user_expression = easygui.enterbox(msg="Выражение введено некорректно, введите верно", title='Калькулятор. Ввод выражения для вычисления')
    expression = user_expression.split()
    expression = ''.join(expression)
    return expression
