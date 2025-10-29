"""В прогресс-баре принято использовать округление вниз (отбрасывание дробной части),
    а не обычное математическое округление, иначе может показаться, что шагов сделано больше,
    чем на самом деле.
    Поэтому количество символов '█' вычисляется так:

     int(доля * длина)
где:
     доля = выполненные_шаги / общее_количество"""

step_done, step_total, dlina_br = int(input()), int(input()), int(input())
done = '█'
ne_done = '░'

prgrs_prc = (step_done / step_total) * 100
dolja = step_done / step_total
prgrs_br_done = int(dolja * dlina_br)
prgrs_br_ne_done = dlina_br - prgrs_br_done

print(f'[{done * prgrs_br_done}{ne_done * prgrs_br_ne_done}] {prgrs_prc:.2f}% ({step_done} / {step_total})')





