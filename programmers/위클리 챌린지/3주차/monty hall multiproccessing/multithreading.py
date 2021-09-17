import multiprocessing
import time
import os

st = time.time()

def count(name):
    for _ in range(10):
        with multiprocessing.Lock(): temp.value += 1
        # print(f"{name} {temp}")
        

num_list = ['P1', 'P2', 'P3', 'P4']

if __name__ == '__main__':
    temp = multiprocessing.Value('i', 0)
    pool = multiprocessing.Pool()
    pool.map(count, num_list)
    pool.close()
    pool.join()

print(f"{temp.value}, {time.time() - st} seconds")