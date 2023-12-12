#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Список студентов
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            grade = list(map(int, input("Успеваемость студента? (Пять оценок через пробел) ").split()))
            while True:
                if len(grade) < 5:
                    print("Введное количество оценок меньше 5, введите оценки еще раз: ", file=sys.stderr)
                    grade = list(map(int, input("Успеваемость студента? (Пять оценок через пробел) ").split()))
                else:
                    break

            # Создать словарь.
            if sum(grade)/len(grade) >= 4.0:
                student = {
                    'name': name,
                    'group': group,
                    'grade': sum(grade)/len(grade),
                }
                # Добавить словарь в список.
                students.append(student)
            
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            if students:
                print("Список студентов с успеваемостью больше 4.0")
                # Заголовок таблицы.
                line = '+-{}-+-{}-+-{}-+'.format(
                    '-' * 4,
                    '-' * 30,
                    '-' * 20
                )
                print(line)
                print(
                    '| {:^4} | {:^30} | {:^20} |'.format(
                        "No",
                        "Ф.И.О.",
                        "Группа"
                    )
                )
                print(line)

                # Вывести данные о всех сотрудниках.
                for idx, student in enumerate(students, 1):
                    print(
                        '| {:>4} | {:<30} | {:<20} |'.format(
                            idx,
                            student.get('name', ''),
                            student.get('group', '')
                        ) 
                    )

                print(line)
            
            else:
                print("Студентов с успеваемостью выше 4.0 нет")
        
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
