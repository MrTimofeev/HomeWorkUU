#!/usr/bin/python
# coding: utf-8
import multiprocessing
import datetime


def read_info(name):
    all_data = []
    for i in name:
        print(i)
        with open(file=i, mode="r", encoding="utf-8") as file:
            for i in file:
                all_data.append(file.readline())


filenames = [
    f'.\\50. Multiprocess programming\\file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
read_info(filenames)
end = datetime.datetime.now()
print(end-start)

# if __name__ == '__main__':
#     start = datetime.datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, (filenames,))
#     end = datetime.datetime.now()
#     print(end-start)
