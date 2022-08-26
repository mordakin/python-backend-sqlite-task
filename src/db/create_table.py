import sqlite3
import os

db = sqlite3.connect(os.path.abspath(__file__ + '/../../../corpus.db'))
cur = db.cursor()


# cur.execute('''
# CREATE TABLE IF NOT EXISTS test_dict2
# (
#     id                      INTEGER PRIMARY KEY AUTOINCREMENT,
#     name                    VARCHAR(255) NOT NULL,
#     surname                 VARCHAR(255) NOT NULL,
#     patronymic              VARCHAR(255),
#     email                   VARCHAR(255)
# )''')

def data_insert(dict_data):
    cur.execute('INSERT INTO test_dict2 (name,surname,patronymic,email) VALUES (:name,:surname,:patronymic,:email)',
                dict_data)
    # cur.execute('UPDATE test_dict2 SET email = :email WHERE name = "aaa"', users)
    db.commit()
