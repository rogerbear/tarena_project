import os

pid = os.fork()

if pid < 0:
    print('create process failed...')
elif pid == 0:
    pid2 = os.fork()
    if pid2 < 0:
        print('create sub_process failed...')
    elif pid2 == 0:
        print('pid2 sucess...')
    else:
        os._exit(0)
else:
    os.wait()
    print('parent process ok...')