

input('Нажми ENTER  чтобы начать')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print('На данный момент проценты у банка по вкладам такие:' + (str(per_cent)))
per_cent_values=per_cent.values()
per_cent_list=list(per_cent_values)
money=(float(input('Введи сумму, которую Вы хотите положить:')))
deposit=[money*i*0.1 for i in per_cent_list]
print('Максимальная сумма, которую Вы можете заработать: ' + (str(max(deposit))))
input()
ываыва