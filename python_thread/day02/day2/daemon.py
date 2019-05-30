import multiprocessing as mp 
from time  import sleep 

def fun():
    print('Child process start')
    sleep(3)
    print("Child process end")

p = mp.Process(target = fun)
p.daemon = True
p.start()
# p.join()#join和daemon二选其一
sleep(1)
print("****main process over******")