from datetime import datetime as dt                         # вызываем класс для работы с датами и временем


def calcus_logger(data):                                    #Создаем функцию логирования
    time = dt.now().strftime("%d.%m.%Yг. %H:%M")            # создаем объект time в формате день, месяц, год + часы +минуты события для последующей работы с ним ниже
    with open('log.cvs', 'a') as file:                      #открываем файл "log.cvs" как объект "file"
        file.write('{}; calcus;{}\n'.format(time, data))    # записываем в наш файл построчно дату события и данные принимаемые функцией
