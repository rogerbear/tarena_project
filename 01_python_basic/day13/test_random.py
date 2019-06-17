import random

#''.join([chr(x) for x in range(ord('A'),ord('A')+26)])

def ran_sec(n):
    s = ''
    source = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'
    for _ in range(n):
        s += random.choice(source)
    return s

print(ran_sec(6))