from signal import *
import time

def handler(sig,frame):
    if sig == SIGALRM:
        print('SIGALRM...')
    elif sig == SIGINT:
        print('SIGINT...')

signal(SIGALRM, handler)
signal(SIGINT, handler)

alarm(6)

while True:
    time.sleep(2)
    print('waiting for signal...')