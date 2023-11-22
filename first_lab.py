import random

import string

# Ввод идентификатора пользователя
user_identifier = input("Введите идентификатор пользователя: ")

a = ord('а')

ru_alphabet = [chr(i) for i in range(a,a+32)]

# Генерация пароля
password = ""

password += "".join([random.choice(ru_alphabet) for _ in range(3)])
password += "".join([random.choice(ru_alphabet).upper() for _ in range(2)])

# Генерация двузначных чисел
N = len(user_identifier)
N4 = N % 100
if N4 < 10:
    password += "0" + str(N4)
else:
    password += str(N4)

# Вывод пароля
print("Сгенерированный пароль:", password)
