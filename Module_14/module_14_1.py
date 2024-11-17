import sqlite3
import random
from pprint import pprint


connection = sqlite3.connect("not_telegram.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
''')

cursor.execute(' CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(1, 11):
#     cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', str(random.randint(58, 62)), str(1000)))

# cursor.execute(' UPDATE Users SET balance = balance - 500 WHERE id = 1')
# cursor.execute(' UPDATE Users SET balance = balance - 500 WHERE id % 2 = 0')
# cursor.execute(' DELETE FROM Users WHERE id = 1 ')
# cursor.execute(' DELETE FROM Users WHERE id % 3 == 0')

cursor.execute(' SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user["username"]} | Почта: {user["email"]} | Возраст: {user["age"]} | Баланс: {user["balance"]}')
connection.commit()
connection.close()
