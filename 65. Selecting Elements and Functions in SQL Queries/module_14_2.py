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
    "D:\\python progect\\HomeWorkUU\\65. Selecting Elements and Functions in SQL Queries\\not_telegram.db")
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

for i in range(1, 11, 2):
    coursor.execute(f"UPDATE Users SET balance = ? WHERE username = ?",
                    (500, f"User{i}"))

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

coursor.execute(f"DELETE FROM Users WHERE id = ?", (6,))

connection.commit()

print("ОСТАВШИЕСЯ ЗАПИСИ ПОСЛЕ УДАЛЕНИЯ")
print_user()
print("----------------------------------------------------")

coursor.execute("SELECT COUNT(*) FROM Users")
count_elements = coursor.fetchone()[0]
print(f"Количество записей: {count_elements}")

coursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = coursor.fetchone()[0]
print(f"Сумма всех балансов: {sum_balance}")

print(f"Средний баланс польльзователей: {sum_balance/count_elements}")

connection.close()
