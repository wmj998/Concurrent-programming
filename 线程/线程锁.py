from threading import Thread, Lock

lock = Lock()  # 创建锁
n = 5000


def fun1():
    global n
    for i in range(1000000):
        lock.acquire()  # 上锁
        n += 1
        lock.release()  # 释放锁


def fun2():
    global n
    for i in range(1000000):
        lock.acquire()
        n -= 1
        lock.release()


t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()

print(n)
