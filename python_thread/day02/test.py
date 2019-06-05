import multiprocessing as mp
from time import sleep
import os

def worker(msg):
    sleep(1)
    print(msg)
    return 'wokers return:' + msg

pool = mp.Pool(processes=4)

result = []
for i in range(10):
    msg = 'hello %d' % i
    r = pool.apply_async(worker,(msg,))
    # print(r)
    result.append(r)

for res in result:
    print(res.get())


pool.close()

pool.join()
