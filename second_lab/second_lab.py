import os
import re
from db import User


logged_in: bool = False
username: str = None
password: str = None

def choose():
    # os.system("clear")
    print(f"""
          _            _           
    /\   | |          | |          
   /  \  | |     _ __ | |__   __ _ 
  / /\ \ | |    | '_ \| '_ \ / _` |
 / ____ \| |____| |_) | | | | (_| |
/_/    \_\______| .__/|_| |_|\__,_|
                | |                
                |_|                
{'Вы авторизованы в системе!' if logged_in else ''}
Выберите действие:
1. Регистрация
2. Вход
3. Доступ к ресурсу
4. Смена пароля    
""")

    choice = int(input("Введите номер пункта --> "))

    return choice

def validate_phone(entered: str):
    phone_pattern = re.compile(r'^9\d{9}$')

    if phone_pattern.match(entered):
        return True
    else:
        return False

def registrate():
    asks = ["имя пользователя", "пароль (только цифры!)", "полное имя", "дату рождения", "место рождения", "номер телефона (в формате 9ххххххххх)"]

    data = [input(f"Введите {ask} --> ") for ask in asks]

    if not data[1].isdigit():
        print("Пароль должен составлять только из цифр! Повторите регистрацию.")

        return registrate()

    if not validate_phone(data[5]):
        print("Номер телефона не соответствует введенному формату, регистрируйтесь заново.")

        return registrate()

    User.create(
        username=data[0],
        password=data[1],
        full_name=data[2],
        birth_date=data[3],
        birth_place=data[4],
        phone_number=data[5]
    )

    print("Вы успешно прошли регистрацию!")


def change_password():
    a = input("Введите номер телефона --> ")

    if User.get_or_none(User.phone_number == a, User.username == username):
        pwd = input("Ввведите новый паронь (только цифры) --> ")

        if not pwd.isdigit():
            print("Повторите еще раз! Неверный формат пароля! Нужны только цифры!")
            return change_password()

        User.update({User.password: pwd}).where(User.username == username).execute()

        print("Пароль успешно обновлен!")

    else:
        print("Номер телефона не совпадает, повторите еще раз")
        return change_password()


def enter():
    global username, password
    uname = input("Введите имя пользователя --> ")
    pwd = input("Введите пароль --> ")

    if User.get_or_none(User.username == uname, User.password == pwd):
        # logged_in = True
        print("Вы успешно вошли в систему!")
        username = uname
        pasword = pwd
        return True

    else:

        print("Неверные данные для входа. Повторите попытку!")
        return enter()


def check_logged():
    return os.path.exists("log")


while True:

    choice = choose()

    # регистрация
    if choice == 1:
        registrate()

        choice = choose()

    # вход
    if choice == 2:
        logged_in = enter()

        choice = choose()

    # доступ к ресурсу
    if choice == 3:

        if logged_in:
            print("Получаем...")
            print(open("secret.txt", 'r').read())

    if choice == 4:
        if logged_in:
            change_password()

            choice = choose()