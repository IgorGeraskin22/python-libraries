# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fio', type=str)
    parser.add_argument('from_', type=str)
    parser.add_argument('to', type=str)
    parser.add_argument('date', type=str)
    parser.add_argument('save', type=str)
    args = parser.parse_args()
    make_ticket(args.fio, args.from_, args.to, args.date, args.save)
    print(args)


def make_ticket(fio, from_, to, date, save):
    try:
        path = os.path.join(os.path.dirname(__file__), 'images', 'ticket_template.png')
        path = Image.open(path)
        draw = ImageDraw.Draw(path)
        w, h = path.size
        font = ImageFont.truetype("arial.ttf", 15)

        draw.text((w - 630, h - 280), fio, font=font, fill=ImageColor.colormap['black'])
        draw.text((w - 625, h - 210), from_, font=font, fill=ImageColor.colormap['black'])
        draw.text((w - 625, h - 145), to, font=font, fill=ImageColor.colormap['black'])
        draw.text((w - 385, h - 145), date, font=font, fill=ImageColor.colormap['black'])

        path.save(save)

    except FileNotFoundError:
        print("Файл не найден")


if __name__ == '__main__':
    main()

# Команда запуска программы
# python 01_ticket_01_argparse.py  "Гераскин Игорь" "Челябинск" "Анталья"  "23.07" "ticket_template_res.png"
