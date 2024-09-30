#!/usr/bin/python
# coding: utf-8
import sqlite3
import pprint


def print_user():
    coursor.execute("SELECT * FROM Users")
    users = coursor.fetchall()
    for i in users:
        pprint.pprint(i)


connection = sqlite3.connect(
    "D:\\python progect\\HomeWorkUU\\64. Creating a database, adding, selecting and deleting elements\\not_telegram.db")
coursor = connection.cursor()

coursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
""")

connection.commit()

for i in range(1, 11):
    coursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))
connection.commit()

print("ДОБАВЛЕННЫЕ ЗАПИСИ В БД")
print_user()
print("----------------------------------------------------")


for i in range(1, 11):
    if i % 2 == 0:
        user_balance = coursor.execute(
            f"Select balance FROM Users WHERE username = ?", (f"User{i}",)).fetchone()
        coursor.execute(f"UPDATE Users SET balance = ? WHERE username = ?",
                        (user_balance[0] + 500, f"User{i}"))

connection.commit()

print("ИЗМЕННЫЙ БАЛАНС У КАЖДОЙ ВТОРОЙ ЗАПИСИ")
print_user()
print("----------------------------------------------------")


for i in range(1, 11, 3):
    coursor.execute(f"DELETE FROM Users WHERE username = ?", (f"User{i}",))

connection.commit()

print("ОСТАВШИЕСЯ ЗАПИСИ ПОСЛЕ УДАЛЕНИЯ")
print_user()
print("----------------------------------------------------")

coursor.execute("SELECT * FROM Users WHERE age <> 60")
users = coursor.fetchall()
print("РЕЗУЛЬТАТ")
for i in users:
    print(f"Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}")
print("----------------------------------------------------")
connection.close()
