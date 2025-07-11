def sum_digits(num):
    """Функция принимает число num и возвращает our_sum сумму цифр в полученном числе"""

    our_sum = 0
    while num >= 1:
        our_sum += num % 10
        num //= 10
    return our_sum




data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    12, 4, 7, 27, 10, 27
]


for i, d in enumerate(data):
    assert sum_digits(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')