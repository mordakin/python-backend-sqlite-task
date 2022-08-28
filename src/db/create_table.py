import sqlite3
import os

db = sqlite3.connect(os.path.abspath(__file__ + '/../../../corpus.db'))
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS test_data
(
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    name                    VARCHAR(255) NOT NULL,
    surname                 VARCHAR(255) NOT NULL,
    patronymic              VARCHAR(255),
    country                 VARCHAR(255) NOT NULL,
    educational_institution VARCHAR(255) NOT NULL,
    phone_number            VARCHAR(255) NOT NULL UNIQUE,
    email                   VARCHAR(255) NOT NULL UNIQUE,
    password                VARCHAR(255) NOT NULL,
    request_status          VARCHAR(20),
    is_admin                BOOLEAN DEFAULT FALSE,
    logged_in               BOOLEAN
)''')


def data_insert_from_registration(dict_data):
    cur.execute('''INSERT INTO test_data
    (name,surname,patronymic,country,educational_institution,phone_number,email,password) 
    VALUES (:name,:surname,:patronymic,:country,:educational_institution,:phone_number,:email,:password)''',
                dict_data)
    db.commit()


def examination_of_user(email):
    cur.execute('''SELECT is_admin
    FROM test_data
    WHERE email = :email
    AND password =:password;
    ''', email)
    res = cur.fetchone()
    if res is None:
        print('\nЛогин или пароль указаны не верно, попробуйте снова')
        return None
    else:
        for i in res:
            return int(i)


def data_insert_request_status(email_user):
    cur.execute('''UPDATE test_data
    SET request_status = 'SENT'
    WHERE email =:email
    ''', email_user)
    db.commit()


def get_information_about_clients():
    cur.execute('''SELECT * FROM test_data
    WHERE is_admin = 0
    ''')
    res = cur.fetchall()
    for i in res:
        print('ID:', i[0])
        print('ФИО:', i[1], i[2], i[3])
        print('Страна:', i[4])
        print('Образовательное учреждение:', i[5])
        print('Телефон:', i[6])
        print('Почта:', i[7])
        print('Статус заявки:', i[9])
        print('\n')


def get_information_about_apply():
    cur.execute('''SELECT * FROM test_data
        WHERE is_admin = 0 
        AND request_status = 'SENT'
        ''')
    res = cur.fetchall()
    for i in res:
        print('ID:', i[0])
        print('ФИО:', i[1], i[2], i[3])
        print('Страна:', i[4])
        print('Телефон:', i[6])
        print('\n')