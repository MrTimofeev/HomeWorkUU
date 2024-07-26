#!/usr/bin/python
#coding: utf-8

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" not in sender or "@" not in recipient:
        print(f"Невозможно отпрпвить письмо  с адреса {sender} на адрес {recipient}")
        return
    elif '.com' != recipient[-4:] and '.ru' != recipient[-3:] and '.net' != recipient[-4:]:
        print(f"Невозможно отпрпвить письмо с адреса {sender} на адрес {recipient}")
        return
    elif '.com' != sender[-4:] and '.ru' != sender[-3:] and '.net' != sender[-4:]:
        print(f"Невозможно отпрпвить письмо с адреса {sender} на адрес {recipient}")
        return
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

    
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

