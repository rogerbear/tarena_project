import os,sys,time

pid = os.fork()

if pid < 0:
    print('process failed')
elif pid == 0:
    print('child process:')
    time.sleep(2)
    sys.exit(1)
else:
    p,status = os.wait()
    print(p,status)
    print('parent process:')
    while True:
        pass
