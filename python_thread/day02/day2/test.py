from multiprocessing import Process
from time import sleep

a = 1


def worker(sec, msg):
    global a
    a = 1000
    for i in range(2):
        sleep(sec)
        print('u r the', msg)
    print(a)


p = Process(target=worker, name='worker', args=(2,), kwargs={'msg': 'good man!'})

print(p.is_alive())

p.start()

print(p.is_alive())

p.join()

print(p.name)
print(p.pid)
print(p.is_alive())

# worker(2,'sub process')
print('parent a:', a)
