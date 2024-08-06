#!/usr/bin/python
# coding: utf-8

class UrTube():
    UrTube_users = []
    UrTube_videos = []
    current_user = None

    def __init__(self):
        pass

    def log_in(cls, nickname, password):
        for i in cls.UrTube_users:
            if i.nickname == nickname and i.password == hash(password):
                cls.current_user = i
                print(f"Добро пожаловать {nickname} на нашу первую версию UrTube!!!")
                return
        print("Возможно учетной записи не существует! Создайте учетную запись либо проверьте правильность введенного логина и пароля!!")

    def register(cls, nickname, password, age):
        if(cls.current_user != None):
            print("Необходимо выйти из текущей учетной записи, чтобы создатить новую или сменить текущую!")
            return

        if(len(password) <5):
            print("Длинна пароля должна быть не меньше 6 символов")
            return
        
        if(len(nickname) <6):
            print("Длинна вашего nickname должна быть не меньше 6 символов")
            return

        for i in cls.UrTube_users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        cls.UrTube_users.append(
            User(nickname=nickname, password=password, age=age))
        cls.log_in(nickname=nickname, password=password)

    def log_out(cls):
        cls.current_user = None
        print("Вы вышли из учетной записи!")

    def add(cls, *videos):
        for item in videos:
            flag = True

            for ur_video in cls.UrTube_videos:
                if (item.title == ur_video.title):
                    flag = False

            if flag:
                cls.UrTube_videos.append(Video(
                    title=item.title, duration=item.duration, time_now=item.time_now, adult_mode=item.adult_mode))

    def get_videos(cls, title_video):
        list_video = []
        for i in cls.UrTube_videos:
            if title_video.lower() in i.title.lower():
                list_video.append(i.title)
        return list_video

    def watch_video(cls, title_video):
        if cls.current_user == None:
            print("Войдите в аккаунт чтобы смотреть видео!!")
            return

        for i in cls.UrTube_videos:
            if i.title == title_video:
                if (cls.current_user.age < 18 and i.adult_mode == True):
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for t_video in range(i.time_now, i.duration):
                    print(t_video+1)

                #обнуление начала просмотра
                i.time_now = 0
    def __str__(cls):
        if cls.current_user == None:
            return "Нет текущего пользователя"
        else:
            return cls.current_user.nickname


class Video():
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
