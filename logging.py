from datetime import datetime as dt


#  Эта функция логирования для калькулятора!
def calcus_logger(resault):  # Логирование для калькулятора, Принимает результат работы калькулятора
    time = dt.now().strftime("%d.%m.%Yг. %H:%M")  # Создаем time в формате день, месяц, год + часы +минуты события
    with open('log_calcus.csv', 'a') as file:  # добавляем файл "log_calcus.csv" - Журнал калькулятора
        file.write('{}; calcus;{}\n'.format(time, resault))  # записываем в наш файл дату события и резул.калькулятора
    with open('log.csv', 'a') as file:  # добавляем файл "log.cvs" на запись - Журнал всех событий
        file.write('{}; calcus; {}\n'.format(time, resault))  # записываем в него дату события и результат калькулятора


#  Логирование Входа,Выхода пользователя из программы и обработки ошибок!
def common_logger(data):
    time = dt.now().strftime("%d.%m.%Yг. %H:%M")  # создаем time в формате день, месяц, год + часы +минуты события
    with open('log.csv', 'a') as file:  # добавляем файл "log.cvs" Журнал всех событий
        file.write('{}; common; {}\n'.format(time, data))  # записываем дату события и вход/выход в программу или ошибки


data = 'вход пользователя или выход или ошибка '
resault = '25 - результат  работы калькулятора'
calcus_logger(resault)
common_logger(data)
        
        
# для вызова функции логирования используйте:       
import logging
logging.calcus_logger(resault)

# для вызова функции логирования используйте:       
import logging
logging.common_logger(data)

# для просмотра журнала калькулятора используйте:
with open('log_calcus.csv', 'r') as file:
    for line in file:
        print(line)

# для просмотра общего журнала используйте:
with open('log.csv', 'r') as file:
    for line in file:
        print(line)       
        
        
