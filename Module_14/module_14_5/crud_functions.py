import sqlite3


def initiate_db():
    connection = sqlite3.connect('Products.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
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
    cursor.execute(' CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')
    # for i in range(11, 16):
    #     cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    #                    (f'Зелье силы {i-10}', f'Дает + {(i-10)*2} бонус к силе на {i-10}ч.', f'{(i-10) * 200}'))
    connection.commit()
    connection.close()


if __name__ == '__main__':
    initiate_db()


def add_user(username, email, age):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users '
                   '(username, email, age, balance) '
                   'VALUES (?, ?, ?, ?)',
                   (username, email, age, str(1000)))
    connection.commit()
    connection.close()


def user_exists(username):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * From Users WHERE username = ?', (username, ))
    user_check = cursor.fetchone()
    if user_check is None:
        connection.commit()
        connection.close()
        return False
    elif user_check is not None:
        connection.commit()
        connection.close()
        return True


def get_total_products_amount():
    connection = sqlite3.connect('Products.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM Products')
    total_products = cursor.fetchone()[0]
    connection.commit()
    connection.close()
    return total_products


def get_all_products():
    connection = sqlite3.connect('Products.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(' SELECT title, description, price FROM Products ')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products
    # for product in products:
    #     print(f'Название: {product["title"]} | Описание: {product["description"]} | Цена: {product["price"]}')


