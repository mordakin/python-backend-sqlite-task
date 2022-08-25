import sqlite3
import os

db = sqlite3.connect(os.path.abspath(__file__ + '/../../../corpus.db'))
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users
(
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    name                    VARCHAR(255) NOT NULL,
    surname                 VARCHAR(255) NOT NULL,
    patronymic              VARCHAR(255),
    country                 VARCHAR(255) NOT NULL,
    educational_institution VARCHAR(255) NOT NULL,
    phone_number            VARCHAR(50)  NOT NULL UNIQUE,
    email                   VARCHAR(255) NOT NULL UNIQUE,
    password                VARCHAR(255) NOT NULL,
    request_status          VARCHAR(20),
    is_admin                BOOLEAN DEFAULT FALSE,
    logged_in               BOOLEAN
)''')

db.commit()
db.close()
