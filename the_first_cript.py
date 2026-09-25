import time

true_code = '1234'
code = ''

while code != true_code:
    code = input('Введите код: ')
    if code != true_code:
        print('Неверный код, попробуйте ещё')
print('Доступ разрешён!')
time.sleep(1)

print('Что хочешь сделать?\n1. Посчитать сколько денег ещё нужно накопить\n2. Воспользоваться калькулятером \n3. Проверить есть ли в твоём имени гласные буквы')
otvet_list = int(input())
time.sleep(2)
if otvet_list == 1:
    money = 1
    total_sum = 0
    while money != 0:
        money = int(input('Сколько денег ты сейчас сможешь положить? '))
        if money < 0:
            print('Нельзя класть меньше 0!')
        elif money > 0:
            total_sum += money
            print(f'Сейчас вкопилке {total_sum} рублей!')
    print(f'Ты накопил {total_sum} рублей.')

if otvet_list == 2:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    oper = input('Что хотите сделать? ')
    if oper == '+':
        result = num_1 + num_2
    elif oper == '-':
        result = num_1 - num_2
    elif oper == '*':
        result = num_1 * num_2
    elif oper == '/':
        if num_2 == 0:
            result = 'На ноль нельзя делить!'
        if num_2 != 0:
            result = num_1 / num_2
    else:
        result = 'Неизвестная операция'
    print(result)

if otvet_list == 3:
    r = input('Введите своё имя: ')
    flag = False

    for i, z in enumerate(r):
        if z in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ':
            print(f'В твоём имени есть гласные: {z}')
            flag = True
    if not flag:
        print('В твоём имени нет гласных')