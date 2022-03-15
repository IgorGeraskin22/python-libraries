# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor




# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


def main():
    try:
        make_ticket(surname_name, departure, arrival, departure_date)
    except FileNotFoundError:
        print("Файл не найден")


def make_ticket(fio, from_, to, date):
    draw.text((w - 630, h - 280), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((w - 625, h - 210), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((w - 625, h - 145), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((w - 385, h - 145), date, font=font, fill=ImageColor.colormap['black'])

    path.save('ticket_template_res.png')


if __name__ == '__main__':
    surname_name = input('Введите ФИО:')
    departure = input('Введите аэропорт вылета:')
    arrival = input('Введите аэропорт прилета:')
    departure_date = input('Введите дату вылета:')
    path = os.path.join(os.path.dirname(__file__), 'images', 'ticket_template.png')
    path = Image.open(path)
    draw = ImageDraw.Draw(path)
    w, h = path.size
    font = ImageFont.truetype("arial.ttf", 15)
    make_ticket(surname_name, departure, arrival, departure_date)
    main()
