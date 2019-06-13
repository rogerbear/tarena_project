import signal 
import time 

#3秒后向自己发送一个SIGALRM信号
signal.alarm(3)
# time.sleep(4)#两个时钟之间不能存在阻塞，否则后面的时钟可能会不生效
signal.alarm(8)#覆盖上面的alarm

# signal.alarm(4)

signal.pause()

while  True:
    time.sleep(1)
    print("等待时钟....")
