import sqlite3


def initiate_db():
    connection = sqlite3.connect(
        "telegram_bot.db")
    coursor = connection.cursor()

    coursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    path_photo TEXT NOT NULL)
    """)

    coursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    """)

    connection.commit()

    return coursor


def add_user(username, email, age):
    coursor = initiate_db()
    coursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                    (username, email, age, 1000))
    coursor.connection.commit()


def is_included(username):
    coursor = initiate_db()
    coursor.execute(f"SELECT * FROM Users WHERE username = ?", (username,))
    users = coursor.fetchall()

    if len(users) == 0:
        return False
    else:
        return True


def get_all_products():
    coursor = initiate_db()
    coursor.execute("SELECT * FROM Products")
    products = coursor.fetchall()
    print(products)
    coursor.connection.close()
    return products


def append_products():
    coursor = initiate_db()
    coursor.execute(f"INSERT INTO Products (title, description, price, path_photo) VALUES (?, ?, ?, ?)",
                    ("Картинка 1", "Кот хоба", "100 рубликов", "\\Кот хоба.jpg"))
    coursor.execute(f"INSERT INTO Products (title, description, price, path_photo) VALUES (?, ?, ?, ?)",
                    ("Картинка 2", "Кот без сигнала", "100 рубликов", "\\Кот без сигнала.jpg"))
    coursor.execute(f"INSERT INTO Products (title, description, price, path_photo) VALUES (?, ?, ?, ?)",
                    ("Картинка 3", "Грустный кот", "100 рубликов", "\\Грустный кот.jpg"))
    coursor.execute(f"INSERT INTO Products (title, description, price, path_photo) VALUES (?, ?, ?, ?)",
                    ("Картинка 4", "Гига кот", "100 рубликов", "\\Гига кот.jpg"))
    coursor.connection.commit()
    coursor.connection.close()
