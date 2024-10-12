import multiprocessing
from datetime import datetime

filenames = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline():
            all_data.append(file.readline())


# start = datetime.now()
# for i in filenames:
#     read_info(i)
# end = datetime.now()
# print(end - start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        all_files = []
        for i in filenames:
            all_files.append(i)
        start = datetime.now()
        pool.map(read_info, all_files)
    end = datetime.now()
    print(end - start)

