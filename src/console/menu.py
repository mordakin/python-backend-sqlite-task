import sys
from src.db.create_table import data_insert_from_registration


def authorization():
    print('''Авторизация
1. Логин
2. Регистрация
3. Закрыть программу''')
    choice = int(input('Введите номер варианта: '))
    if choice == 1:
        login_menu()
    elif choice == 2:
        registration_menu()
    elif choice == 3:
        sys.exit()
    else:
        print('Неккоректный ввод, попробуйте снова')
        authorization()


def login_menu():
    print('\nПодсказка: для выхода напишите exit\n')
    input('Введите email: ')
    input('Введите пароль: ')
    pass  # переход к меню юзера или админа


def registration_menu():
    global dict_data
    dict_data = {}
    print('\nПодсказка: для выхода напишите exit\n')
    name = input('Введите имя: ')
    if name == 'exit':
        authorization()
    else:
        dict_data['name'] = name
    surname = input('Введите фамилию: ')
    if surname == 'exit':
        authorization()
    else:
        dict_data['surname'] = surname
    patronymic = input('Введите отчество: ')
    if patronymic == 'exit':
        authorization()
    else:
        dict_data['patronymic'] = patronymic
    country = input('Введите страну: ')
    if country == 'exit':
        authorization()
    else:
        dict_data['country'] = country
    educational_institution = input('Введите образовательное учреждение: ')
    if educational_institution == 'exit':
        authorization()
    else:
        dict_data['educational_institution'] = educational_institution
    phone_number = input('Введите номер телефона: ')
    if phone_number == 'exit':
        authorization()
    else:
        dict_data['phone_number'] = phone_number
    email = input('Введите email: ')
    if email == 'exit':
        authorization()
    else:
        dict_data['email'] = email
    password_func()


def password_func():
    password = input('Введите пароль: ')
    repeat_password = input('Повторите пароль: ')
    if password != repeat_password:
        print('Пароли не совпадают, попробуйте снова')
        password_func()
    else:
        dict_data['password'] = password
        data_insert_from_registration(dict_data)
        menu_users()


def menu_users():
    print('''
Меню пользователя
1. О проекте
2. Лица проекта
3. Подать заявку в лагерь
4. Выйти из аккаунта
5. Закрыть программу''')
    choice = int(input('Введите номер варианта: '))
    if choice == 1:
        about_project()
    elif choice == 2:
        face_of_program()
    elif choice == 3:
        apply()
    elif choice == 4:
        authorization()
    elif choice == 5:
        sys.exit()
    else:
        print('Неккоректный ввод, попробуйте снова')
        menu_users()


def about_project():
    print('''
О проекте
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.

1. Назад
2. Выйти из аккаунта
3. Закрыть программу
''')
    choice = int(input('Введите номер варианта: '))
    if choice == 1:
        menu_users()
    elif choice == 2:
        authorization()
    elif choice == 3:
        sys.exit()


def face_of_program():
    print('''
Лица проекта
№1
ФИО: Василий Анатольевич Пупкин
Специальность: Русский язык
Опыт работы: 10 лет

№2
ФИО: Пётр Петрович Гриб
Специальность: Английский язык
Опыт работы: 10 лет

1. Назад
2. Выйти из аккаунта
3. Закрыть программу
''')
    choice = int(input('Введите номер варианта: '))
    if choice == 1:
        menu_users()
    elif choice == 2:
        authorization()
    elif choice == 3:
        sys.exit()


def apply():
    print('''Заявка отправлена на рассмотрение''')
    # отправление заявки в БД
    menu_users()


def admin_menu():
    print('''
Меню администратора
1. Все клиенты
2. Заявки
3. Выход из аккаунта
4. Закрыть программу
''')
    choice = int(input('Введите номер варианта: '))
    if choice == 1:
        all_clients()
    elif choice == 2:
        pass
    elif choice == 3:
        authorization()
    elif choice == 4:
        sys.exit()


def all_clients():
    pass  # придумать как выводить инфу о всех пользователях


def statement():
    pass  # придуматб как вывести информацию о заявках


registration_menu()
