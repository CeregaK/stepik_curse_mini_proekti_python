# Шаблон вывода успеваемости учеников
"""Вводимые данные:
--------------------
3
Анна иванова;95
Борис ПЕТРОВ;67
света сидорова;42
--------------------
5
Кукумбер ОГУРЦОВ;100
oneill patrick;89
екатерина;60
миша;59
ли;0
---------------------"""
n = int(input())
itog_result = 'ИТОГОВЫЕ РЕЗУЛЬТАТЫ:'
statistic = 'СТАТИСТИКА:'
l = n * 10 - 20
grade_summ = otl = hor = neud = 0
datas = []

for el in range(n):
    fio, grade = input().split(';')
    grade_summ += int(grade)

    if int(grade) > 90:
        status = 'с отличием'
        otl += 1
    elif 60 <= int(grade) < 90:
        status = 'зачёт'
        hor += 1
    else:
        status = 'незачёт'
        neud += 1

    data = f'Имя: {fio.title()}, Баллы: {grade}, Статус: {status}'
    datas.append(data)

print(f"{itog_result:*^{n * 10}}")

for el in datas:
    print(el)

print(f"""\
{statistic:*^{n * 10}}
{'Средний балл:':<20}{(grade_summ / n):>{l}.1f}
{'Отличники:':<20}{(otl / n):>{l}.1%}
{'Сдавшие:':<20}{(hor / n):>{l}.1%}
{'Не сдавшие:':<20}{(neud / n):>{l}.1%}""")
