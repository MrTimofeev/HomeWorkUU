#!/usr/bin/python
# coding: utf-8
import multiprocessing
import datetime


def read_info(name):
    all_data = []
    print(name)
    with open(file=name, mode="r", encoding="utf-8") as file:
        for line in file:
            # Проверяем, является ли строка пустой
            if line == '':
                break

            all_data.append(line)


filenames = [
    f'.\\50. Multiprocess programming\\file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.datetime.now()
print(end-start)

# if __name__ == '__main__':
#     start = datetime.datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     end = datetime.datetime.now()
#     print(end-start)
