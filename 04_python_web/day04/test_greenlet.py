from greenlet import greenlet

def test1():
    print(11111)
    gr2.switch()
    print(22222)
    gr2.switch()

def test2():
    print(33333)
    gr1.switch()
    print(44444)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()