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
    cursor.execute(' CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')
    for i in range(1, 11):
        cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Зелье {i}', f'Дает 100% бонус к интеллекту на {i}ч.', f'{i * 100}'))
    connection.commit()
    connection.close()


# if __name__ == '__main__':
#     initiate_db()



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


