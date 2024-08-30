import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as f:
        all_data = f.read().splitlines()



if __name__ == '__main__':
    files_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    start = datetime.now()
    read_info('file 1.txt')
    read_info('file 2.txt')
    read_info('file 3.txt')
    read_info('file 4.txt')
    end = datetime.now()
    print(end - start)
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, files_list)
    end = datetime.now()
    print(end - start)


