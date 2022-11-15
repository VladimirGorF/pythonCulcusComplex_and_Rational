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
