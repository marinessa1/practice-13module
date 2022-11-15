# Задание 13.8.19
# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается
# стоимость:
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек
# на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
#
# Ответ:

price_all = 0

ticket_number = int(input('Введите количество билетов: '))

for i in range(ticket_number):
    age_for_ticket = int(input(f'Для какого возраста билет №{i}? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        price_all += 990
        print('Стоимость билета: 990 руб.')
    else:
        price_all += 1390
        print('Стоимость билета: 1390 руб.')

if ticket_number > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки.')
else:
    print(f'Сумма к оплате {price_all} руб.')
