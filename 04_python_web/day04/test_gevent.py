import gevent
import time


def foo(a, b):
    print('a,b:', a, b)
    gevent.sleep(3)
    print('switch foo again')


def bar():
    print('bar...')
    gevent.sleep(2)
    print('switch bar again')


f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)

# gevent.join(f)
# gevent.join(b)
gevent.joinall([f, b])
