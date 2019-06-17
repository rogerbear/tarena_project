import threading
from time import ctime, sleep
import threadpool


class MyThread(threading.Thread):
    def __init__(self, func, args, name = 'player'):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def player(file, time):
    for i in range(3):
        print('starting %s: %s', (file, ctime()))
        sleep(time)


t = MyThread(player, ('only u.mp3', 2))
t.start()
t.join()
