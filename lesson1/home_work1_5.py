revenue = int(input('ваша выручка: '))
cost = int(input('ваши издержки: '))

profit = revenue - cost

if profit < 0:
    print(f'Вы работаете с убытком {profit}')
if profit == 0:
    print('Вы работаете без прибыли и убытков')
if profit > 0:
    print(f'Вы работаете с прибылью {profit}!')
    staff = int(input('сколько у вас сотрудников? '))
    profit_staff = profit / staff
    print(f'Прибыль на одного сотрудника: {profit_staff}')