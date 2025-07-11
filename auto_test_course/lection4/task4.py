def multiplication_chain(num):
    """Функция multiplication_chain прнимает положительное число num и возвращает колличество
     сложений цифр числа, пока чтсло не станет цифрой
     Например 39 --> 3 (потому что 3*9 = 27, 2*7 = 14, 1*4 = 4, вот 4 одна цифра. Итого 3 итерации)"""
    count_multi = 0
    while num >= 10:
        digit = [int(i) for i in str(num)]
        chislo = 1
        for i in digit:
            chislo *= i
        num = chislo
        count_multi += 1
    return count_multi





data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]


for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')