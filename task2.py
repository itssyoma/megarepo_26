#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Создание словаря, где ключами являются числа, а значениями – строки
    original_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }

    # Применение метода items() для получения объекта dict_items
    dict_items = original_dict.items()

    # Создание нового словаря, "обратного" исходному
    reversed_dict = {value: key for key, value in dict_items}

    print(reversed_dict)
