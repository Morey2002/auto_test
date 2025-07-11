def create_phone_number(num_tuple):
    """Функция create_phone_number принимает кортеж num_tuple из 10 цифр num_tuple
    возвращает строку этих чисел в виде номера телефона str_phone
    Например (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890" """
    digits = ''.join(map(str, num_tuple))
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')